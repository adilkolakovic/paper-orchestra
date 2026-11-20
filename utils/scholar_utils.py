# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import requests
import time
import threading
from email.utils import parsedate_to_datetime
from typing import List, Dict, Optional
from thefuzz import fuzz  # type: ignore
import datetime

from dotenv import load_dotenv  # type: ignore

cur_dir = os.path.dirname(os.path.realpath(__file__))
load_dotenv(os.path.join(cur_dir, "../.env"))
S2_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
if S2_API_KEY:
    print("Semantic Scholar API key is configured.")

_S2_REQUEST_LOCK = threading.Lock()
_S2_MIN_REQUEST_INTERVAL_SECONDS = 2.0
_S2_LAST_REQUEST_AT = 0.0
_S2_BACKOFF_UNTIL = 0.0


def _s2_retry_delay(retry_after: Optional[str], attempt: int) -> float:
    try:
        delay = float(retry_after) if retry_after else 2**attempt
    except ValueError:
        try:
            retry_time = parsedate_to_datetime(retry_after)
            delay = max(0.0, retry_time.timestamp() - time.time())
        except (TypeError, ValueError, OverflowError):
            delay = 2**attempt
    return max(delay, 1.0)


def _s2_request(
    method: str,
    url: str,
    params: Dict,
    timeout: int,
    json_body: Optional[Dict] = None,
) -> requests.Response:
    global _S2_BACKOFF_UNTIL, _S2_LAST_REQUEST_AT
    headers = {"X-API-KEY": S2_API_KEY} if S2_API_KEY else {}

    for attempt in range(4):
        with _S2_REQUEST_LOCK:
            now = time.monotonic()
            wait_seconds = max(
                _S2_MIN_REQUEST_INTERVAL_SECONDS - (now - _S2_LAST_REQUEST_AT),
                _S2_BACKOFF_UNTIL - now,
            )
            if wait_seconds > 0:
                time.sleep(wait_seconds)

            response = requests.request(
                method,
                url,
                headers=headers,
                params=params,
                json=json_body,
                timeout=timeout,
            )
            _S2_LAST_REQUEST_AT = time.monotonic()
            if response.status_code == 429:
                delay = _s2_retry_delay(
                    response.headers.get("Retry-After"), attempt
                )
                _S2_BACKOFF_UNTIL = max(
                    _S2_BACKOFF_UNTIL,
                    _S2_LAST_REQUEST_AT + delay,
                )

        if response.status_code != 429:
            response.raise_for_status()
            return response

        if attempt == 3:
            response.raise_for_status()

    raise RuntimeError("Semantic Scholar retry loop exited unexpectedly.")


# --- SEMANTIC SCHOLAR UTILS ---


def s2_title_search(
    title_query: str, year_hint: int = None, cutoff_date: str = None
) -> Optional[Dict]:
    def is_date_valid(p_date, p_year, cutoff_str):
        if not cutoff_str:
            return True
        try:
            c_year, c_month = map(int, cutoff_str.split("-"))
            cutoff_dt = datetime.datetime(c_year, c_month, 1)
            if p_date:
                try:
                    p_dt = datetime.datetime.strptime(p_date, "%Y-%m-%d")
                    return p_dt < cutoff_dt
                except ValueError:
                    pass
            if p_year:
                if p_year < c_year:
                    return True
                if p_year == c_year and c_month > 1:
                    return True
                return False
            return True
        except Exception:
            return True

    try:
        rsp = _s2_request(
            method="GET",
            url="https://api.semanticscholar.org/graph/v1/paper/search",
            params={
                "query": title_query,
                "limit": 3,
                "fields": "title,authors,venue,year,abstract,citationCount,journal,publicationDate",
            },
            timeout=20,
        )
        results = rsp.json().get("data", [])
        if not results:
            return None

        best_match = None
        highest_ratio = 0

        for r in results:
            if not r.get("title"):
                continue
            if not is_date_valid(r.get("publicationDate"), r.get("year"), cutoff_date):
                continue

            ratio = fuzz.ratio(title_query.lower(), r["title"].lower())
            if year_hint and r.get("year") == year_hint:
                ratio += 10

            if ratio > highest_ratio:
                highest_ratio = ratio
                best_match = r

        if highest_ratio > 70:
            return best_match
        return None
    except Exception as e:
        print(f"      ⚠️ S2 Error for '{title_query}': {e}")
        return None


def s2_paper_search(query: str, limit: int = 10) -> List[Dict]:
    response = _s2_request(
        method="GET",
        url="https://api.semanticscholar.org/graph/v1/paper/search/bulk",
        params={
            "query": query,
            "fields": "paperId,title,year",
        },
        timeout=20,
    )
    return [
        paper
        for paper in response.json().get("data", [])[:limit]
        if paper.get("paperId") and paper.get("title")
    ]


def s2_paper_batch(paper_ids: List[str]) -> Dict[str, Dict]:
    fields = (
        "title,authors,venue,year,abstract,citationCount,"
        "journal,publicationDate"
    )
    papers_by_id = {}
    for start in range(0, len(paper_ids), 500):
        response = _s2_request(
            method="POST",
            url="https://api.semanticscholar.org/graph/v1/paper/batch",
            params={"fields": fields},
            json_body={"ids": paper_ids[start : start + 500]},
            timeout=30,
        )
        for paper in response.json():
            if paper and paper.get("paperId"):
                papers_by_id[paper["paperId"]] = paper
    return papers_by_id
