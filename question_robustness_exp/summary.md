# Results: robustness to question formulation

The experiment evaluates **120 stratified original trajectories**, 20 per generator, with original first-commitment direction balanced (60 man, 60 woman). The same three LLM judges evaluated cumulative sentence prefixes using scenario-specific questions directly referring to the target behaviour.

| Quantity | Result |
|---|---:|
| Sampled trajectories | 120 |
| Behavioural-question checkpoints judged by all three models | 1,608 |
| Checkpoints with available original-question judgments | 1,605 |
| Identical majority label at matched checkpoints | 1,499 / 1,605 (93.40%) |
| Same attribution direction when both checkpoint labels are committed | 941 / 948 (99.26%) |
| Same first-commitment direction among stories committed under both formulations | 115 / 117 (98.29%) |
| Same first-commitment checkpoint among stories committed under both formulations | 96 / 117 (82.05%) |
| Behavioural formulation first commitment earlier / later | 11 / 10 stories |
| Originally committed stories unresolved with the behavioural formulation | 3 |
| First-commitment direction different | 2 |
| Identical final evaluated label | 107 / 120 (89.17%) |

The five changed first-commitment outcomes comprise two opposite first directions (the trajectories subsequently converge in direction) and three trajectories in which the behavioural formulation yielded no definite commitment. Agreement in **direction** is higher than agreement in **timing**, consistent with the paper's conclusions.

**Denominators:** 1,608 = all sampled checkpoints under the behavioural formulation; 1,605 = those with original-question judgments; 948 = checkpoints where both question formulations yield either man or woman; 117 = stories committed under both formulations. These summaries describe this balanced sample, not a population estimate.

**Provenance note:** Values reproduce the existing comparison results and were checked against the accompanying TSV files. This package is not a new analysis. Three original-question checkpoints could not be matched (see README).
