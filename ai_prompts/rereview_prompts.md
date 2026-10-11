# Targeted blind re-review prompts (risk line and metric line)

English translations of the two Chinese prompts used for the blind re-reviews of records that the first round had excluded as E3/E4/E5 (353 records for the risk line, 537 for the metric line; 10 October 2026). Each record was judged by three AI reviewers who did not see the first-round decision. The eligibility criteria (Table S3) were read first (`<local-path>`).

## Risk line

This run re-checks the boundary of the risk line, using the following reading (a clarification of criterion 6, not a change to the criteria):
- After "human brain tumour + MRI + automatic segmentation/detection" is satisfied, if the paper makes **uncertainty estimation, confidence/calibration, segmentation-quality prediction, quality control, failure detection or conformal prediction** one of its main contributions, or evaluates it, **include (risk line)**. The evaluation unit need not be named in the abstract: a voxel-wise uncertainty map is the "voxel" unit and counts as stating the unit.
- Uncertainty mentioned only in passing (an adjective, future work, a limitation), or an internal module unrelated to the results → **exclude E4** (if only global voxel metrics are reported).
- Uncertainty is clearly a component of the method in the abstract (e.g. "uncertainty-guided refinement/semi-supervision") but it cannot be seen whether it is evaluated separately → **unclear**.
- Judge the metric line at the same time: lesion-level results in the abstract (lesion-wise, detection rate, false positives per case, size stratification, analysis of misses) → include (metric line).
- Otherwise apply E1–E9. For records without an abstract, judge from the title only; if in doubt, unclear.

Output a TSV, no header, 4 columns: id; decision (Include/Exclude/Unclear); code (exclusions: E1–E9; inclusions: metric, risk or both; unclear: empty); reason (one sentence, ≤40 characters, no tab or line break). Validate the line count and the one-to-one match of ids with `python3 -I`. Do not ask questions; when finished reply with one sentence (the numbers of the three decisions).

## Metric line

This run re-checks the boundary of the metric line:
- After "human brain tumour + MRI + automatic segmentation/detection" is satisfied, if the abstract reports **lesion-level results** — lesion-wise metrics, lesion/metastasis detection sensitivity or detection rate, false-positive lesions per case/scan, FROC, results stratified by lesion size or number, explicit analysis of missed lesions, instance-level segmentation metrics — **include (metric)**.
- "Detection" used only as a descriptor (e.g. "tumour detection" that is really whole-image classification of tumour present or absent), or only Dice/HD95/accuracy-type global metrics → exclude (classification E3; global voxel metrics E4; generic or non-brain-tumour E5).
- 2D object-detection boxes (YOLO, mAP, recall): if it is tumour detection on brain tumour MRI and reports detection recall/precision/mAP, write **unclear** with the note "box detection".
- Suspected lesion-level results in the abstract but uncertain → unclear. Without an abstract, judge from the title; if in doubt, unclear.
- Judge the risk line at the same time: uncertainty/calibration/quality control/failure detection as a main contribution or evaluated (voxel level also counts) → include (risk).
- Otherwise apply E1–E9.

Output format and closing instructions as for the risk line.
