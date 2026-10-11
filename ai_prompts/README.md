# AI prompts

The screening and extraction passes were run with `claude-sonnet-5-5` (see Supplementary Methods, section 2, and Table S1). The prompts were written and run in Chinese. The files here are English translations of those prompts; they are not the literal text that was run. Local file paths are replaced by `<local-path>`. In the original runs the decision labels and field values were Chinese words; the English equivalents used in Table S5 are given in the prompts.

| File | Run | Records |
|---|---|---|
| `fulltext_extraction_prompt.md` | Full-text screening and extraction: first pass for 52 records whose full text was retrieved later, independent second pass for the same 52 and for 161 records coded only once, and two independent passes for 8 records from the E4 (to be verified) abstract re-screen | 52 + 161 + 8 |
| `arbitration_prompt.md` | Third-pass arbitration of disagreements between the two extractors | 28 + 2 (F0 run); 50 (second-pass run) |
| `rereview_prompts.md` | Blind re-review of records excluded in the first round as E3/E4/E5: risk line and metric line | 353; 537 |

Agreement between passes is reported in Table S1; outcomes are in Tables S5 and S6. The intermediate output files of the runs and the utility scripts (merging, comparison, DOI check, open-access search) are not published; they contain Chinese working notes, and their results are incorporated in Tables S5 and S6.
