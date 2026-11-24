# Question-formulation robustness experiment

This directory contains release-ready data from the question-formulation robustness analysis accompanying **When Does a Story Become Gendered? A Trajectory-Based Analysis of Masculinity-Related Bias in Free-Text Generation**.

## Objective

The original MRNI-BB attribution questions sometimes ask the judge to infer a general norm endorsement from a character's situated behaviour. We replace these with scenario-specific questions referring directly to the behaviour, and compare the resulting judgments on the *same generated story prefixes*. No new story continuations are generated for this test.

## Files

- `sampled_stories_and_questions.tsv`: 120 sampled trajectories (20 per generator), their original and proposed behavioural questions, base scenarios, generated texts, and sampling metadata. The `question_review_status` column is retained from the working data; all 120 rows are marked `needs review` and should not be mistaken for independent human approval of the question paraphrases.
- `behavioral_question_judgments.tsv`: one row per story prefix and judge for the scenario-specific behavioural question (1,608 checkpoints x 3 judges = 4,824 rows). These are **completed final** responses from Llama-3.3-70B-Instruct, Qwen2.5-72B-Instruct, and DeepSeek-V3.2, excluding an earlier incomplete Qwen run. `judge_raw_output` is the returned answer token/alias; `judge_predicted_answer` is its decoded category. Full prompts and token accounting are not included in this compact release.
- `evaluated_story_prefixes.tsv`: exact 1,608 cumulative story prefixes supplied to the behavioural-question judges, with corresponding questions.
- `checkpoint_comparison.tsv`: checkpoint-level original vs behavioural judgments, majority labels and each judge's classifications. Missing original judgments remain blank.
- `story_comparison.tsv`: first-commitment direction/timing and final-checkpoint comparison for each of the 120 stories.
- `summary.md`: numerical findings and denominator definitions.
- `verify_summary.py`: standard-library Python script verifying the key counts from the comparison tables.

## IDs and labels

`sample_id` uniquely identifies a sampled trajectory. `instance_id` in the sample and behavioral judgments refers to the original generator instance. `original_instance_id` in the story comparison is the same identifier. `timepoint_number` identifies the cumulative sentence-prefix checkpoint. The labels are `the man`, `the woman`, `insufficient information` (and, where applicable, `no_majority`). For first-commitment outcomes, `unresolved` means no committed checkpoint was identified. Boolean fields in the comparison files use the literal strings `True` and `False`.

## Missing data and interpretation

The behavioural-question run contains 1,608 complete checkpoints for each of the three judges. The available original-question results match 1,605 checkpoints. Original judgments are unavailable for QROB_064 at t=30, QROB_069 at t=25, and QROB_074 at t=25. For comparisons of complete original vs behavioural majority labels, exclude these three checkpoints. The sample was intentionally balanced on **original** first-commitment gender (60 man, 60 woman), so it should not be used to estimate population-level gender attribution rates.

This package includes the experimental data and derived comparison results from the existing analysis. In particular, it does **not** establish that all proposed behavioural questions have undergone an independent manual semantic review.
