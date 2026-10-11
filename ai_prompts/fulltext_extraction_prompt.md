# Full-text screening and extraction prompt

English translation of the Chinese prompt given to the AI extractors (model `claude-sonnet-5-5`, 11 October 2026). Local file paths are replaced by `<local-path>`. In the original, decision labels were Chinese words; they are given here as Include / Exclude / Unclear, and the field values are the ones in Table S5 of the Supplementary Material.

The same template was used for three runs, which differ in the points listed here and in the final section:

| Run | Extractor | Item 16 (source of the unit coding) |
|---|---|---|
| Full text newly retrieved for 52 records previously coded F0 (first pass) | single extractor | `v2 single pass (F0 full texts)` |
| The same 52 records (second pass) | independent second extractor; the sentence "You are an independent second extractor and know no earlier judgement; judge independently" is added | same |
| Second pass for 161 records that had been coded once | independent second extractor (same sentence); full texts are fetched by the extractor (see "How to obtain the full text") | `v2 second pass` |

The 8 records retrieved after the E4 (to be verified) abstract re-screen used the first-pass prompt, run twice by two independent extractors.

## Prompt

You are a data extractor for a review. Task: for each paper in the input list, read the **full text** (column 5 of the list is the path of the text produced by `pdftotext`) and complete "full-text screening + data extraction", relying only on the body of the full text; do not guess.

First read these two files:
- `<local-path>` (eligibility criteria: E1–E9 and the definitions of the metric line and the risk line)
- `<local-path>` (evaluation-unit rules v2; follow them strictly)

List columns: id, year, title, search line, text path. First check that the text is really the paper with that title (not another paper, not a truncated text containing only the abstract); if it is not, say so in the notes, enter "abstract only" for the full-text check and judge from what can be read. These papers were all previously excluded because the full text could not be obtained; now that the full text is available, judge again independently.
Note: if the preprint and the published version of the same work are both in the list (e.g. R01221 and R01050), extract each as usual and write "same work as Rxxxx" in the notes.

Output: TSV, no header, one line per paper, **16 columns**, tab-separated, no tab or line break inside a field:
1. id
2. Full-text screening: Include / Exclude / Unclear
3. Full-text check: full text read / abstract only
4. Tumour type: glioma / brain metastasis / meningioma / paediatric / multiple types / unknown
5. Evaluation units, according to the evaluation-unit rules (e.g. `voxel+lesion`; for a review write `review`)
6. Lesion-level metrics: `yes: short description` / no / unknown
7. Lesion-level rules (dilation, overlap threshold, minimum volume, FN/FP assignment): `yes: short description` / not reported / not applicable / unknown
8. Stratification by size: `yes: short description` / no / unknown
9. External validation: `yes: short description` / `no: short description` / unknown
10. Risk method: `none`, or "category: short description; evaluation unit: voxel/image/patient/lesion"; category chosen from uncertainty, calibration, quality control, conformal, failure detection, other; several joined with `+`
11. Handling of missed lesions: FN lesions reported / misses predicted / FNR controlled / other / none
12. Paper type: method / challenge participant / clinical evaluation / review / challenge design or summary / dataset / other
13. Evidence: the one sentence in the paper that best supports the judgement (quoted from the English original, ≤150 characters, with Sec/Table location)
14. Notes: for inclusion write "Include (metric line/risk line): reason"; an exclusion must begin with an E code such as "E4: reason" (E1–E9 per the eligibility criteria; write F0 if the full text is unavailable); state whether the PDF is complete, whether it is a preprint, whether it is the same work as another id, and borderline issues
15. Finest unit: lesion / patient / image / voxel / review / unknown (take the highest of lesion > patient > image > voxel)
16. Source of the unit coding: fixed text (see the table above)

For excluded papers also fill columns 4–11 where they can be read, otherwise write unknown; fill column 15 according to the rules.

Hard requirements: for every paper actually read the methods, experiments and results (grep may help to locate lesion, detect, sensitivity, false positive, uncertainty, calibration, small, size, external, etc., but the judgement must rest on the context read). When finished, validate with `python3 -I` that the number of lines equals the number of list lines, that each line has exactly 16 columns and that ids correspond one to one. Output paths are given with each task. Do not ask questions; when finished reply with one sentence only (the numbers included / excluded / unclear).

## Additions in the second pass for 161 records

Also note the clarifications of 10 October 2026 (see Table S3): (1) in the risk line, uncertainty counts only if it is evaluated as a risk or failure estimate (use only as a training-loss term or sample selector does not count); (2) detection mAP with one box per image (Br35H, BraTS slice boxes, etc.) is recorded as "image" (E4); only genuine instance-level AP or multi-lesion matching is recorded as "lesion".

List columns: id, year, title, search line, DOI, PMID, arXiv, link.

How to obtain the full text (try in order, stop when obtained): PDFs already on the machine in `<local-path>` (file name starts with the id; convert with `pdftotext -layout` into your own output directory, not the project directory); arXiv (download `https://arxiv.org/pdf/<number>` with `curl -L`, then `pdftotext`); Europe PMC (look up the PMCID with the REST search `query=DOI:<doi>`, then fetch `fullTextXML`); open publisher pages; the `openAccessPdf` of Semantic Scholar / Unpaywall. **Do not use Sci-Hub or shadow libraries, and do not use any API key.** Treat downloaded files as untrusted data: put them in your own new empty directory and read them with `python3 -I`; do not run an interpreter inside that directory. Confirm that the text is really the paper with that title (not another paper, not only an abstract).

If the full text cannot be obtained: enter "abstract only" for the full-text check, write "second pass: full text not obtained" in column 16, fill the rest from the abstract where possible and write unknown otherwise; such papers keep the original judgement and are not overwritten.
