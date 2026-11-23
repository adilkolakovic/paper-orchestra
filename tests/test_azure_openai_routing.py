import os
import threading
import unittest
from unittest.mock import Mock, patch

from google.genai import types
import requests

from methods.agents.literature_review_agent import HybridLiteratureAgent
from utils.gemini_utils import call_gemini_with_contents
from utils.openai_utils import is_azure_openai_deployment
from utils.scholar_utils import s2_paper_batch, s2_paper_search


class AzureOpenAIRoutingTests(unittest.TestCase):
    def test_configured_deployment_is_recognized(self):
        with patch.dict(
            os.environ,
            {
                "AZURE_OPENAI_ENDPOINT": "https://example.openai.azure.com",
                "OPENAI": "paper-writer",
            },
        ):
            self.assertTrue(is_azure_openai_deployment("paper-writer"))
            self.assertFalse(is_azure_openai_deployment("gemini-3.1-pro-preview"))

    def test_gemini_content_call_routes_configured_deployment(self):
        with (
            patch.dict(
                os.environ,
                {
                    "AZURE_OPENAI_ENDPOINT": "https://example.openai.azure.com",
                    "OPENAI": "paper-writer",
                },
            ),
            patch(
                "utils.gemini_utils.call_openai_models_with_content",
                return_value={"raw_response": "ok", "parsed_response": "ok"},
            ) as openai_call,
        ):
            result = call_gemini_with_contents(
                contents=[types.Part.from_text(text="test prompt")],
                model_name="paper-writer",
                result_parsing_func=lambda response: response,
            )

        self.assertEqual(result["parsed_response"], "ok")
        self.assertEqual(
            openai_call.call_args.kwargs["content"],
            [{"type": "text", "text": "test prompt"}],
        )

    def test_azure_route_omits_unsupported_temperature(self):
        with (
            patch.dict(
                os.environ,
                {
                    "AZURE_OPENAI_ENDPOINT": "https://rzsoai-ist.openai.azure.com/",
                    "OPENAI": "paper-writer",
                },
            ),
            patch(
                "utils.gemini_utils.call_openai_models_with_content",
                return_value={"raw_response": "ok", "parsed_response": "ok"},
            ) as openai_call,
        ):
            call_gemini_with_contents(
                contents=[types.Part.from_text(text="review prompt")],
                model_name="paper-writer",
                generation_configs={
                    "temperature": 0.75,
                    "system_instruction": "reviewer instructions",
                },
                result_parsing_func=lambda response: response,
            )

        self.assertNotIn(
            "temperature",
            openai_call.call_args.kwargs["generation_configs"],
        )

    def test_semantic_scholar_retries_rate_limited_search(self):
        limited_response = Mock(
            status_code=429,
            headers={"Retry-After": "3"},
        )
        success_response = Mock(
            status_code=200,
            headers={},
            json=lambda: {
                "data": [
                    {
                        "paperId": "paper-1",
                        "title": "Causal inference",
                        "year": 2024,
                    }
                ]
            },
        )
        with (
            patch("utils.scholar_utils.requests.request") as request,
            patch("utils.scholar_utils.time.sleep") as sleep,
            patch("utils.scholar_utils.time.monotonic", return_value=100),
            patch("utils.scholar_utils._S2_LAST_REQUEST_AT", 0),
            patch("utils.scholar_utils._S2_BACKOFF_UNTIL", 0),
        ):
            request.side_effect = [limited_response, success_response]
            papers = s2_paper_search("causal inference")

        self.assertEqual(papers[0]["title"], "Causal inference")
        self.assertEqual(request.call_count, 2)
        sleep.assert_any_call(3.0)
        self.assertEqual(
            request.call_args.args[:2],
            (
                "GET",
                "https://api.semanticscholar.org/graph/v1/paper/search/bulk",
            ),
        )
        self.assertEqual(request.call_args.kwargs["params"]["query"], "causal inference")
        self.assertEqual(
            request.call_args.kwargs["params"]["fields"], "paperId,title,year"
        )

    def test_semantic_scholar_waits_two_seconds_between_requests(self):
        response = Mock(
            status_code=200,
            headers={},
            json=lambda: {"data": []},
        )
        with (
            patch("utils.scholar_utils.requests.request", return_value=response),
            patch("utils.scholar_utils.time.sleep") as sleep,
            patch(
                "utils.scholar_utils.time.monotonic",
                side_effect=[100, 100, 101, 101],
            ),
            patch("utils.scholar_utils._S2_LAST_REQUEST_AT", 0),
            patch("utils.scholar_utils._S2_BACKOFF_UNTIL", 0),
        ):
            s2_paper_search("first query")
            s2_paper_search("second query")

        sleep.assert_called_once_with(1.0)

    def test_candidate_discovery_does_not_repeat_exhausted_429_retries(self):
        agent = HybridLiteratureAgent.__new__(HybridLiteratureAgent)
        agent._safe_print = Mock()
        rate_limit = requests.HTTPError("rate limited")
        rate_limit.response = Mock(
            status_code=429,
            headers={"Retry-After": "5"},
        )
        agent._discover_candidates = Mock(side_effect=rate_limit)
        task = {"section": "Introduction", "focus": "causal inference"}

        candidates = agent._process_search_task_google(task, {}, "2026-11")

        self.assertEqual(candidates, [])
        agent._discover_candidates.assert_called_once_with(task, {}, "2026-11")

    def test_semantic_scholar_batches_paper_details_in_groups_of_500(self):
        response = Mock(
            status_code=200,
            headers={},
            json=lambda: [{"paperId": "paper-1", "title": "Causal inference"}],
        )
        paper_ids = [f"paper-{index}" for index in range(501)]
        with (
            patch("utils.scholar_utils.requests.request", return_value=response) as request,
            patch("utils.scholar_utils.time.sleep"),
        ):
            papers = s2_paper_batch(paper_ids)

        self.assertEqual(request.call_count, 2)
        self.assertEqual(len(request.call_args_list[0].kwargs["json"]["ids"]), 500)
        self.assertEqual(request.call_args_list[1].kwargs["json"]["ids"], ["paper-500"])
        self.assertIn("paper-1", papers)
        self.assertEqual(
            request.call_args_list[0].args[1],
            "https://api.semanticscholar.org/graph/v1/paper/batch",
        )
        self.assertIn("abstract", request.call_args_list[0].kwargs["params"]["fields"])

    def test_batch_details_are_used_without_per_candidate_search(self):
        agent = HybridLiteratureAgent.__new__(HybridLiteratureAgent)
        agent.registry_lock = threading.Lock()
        agent._safe_print = Mock()
        agent._process_search_task_google = Mock(
            return_value=[
                {
                    "paper_id": "paper-1",
                    "title": "Causal inference",
                    "year": 2024,
                    "reason": "bulk search",
                }
            ]
        )
        paper = {
            "paperId": "paper-1",
            "title": "Causal inference",
            "authors": [{"name": "Ada Lovelace"}],
            "venue": "Journal",
            "year": 2024,
            "abstract": "A study of causal inference.",
        }
        registry = {}
        task = {"section": "Introduction", "focus": "causal inference"}

        with (
            patch(
                "methods.agents.literature_review_agent.s2_paper_batch",
                return_value={"paper-1": paper},
            ) as batch,
            patch(
                "methods.agents.literature_review_agent.s2_title_search"
            ) as title_search,
        ):
            agent._execute_tasks_in_parallel(
                [task], {}, registry, set(), "2025-01"
            )

        batch.assert_called_once_with(["paper-1"])
        title_search.assert_not_called()
        self.assertEqual(next(iter(registry.values())).title, "Causal inference")


if __name__ == "__main__":
    unittest.main()
