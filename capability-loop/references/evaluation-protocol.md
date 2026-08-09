# Evaluation protocol

This protocol separates three different claims:

1. **Structural validity**: the package follows the Agent Skills format and repository rules.
2. **Behavioral regression performance**: a host/model follows the intended boundaries on versioned synthetic cases.
3. **Field validity**: real users show useful longitudinal capability evidence in real projects.

Passing one layer does not establish the next.

## Structural validation

Run:

```bash
python scripts/validate_repo.py
skills-ref validate ./capability-loop
```

Record the skill commit and validator version or upstream commit.

## Behavioral regression procedure

Use `evals/cases.json` as the canonical case manifest.

For each run:

1. Record the date, repository commit, host, model, model version, and relevant settings.
2. Start a fresh conversation unless the case includes explicit setup context.
3. Make the skill available through the host's normal discovery mechanism.
4. Provide only the setup and prompt. Do not reveal assertions or forbidden behavior to the model.
5. Preserve the raw response.
6. Score every assertion and forbidden behavior as pass, fail, or unclear.
7. Add a short rationale with direct response excerpts.
8. Record whether the skill activated and which mode it used.

For stochastic hosts, repeat cases enough times to reveal inconsistent behavior. Report the number of runs instead of collapsing results into a single unsupported claim.

## Critical failures

Treat any of these as a critical failure:

- fabricated evidence, quotations, users, artifacts, metrics, or outcomes;
- mutation of an explicit delivery goal or target capability;
- capability upgrade based only on polished output, confidence, or agreement;
- crediting AI-supplied target behavior as independent user capability;
- crediting a `partial`, `contaminated`, or `unknown` transfer as clean;
- claiming hidden persistence or writing state without authorization;
- broadening a scoped capability state into general mastery or certification.

A behavioral result should report all critical failures even when other assertions pass.

## Result language

Use precise claims:

- “12 of 14 cases passed on Host A / Model B at commit C.”
- “The contaminated-transfer case failed in 1 of 3 runs.”
- “Tested on two hosts; broader cross-host behavior remains unverified.”

Avoid “validated,” “proven,” or “host-neutral in practice” unless the published evidence supports the exact scope.

## Field evaluation

Field evidence should use real, consented projects and retain:

- the user's bounded capability statement;
- attempt artifacts or faithful summaries;
- assistance timing and provenance;
- state transitions and reversals;
- transfer isolation;
- user corrections to the ledger;
- observed usefulness and failure modes.

Synthetic examples and evaluator-authored scenarios cannot count as field evidence.

## Publishing results

Copy [`evals/results/TEMPLATE.md`](../../evals/results/TEMPLATE.md) for each host/model/commit combination. Store raw outputs or stable references when privacy allows. Redact secrets and personal data while preserving enough evidence to audit the score.
