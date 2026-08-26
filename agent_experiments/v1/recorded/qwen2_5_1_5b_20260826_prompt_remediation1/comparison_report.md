# Live-Agent exposed-case comparison report

The Profiler and Planner were evaluated separately. The Planner consumed the human canonical packet, not the Profiler proposal. No end-to-end execution ran.

| Case | Role | Free-form | Vocabulary-assisted | Bounded harness | Failure layers |
| --- | --- | --- | --- | --- | --- |
| xeisd | PROFILER | PASS | FAIL | FAIL | TYPED_CONTRACT, BOUNDED_HARNESS |
| hsp90 | PROFILER | PASS | FAIL | FAIL | TYPED_CONTRACT, BOUNDED_HARNESS |
| xeisd | PLANNER | PASS | FAIL | FAIL | TYPED_CONTRACT, BOUNDED_HARNESS |
| hsp90 | PLANNER | PASS | FAIL | FAIL | TYPED_CONTRACT, BOUNDED_HARNESS |

Hard gates: **FAIL**.

The three columns assess the same recorded proposal at increasing deterministic controls; they are not independent model samples and no percentage metric is reported.

Claim ceiling: this is a two-case exposed-development comparison only. It does not establish source-science validity, scientific support, Agent value, general Operator behavior, transfer, or held-out performance.
