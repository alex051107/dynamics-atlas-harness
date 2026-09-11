# Rules incremental-value experiment runtime

This experiment compares a tool-using Luna agent with the same agent given selected scientific rules, then with those rules plus one deterministic warning report. The scientific result remains unmeasured until the frozen answers are scored and compared.

The runtime preserves the existing offline Docker tools, input mounts, model, reasoning level and per-run resource limits. Its only scientific enforcement is four warnings on the first accepted submission: claim-ceiling wording, numerical occurrence in tool output, condition/window/statistical-unit wording, and public input sanity metadata. Warnings never rewrite the answer. All arms may submit one optional revision within the same budget.

`agent_run.py` takes a task root containing `cases`, `runtime`, `runs`, and `outputs`. Each case has `common` mounted at `/source` and an isolated writable `/work`; hidden rubrics and metadata are never mounted. Use the frozen Docker image named in that round's freeze manifest. Obtain the OpenRouter credential from the operating-system keychain and inject it as `OPENROUTER_API_KEY`; do not place credentials in the task workspace.

`python3 test_checks.py` checks the four warning categories and that the submitted answer is not altered. Passing it establishes implementation behavior, not scientific validity. The numerical check recognizes occurrence within 1%, not semantic provenance; the wording check can flag legitimate negative claims. These limits are predeclared in the experiment protocol.

An individual token/resource stop is preserved in its receipt. A saved accepted answer remains available for evaluation; no answer is invented when submission is missing. The orchestration resumes only unattempted positions in the frozen order. Unknown charges, cost limits and infrastructure errors stop the campaign.
