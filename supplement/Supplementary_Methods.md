# Electronic Supplementary Material

**Lesion-level miss measurement and risk estimation in brain tumour MRI segmentation: a scoping review**

Contents: Supplementary Methods (search strategies, AI use, evaluation-unit rules); Table S1 (agreement between AI passes); Table S2 (AI against human raters); Table S3 (eligibility criteria and change log); Table S4 (evaluation-unit rules); Table S5 (extraction table, file `S5_extraction_table.tsv`); Table S6 (full-text-stage exclusions, file `S6_full_text_exclusions.tsv`); Table S7 (check of extracted fields, file `S7_spot_check.tsv`); Table S8 (citation-tracking re-run for one seed, file `S8_citation_tracking_rerun.tsv`); PRISMA-ScR checklist.

---

## Supplementary Methods

### 1. Search strategies

Search dates: PubMed, OpenAlex, arXiv and Europe PMC, 9 October 2026; Web of Science Core Collection and Scopus, 10 October 2026. Publication years 2015 to the search date; no language restriction at search. Brain tumour term sets, concept blocks and databases:

| Block | Concept | Databases |
|---|---|---|
| A2 | Lesion-level measurement and misses | PubMed, OpenAlex, arXiv, Web of Science, Scopus |
| A3 | Lesion sensitivity and false positives per patient/scan | PubMed, OpenAlex, arXiv, Web of Science, Scopus |
| B2 | Risk estimation (uncertainty, quality control, failure detection) | PubMed, OpenAlex, arXiv, Web of Science, Scopus |
| C | BraTS challenge line | PubMed, OpenAlex, arXiv, Web of Science, Scopus |

Blocks A2 and B2 omit an MRI term, because abstracts of lesion-level or risk-estimation papers often do not name the modality.

#### 1.1 PubMed (E-utilities; field [tiab]; publication date 2015/01/01 to 2026/10/09)

Tumour: `(brain neoplasms[MeSH Terms] OR glioma*[tiab] OR glioblastoma*[tiab] OR meningioma*[tiab] OR "brain tumor*"[tiab] OR "brain tumour*"[tiab] OR "brain metasta*"[tiab] OR "intracranial tumor*"[tiab])`

Task: `(segmentation[tiab] OR detection[tiab])`

- A2: tumour AND task AND `("lesion-wise"[tiab] OR "lesion wise"[tiab] OR "lesion-level"[tiab] OR "per-lesion"[tiab] OR "instance-level"[tiab] OR "missed lesion*"[tiab] OR "false negative lesion*"[tiab] OR "small lesion*"[tiab] OR "detection rate"[tiab] OR "lesion detection"[tiab])`
- B2: tumour AND task AND `(uncertainty[tiab] OR "failure detection"[tiab] OR "quality control"[tiab] OR "selective prediction"[tiab] OR conformal[tiab] OR calibration[tiab] OR "quality assessment"[tiab] OR "error detection"[tiab] OR "quality estimation"[tiab])`
- A3: tumour AND task AND `("lesion sensitivity"[tiab] OR "lesion-wise sensitivity"[tiab] OR "per-lesion sensitivity"[tiab] OR "false positives per patient"[tiab] OR "false positives per scan"[tiab] OR "number of false positives"[tiab] OR "false positive lesions"[tiab])`
- C: `(BraTS[tiab] OR "brain tumor segmentation challenge"[tiab]) AND (segmentation[tiab] OR challenge[tiab] OR benchmark[tiab])`

#### 1.2 OpenAlex (API filter `title_and_abstract.search`; `from_publication_date:2015-01-01`, `to_publication_date:2026-10-09`)

Tumour: `("brain tumor" OR "brain tumors" OR "brain tumour" OR "brain tumours" OR glioma OR gliomas OR glioblastoma OR meningioma OR meningiomas OR "brain metastases" OR "brain metastasis" OR "intracranial tumor")`

Task: `(segmentation OR detection)`

- A2: tumour AND task AND `("lesion-wise" OR "lesion wise" OR "lesion-level" OR "per-lesion" OR "instance-level" OR "missed lesion" OR "missed lesions" OR "false negative lesions" OR "small lesion" OR "small lesions" OR "detection rate" OR "lesion detection")`
- B2: tumour AND task AND `(uncertainty OR "failure detection" OR "quality control" OR "selective prediction" OR conformal OR calibration OR "quality assessment" OR "error detection" OR "quality estimation")`
- A3: tumour AND task AND `("lesion sensitivity" OR "lesion-wise sensitivity" OR "per-lesion sensitivity" OR "false positives per patient" OR "false positives per scan" OR "number of false positives" OR "false positive lesions")`
- C: `(BraTS OR "brain tumor segmentation challenge" OR "brain tumour segmentation challenge") AND (segmentation OR challenge OR benchmark)`

#### 1.3 arXiv (API; categories cs.CV, eess.IV, cs.LG, stat.ML; abstract field)

Tumour: `(abs:"brain tumor" OR abs:"brain tumour" OR abs:glioma OR abs:glioblastoma OR abs:meningioma OR abs:"brain metastases" OR abs:"brain metastasis" OR abs:BraTS OR ti:"brain tumor")`

Task: `(abs:segmentation OR abs:detection)`

- A2: tumour AND task AND `(abs:"lesion-wise" OR abs:"lesion wise" OR abs:"lesion-level" OR abs:"per-lesion" OR abs:"instance-level" OR abs:"missed lesion" OR abs:"missed lesions" OR abs:"false negative lesions" OR abs:"small lesions" OR abs:"detection rate" OR abs:"lesion detection")`
- B2: tumour AND task AND `(abs:uncertainty OR abs:"failure detection" OR abs:"quality control" OR abs:"selective prediction" OR abs:conformal OR abs:calibration OR abs:"quality assessment" OR abs:"error detection" OR abs:"quality estimation")`
- A3: tumour AND task AND `(abs:"lesion sensitivity" OR abs:"lesion-wise sensitivity" OR abs:"per-lesion sensitivity" OR abs:"false positives per patient" OR abs:"false positives per scan" OR abs:"number of false positives" OR abs:"false positive lesions")`
- C: `((abs:BraTS OR abs:"brain tumor segmentation challenge") AND (abs:segmentation OR abs:challenge OR abs:benchmark))`

#### 1.4 Europe PMC (REST API; fields TITLE_ABS; first publication date 2015-01-01 to 2026-10-09)

Tumour: `TITLE_ABS:("brain tumor" OR "brain tumors" OR "brain tumour" OR "brain tumours" OR glioma OR glioblastoma OR meningioma OR "brain metastases" OR "brain metastasis" OR "intracranial tumor")`

Task: `TITLE_ABS:(segmentation OR detection)`

- A2: tumour AND task AND `TITLE_ABS:("lesion-wise" OR "lesion wise" OR "lesion-level" OR "per-lesion" OR "instance-level" OR "missed lesion" OR "missed lesions" OR "false negative lesions" OR "small lesions" OR "detection rate" OR "lesion detection")`
- B2: tumour AND task AND `TITLE_ABS:(uncertainty OR "failure detection" OR "quality control" OR "selective prediction" OR conformal OR calibration OR "quality assessment" OR "error detection" OR "quality estimation")`
- A3: tumour AND task AND `TITLE_ABS:("lesion sensitivity" OR "lesion-wise sensitivity" OR "per-lesion sensitivity" OR "false positives per patient" OR "false positives per scan" OR "number of false positives" OR "false positive lesions")`
- C: `TITLE_ABS:(BraTS OR "brain tumor segmentation challenge") AND TITLE_ABS:(segmentation OR challenge OR benchmark)`

#### 1.5 Web of Science Core Collection (field Topic, TS; publication years 2015–2026)

- A2: `TS=(("brain tumor*" OR "brain tumour*" OR glioma* OR glioblastoma* OR meningioma* OR "brain metasta*" OR "intracranial tumor*") AND (segmentation OR detection) AND ("lesion-wise" OR "lesion wise" OR "lesion-level" OR "per-lesion" OR "instance-level" OR "missed lesion*" OR "false negative lesion*" OR "small lesion*" OR "detection rate" OR "lesion detection"))`
- B2: `TS=(("brain tumor*" OR "brain tumour*" OR glioma* OR glioblastoma* OR meningioma* OR "brain metasta*" OR "intracranial tumor*") AND (segmentation OR detection) AND (uncertainty OR "failure detection" OR "quality control" OR "selective prediction" OR conformal OR calibration OR "quality assessment" OR "error detection" OR "quality estimation"))`
- A3: `TS=(("brain tumor*" OR "brain tumour*" OR glioma* OR glioblastoma* OR meningioma* OR "brain metasta*" OR "intracranial tumor*") AND (segmentation OR detection) AND ("lesion sensitivity" OR "lesion-wise sensitivity" OR "per-lesion sensitivity" OR "false positives per patient" OR "false positives per scan" OR "number of false positives" OR "false positive lesions"))`
- C: `TS=((BraTS OR "brain tumor segmentation challenge" OR "brain tumour segmentation challenge") AND (segmentation OR challenge OR benchmark))`

#### 1.6 Scopus (field TITLE-ABS-KEY; 2015–2026)

- A2: `TITLE-ABS-KEY(("brain tumor*" OR "brain tumour*" OR glioma* OR glioblastoma* OR meningioma* OR "brain metasta*" OR "intracranial tumor*") AND (segmentation OR detection) AND ("lesion-wise" OR "lesion wise" OR "lesion-level" OR "per-lesion" OR "instance-level" OR "missed lesion*" OR "false negative lesion*" OR "small lesion*" OR "detection rate" OR "lesion detection")) AND PUBYEAR > 2014 AND PUBYEAR < 2027`
- B2: `TITLE-ABS-KEY(("brain tumor*" OR "brain tumour*" OR glioma* OR glioblastoma* OR meningioma* OR "brain metasta*" OR "intracranial tumor*") AND (segmentation OR detection) AND (uncertainty OR "failure detection" OR "quality control" OR "selective prediction" OR conformal OR calibration OR "quality assessment" OR "error detection" OR "quality estimation")) AND PUBYEAR > 2014 AND PUBYEAR < 2027`
- A3: `TITLE-ABS-KEY(("brain tumor*" OR "brain tumour*" OR glioma* OR glioblastoma* OR meningioma* OR "brain metasta*" OR "intracranial tumor*") AND (segmentation OR detection) AND ("lesion sensitivity" OR "lesion-wise sensitivity" OR "per-lesion sensitivity" OR "false positives per patient" OR "false positives per scan" OR "number of false positives" OR "false positive lesions")) AND PUBYEAR > 2014 AND PUBYEAR < 2027`
- C: `TITLE-ABS-KEY((BraTS OR "brain tumor segmentation challenge" OR "brain tumour segmentation challenge") AND (segmentation OR challenge OR benchmark)) AND PUBYEAR > 2014 AND PUBYEAR < 2027`

#### 1.7 Records retrieved per block

Web of Science: A2 354, A3 28, B2 493, C 2244 (3119 records; 2952 after removing duplicates across blocks). Scopus: A2 606, A3 44, B2 1150, C 3172 (4972 records; 4664 after de-duplication across blocks). PubMed, OpenAlex, arXiv and Europe PMC together yielded 8202 records (5190 after de-duplication). The table gives the unique records attributed to each source and block (a record can be retrieved by several sources and blocks):

| Source | A2 | A3 | B2 | C |
|---|---|---|---|---|
| PubMed | 251 | 12 | 248 | 606 |
| OpenAlex | 665 | 47 | 877 | 3813 |
| arXiv | 49 | 4 | 118 | 560 |
| Europe PMC | 216 | 13 | 234 | 64 |

De-duplication used the DOI first and the normalised title second. Records were merged in the order: PubMed/OpenAlex/arXiv/Europe PMC (5190), citation tracking (406 new), Web of Science (417 new), Scopus (940 new), giving 6953 unique records.

#### 1.8 Citation tracking

Forward and backward citations of eight core papers (the two Wang 2024 meta-analyses; Wang 2025 on meningioma; Ozkara 2023; BraTS-METS 2023; BraTS-PEDs 2023; Molchanova 2023 and 2025) were retrieved from the Semantic Scholar Graph API: 559 unique papers, of which 112 were already in the first-round results and 406 (2015 or later, or year missing) were new. The Molchanova 2023 seed was re-run separately with its correct arXiv identifier (20 references, 12 citing papers); of these, 8 records dated 2015 or later were not in the pool, and none met the inclusion criteria (one multiple sclerosis reference record, seven excluded). These 8 records are listed in `S8_citation_tracking_rerun.tsv` (Table S8) and are not part of the counts in Fig. 1.

#### 1.9 Random-sample line

Sampling frame: PubMed, `("brain tumor*" OR "brain tumour*" OR glioma* OR glioblastoma* OR meningioma* OR "brain metasta*")[tiab] AND segmentation[tiab] AND ("deep learning" OR "neural network*" OR "machine learning" OR "U-Net" OR convolutional)[tiab]`, 2015-01-01 to 2026-10-09, English, journal articles; 1544 records. One hundred records were drawn without replacement with random seed 20261011. Open-access full text (Europe PMC) was available for 63; the other 37 were classified from the abstract.

### 2. Use of AI in screening and extraction

All AI steps were carried out by Claude Sonnet 5.5 (model identifier `claude-sonnet-5-5`, Anthropic), run through Claude Code, between 9 and 11 October 2026. No other language model was used. Roles:

| Step | Agents | Input | Output |
|---|---|---|---|
| Title/abstract screening | AI agents, batches of records | title, abstract, frozen criteria (Table S3) | include / exclude (code) / unclear |
| Re-check of title/abstract decisions | independent agent, blind to the first agent's reasoning | same | decision; the re-check prevailed in disagreements |
| Targeted blind re-reviews (353 risk-line and 537 metric-line records) | three independent agents per record | title, abstract | decision by majority |
| Re-screening of E4-on-title-only records | AI agent | title and abstract where available | include / exclude |
| Full-text eligibility and data extraction | two independent agents, a third agent to arbitrate | full text (or abstract) and the 14-field form | fields in Table S5; arbitration of disagreements |

Prompts, forms and agent outputs are provided in the public repository (see Data availability). The human contribution was the labelling of a stratified sample of 100 title/abstract records by two raters and the check of extracted fields described in the main text (Table S7).

### 3. Evaluation-unit rules

See Table S4.

---

## Table S1. Agreement between AI passes

| Comparison | Records | Agreement |
|---|---|---|
| Title/abstract: first round, re-check of a sample | 52 | 44 (85%) |
| Title/abstract: Web of Science, re-check of a sample | 50 | 47 (94%) |
| Title/abstract: Scopus, re-check of a sample | 54 | 36 (67%) |
| Blind re-review of 60 randomly chosen title-level voxel-only (E4) exclusions | 60 | 60 (100%) stayed excluded |
| Evaluation unit, two independent codings (papers read in full) | 198 | 171 (86%) |
| Finest evaluation unit, two independent codings | 198 | 184 (93%) |
| Full-text eligibility, late batch (papers with full text retrieved after first classification as F0) | 52 | 26 (50%) |
| Finest unit, same late batch | 52 | 34 (65%) |
| Full-text eligibility and finest unit, second pass for papers originally coded once | 161 | 110 (68%) |

Disagreements in the evaluation-unit and full-text passes were resolved by a third agent. All comparisons are between AI passes.

## Table S2. AI decision against the two human raters (100 title/abstract records)

Cells give include / unclear / exclude as labelled by the rater.

| AI decision (n) | Rater A | Rater O |
|---|---|---|
| Include (30) | 20 / 6 / 4 | 24 / 4 / 2 |
| Unclear (10) | 2 / 6 / 2 | 2 / 8 / 0 |
| Exclude (60) | 3 / 4 / 53 | 2 / 17 / 41 |

Cohen's κ: AI–A 0.62, AI–O 0.57, A–O 0.65. Stratification of the sample: 30 AI-include, 10 AI-unclear, 35 random AI-exclude (codes E1–E6), 20 AI-exclude coded E4 or E3 with relevant terms in the abstract, 5 AI-exclude coded E4 on the title only.

## Table S3. Eligibility criteria and change log

Population–Concept–Context: human brain tumours (glioma, meningioma, brain metastasis, paediatric tumours) on MRI, automatic segmentation or detection; concept (i) lesion-level measurement and reporting of misses, (ii) risk estimation for segmentation quality or failure, classified by evaluation unit; context: method development, challenges, external validation, distribution shift.

**Inclusion** (all of 1–4, and 5 or 6): (1) human brain tumour, primary or metastatic, adult or paediatric; (2) MRI as the main input; (3) automatic segmentation or detection; (4) journal paper, conference paper, or preprint/open-access journal; (5) metric line: lesion-level results (lesion-wise metrics, lesion sensitivity or detection rate, false-positive lesion counts), results stratified by lesion size or number, or explicit analysis of missed lesions; (6) risk line: a method for estimating segmentation quality or failure (uncertainty, quality control, failure detection, calibration, conformal prediction) with a stated evaluation unit.

**Exclusion codes** (the first matching code is recorded): E1 not a brain tumour (multiple sclerosis, stroke and others; lesion-level uncertainty work on non-brain diseases was recorded as reference material and not analysed); E2 not MRI; E3 classification, grading, molecular or survival prediction only; E4 brain tumour segmentation with only overall voxel-level metrics, no lesion-level result and no risk estimation (counted); E5 general method, no brain tumour focus; E6 image synthesis, reconstruction, registration or pre-processing; E7 conference abstract, poster, thesis, erratum or no full text; E8 not in English; E9 duplicate publication; F0 full text not retrievable.

Special handling: challenge design and summary papers were included; challenge participant papers only when they reported lesion-level results or discussed misses. Reviews were included if they addressed either concept.

| Date | Change | Reason |
|---|---|---|
| 9 Oct 2026 | Criteria v1 fixed. Time range 2015-01-01 to search date; preprints included; reference class for lesion-level uncertainty in other diseases. | — |
| 9 Oct 2026 | Search extended: MRI term dropped (A2, B2); challenge line (block C); citation-tracking line; random-sample line. | Pilot searches showed that challenge, paediatric and similar papers have no lesion-level or risk terms in the abstract. |
| 9 Oct 2026 | Block A3 added (lesion sensitivity and false positives per patient/scan). | Detection papers on brain metastases report these terms rather than "lesion-wise". |
| 10 Oct 2026 | Clarification 1: a voxel-level uncertainty map is itself the voxel evaluation unit; papers in which uncertainty, calibration or quality control is a main contribution or is evaluated belong to the risk line and are not excluded as voxel-only. | Inconsistent handling of voxel-level uncertainty in the first round. |
| 10 Oct 2026 | Clarification 2: uncertainty merely mentioned, or used only as a training term or sample selector and not evaluated, remains excluded (E4). | As above. |
| 10 Oct 2026 | Clarification 3: reviews, toolkits and challenge summaries are judged by content, not excluded by article type; conference abstracts without results remain E7. | As above. |
| 10 Oct 2026 | Blind re-reviews of records first excluded as E3/E4/E5: 353 with uncertainty/calibration/quality-control/failure-detection terms; 537 with lesion-wise, per-lesion, detection-rate, false-positives-per-scan, FROC or instance-segmentation terms. | Symmetric check of both concept lines. |
| 10–11 Oct 2026 | Records excluded on title alone as voxel-only (E4) re-screened with abstracts where obtainable (1988 on 10 Oct; 605 on 11 Oct). | Title-only decisions. |

## Table S4. Evaluation-unit rules

Applied to the metrics for which a paper reports results (tables, figures, results text), not to the method's inputs and outputs or the paper's motivation.

| Unit | Definition (object on which the metric is computed) | Counts | Does not count |
|---|---|---|---|
| Voxel | Metric computed on mask voxels or pixels | Dice, IoU, HD95, ASSD, voxel-level sensitivity/specificity, volume error, volume correlation (volumes derived from masks); Dice averaged per patient remains voxel | — |
| Image | One decision per slice or image | Slice- or image-level classification accuracy, slice-level detection, per-image box detection hit | One decision per patient or case (patient) |
| Patient | One decision per patient or case | Patient-level detection (at least one lesion found), case-level quality-control pass/fail, case-level failure-detection AUC | Per-lesion counts within a patient (lesion) |
| Lesion | Prediction and reference are first split into lesion instances (connected components or boxes), then matched and counted | Lesion-wise Dice/sensitivity/F1, number of lesions detected, false-positive lesions per patient, detection rate by lesion size, instance-segmentation AP/mAP, lesion-level uncertainty or confidence | Lesion number used only as a patient attribute without instance matching |

Output per paper: (1) all units with a result metric, in the order voxel + image + patient + lesion; (2) the finest unit, taken as the highest of lesion > patient > image > voxel. Only a finest unit of "lesion" counts as lesion-level reporting. Reviews without results of their own are coded "review". Challenge and dataset design papers are coded by their official evaluation metrics (for example, lesion-wise Dice in BraTS 2023 onwards). When neither the abstract nor an available full text is clear, the unit is coded "unknown". The evaluation unit of a risk method is the unit at which the risk score or uncertainty is evaluated or used.

## Table S5. Extraction table of the 330 included papers

File `S5_extraction_table.tsv`.

## Table S6. Full-text-stage records excluded (n = 171, including 35 without retrievable full text, code F0) and unresolved (n = 2)

File `S6_full_text_exclusions.tsv`.

## Table S7. Human spot-check of extracted fields

File `S7_spot_check.tsv`: 38 primary studies, one row each, with the AI-coded finest unit, coding route, source available to the checker and the verdict (correct, incorrect, uncertain) for eligibility and seven extracted fields. Column notes are given in the main text (Methods, Human rating and spot-check).

## Table S8. Records from the citation-tracking re-run for the Molchanova 2023 seed (n = 8)

File `S8_citation_tracking_rerun.tsv`.

## PRISMA-ScR checklist

File `PRISMA-ScR_checklist.md`.
