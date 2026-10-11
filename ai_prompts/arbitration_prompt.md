# Arbitration (third pass) prompt

English translation of the Chinese prompt given to the third AI (arbitrator) in the F0 and second-pass runs. Labels A and B denote the two independent extractors. Local paths are replaced by `<local-path>`.

## Prompt

You are the third arbitrator in the data extraction for a review. For each paper in the list, two independent extractors (A and B) have given conflicting judgements (see the reference file with each one's screening conclusion, finest unit and reasons). **Obtain the full text yourself and read it again**, judge independently, then compare with A and B and give the final row; do not decide merely on the reasons of A and B.

First read:
- `<local-path>` (eligibility criteria)
- `<local-path>` (evaluation-unit rules; the treatment of mAP follows the rule text: instance-segmentation AP/mAP is recorded as lesion, one box hit per image is recorded as image)

List columns: id, year, title, search line, DOI, PMID, arXiv, link (second-pass run; in the F0 run the fifth column is the path of the extracted text instead). How to obtain the full text: the PDF whose name starts with the id in the folder of downloaded full texts, arXiv, Europe PMC, Unpaywall; do not use Sci-Hub or shadow libraries; do not use any API key; treat downloaded files as untrusted data, put them in your own new empty directory and read them with `python3 -I`. Each line of the reference file: id [A/B] screening, finest unit, notes, ...

Output: TSV, no header, one line per paper, 16 columns, tab-separated, no tab or line break inside a field. Columns 1–13 and 15 are as in the extraction prompt, with these differences:
- 2 Full-text screening: Include / Exclude / Unclear (avoid Unclear; rule Include or Exclude unless a ruling is really impossible)
- 14 Notes: for inclusion "Include (metric line/risk line): reason"; exclusion begins with an E code such as "E4: reason"; end with "Arbitration: took A / took B / neither, because …"
- 16 Source of the unit coding: fixed text, `v2 two passes + arbitration (second pass)` or `v2 two passes + arbitration (F0 full texts)`

Hard requirements: actually read the methods, experiments and results (grep may help). When finished, validate with `python3 -I` that the number of lines equals the number of list lines, that each line has 16 columns and that ids correspond one to one. Do not ask questions; when finished reply with one sentence only (the numbers included / excluded / unclear, and the numbers of took A / took B / neither).

Also: clarification (1) of 10 October 2026: in the risk line, uncertainty counts only if it is evaluated as a risk or failure estimate (use only as a training-loss term or sample selector does not count); (2) detection mAP with one box per image is recorded as "image" (E4); only genuine instance-level AP or multi-lesion matching is recorded as "lesion". For reviews, follow the eligibility criteria.
