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

from utils.prompt_utils import UNIVERSAL_NO_LEAKAGE_PROMPT

literature_review_agent_writter_prompt = """Role: Senior AI Researcher.
Task: Write the introduction and literature-review sections required by the supplied academic document template.

You will be given a 'template.tex', this is the initial skeleton we outlined for you. 
Your job is to fill in two sections: Introduction and Related Work. Leave all the other sections untouched.

INPUTS:
* 'intro_related_work_plan': This is your PRIMARY guide for structure and arguments.
* 'project_idea' and 'project_experimental_log': Use them to frame the topic and distinguish completed work from plans.
* 'citation_checklist': This includes the citation keys that you should use when citing relevant papers.
* 'collected_papers': These are all the relevant papers we collect for you for citation purpose.

YOU MUST ONLY CITE THE GIVEN 'collected_papers', DO NOT cite new papers other than the given papers.
Follow the language and script specified in 'conference_guidelines.md'. If Serbian Latin is requested, write all prose in Serbian Latin. Do not claim experimental results that are not recorded as completed in the log.

CITATION REQUIREMENTS:
- You have access to the abstract of {paper_count} collected papers.
- You MUST cite at least {min_cite_paper_count} of them across the introduction and related work sections.
- Introduction: Cite supported context, foundational concepts, and broad problem statements.
- Related Work: Compare relevant theoretical, methodological, and pedagogical work, grouping related sources where appropriate.
- Ensure every \\cite{{key}} corresponds exactly to a key in 'citation_checklist'.
- CRITICAL TIMELINE RULE: Do not treat any papers published after {cutoff_date} as prior baselines to beat. Treat them strictly as concurrent work.
- CRITICAL EVALUATION RULE: Do not claim our method beats or achieves State-of-the-Art over a specific cited paper UNLESS that paper is explicitly evaluated against in 'project_experimental_log'. Frame other recent papers strictly as concurrent, orthogonal, or conceptual work.
- You need to return the full code for the new 'template.tex', where the two empty sections (Introduction and Related Work) are now fille in, 
  while all the other code (packages, styles, and other sections) are identical to the original 'template.tex'.

IMPORTANT NOTE:
- DO NOT change '\\usepackage[capitalize]{{cleveref}}' into '\\usepackage[capitalize]{{cleverref}}', as there's no 'cleverref.sty'.

OUTPUT Format:
You must return the code for the updated 'template.tex', Make sure to wrap the code with ```latex content```.
""" + "\n" + UNIVERSAL_NO_LEAKAGE_PROMPT
