# Dynamics Atlas

**What can simulations and experiments jointly tell us about protein dynamics?**

We aim to produce useful, checkable scientific answers from heterogeneous protein data. Reliable quantities and cross-source comparisons are the scientific goals; reusable workflows and AI assistance are means to those goals.

## For Soojung and the research group

**[Read the findings and decisions brief](collaborators/README.md).** It explains the original goal, what each stage actually tested, the current results, and four questions on which we need scientific guidance.

The brief links the [author-claim / project-result comparisons](collaborators/docs/RESULTS.md) and the existing English slides. No installation or code review is needed to understand the discussion.

**Current stage:** the selected-case analyses and the component pilot are complete. Some guidance helped on one case but not another. The pilot did not establish that a rule-centered system is necessary or that more rules would solve the remaining failures. The next scientific milestone and the role of automated rule selection remain decisions, not completed work.

## Optional technical material

[Methods and boundaries](collaborators/docs/METHODS.md) · [Numerical reproduction](collaborators/docs/REPRODUCE.md) · [Primary sources](collaborators/docs/SOURCES.md)

The reproduction package starts from supplied analysed tables. It does not rebuild raw coordinates or independently validate the biological interpretations.

<details>
<summary>For maintainers: code, frozen evidence and earlier work</summary>

`src/`, `tests/` and `agent_experiments/` contain implementation work. [Research records](research/README.md) retain prior plans, reviews, failed runs and frozen evidence. They are supporting records, not the reading path for the group.

This documentation branch is based on `feature/luna-runtime-v1` at `c025a74ed8235ddde463572158c73458753780b0`. It changes presentation and interpretation notes only. It does not change scientific inputs, scores, experiment outputs or `main`, and it does not authorize further runs.

</details>
