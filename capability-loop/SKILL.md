---
name: capability-loop
description: "Use when a user wants to build or assess a transferable capability through real work, separate delivery results from learning evidence, run a capability checkpoint, compare AI assistance across attempts, or design an adjacent transfer test. Operate in start, checkpoint, or transfer mode; keep routine delivery work outside the loop."
license: MIT
compatibility: "Agent Skills-compatible hosts. No network, CLI, MCP server, database, fixed path, or external account required."
metadata:
  author: dlxeva
  version: "0.2.0"
---

# Capability Loop

Run an evidence-based capability growth loop for AI-assisted work. Keep the core host-neutral and dependency-free.

## Activate narrowly

Activate when the user explicitly wants to:

- grow or assess a capability through a real project;
- distinguish what was delivered from what they can now repeat;
- review a learning checkpoint;
- compare assistance across attempts;
- test repeatability or transfer on an adjacent problem.

Stay inactive for routine delivery planning, project status, generic explanations, isolated bug fixes, or completion checks with no capability-learning intent.

Use exactly three modes: `start`, `checkpoint`, and `transfer`.

## Preserve truth and scope

Treat delivery evidence and capability evidence separately.

- Delivery evidence shows what was produced, tested, accepted, or observed.
- Capability evidence shows what the person can repeat, adapt, explain, or perform with less substitutive help.

Never infer capability from a polished deliverable alone. Never invent evidence, metrics, thresholds, timelines, participant counts, assistance levels, acceptance criteria, quotations, events, artifacts, or results.

Preserve the semantic boundary of every explicit user goal. A faithful restatement may shorten wording but must not add outcomes, beneficiaries, methods, future effects, or success conditions. Keep extensions separate and label them as proposals.

Scope every capability claim to:

- one bounded capability statement;
- one task family or context;
- the attempts and evidence currently on record;
- any known limitations or contamination.

Do not generalize a scoped state into broad mastery, certification, employability, or independent competence outside the recorded task family.

## Keep conversation natural

Use prose and concise bullets by default. Do not emit a mandatory schema on every turn.

Maintain a compact working ledger only in the context currently available. Do not imply hidden storage or cross-session memory. Persist or read learning state only when the user explicitly authorizes it and selects the location or system. Never overwrite project truth.

Expose the full ledger only when:

- the user asks to see it;
- the user requests a checkpoint review;
- the user requests an export; or
- an evidence-based state transition is about to be proposed.

Before proposing a state transition, show the evidence for and against it. Ask the user to verify factual accuracy and provenance. User agreement can correct the record; agreement alone cannot create upgrade evidence.

Read [references/evidence-ledger.md](references/evidence-ledger.md) whenever constructing, exporting, or reviewing a ledger or state transition.

## Record assistance at the attempt level

For each relevant attempt, record:

- whether a user first attempt exists;
- what target behavior is visible in that first attempt;
- the assistance source;
- when assistance entered: `pre_attempt`, `during_attempt`, `post_attempt`, `tool_execution`, `external_feedback`, `none`, or `unknown`;
- whether the assistance supplied the target behavior: `yes`, `no`, or `unknown`;
- whether assistance became `increased`, `similar`, `reduced`, or `unknown` relative to the prior comparable attempt.

AI generation, templates, reasoning patterns, or step-by-step coaching supplied before the user's first attempt cannot count as independent capability evidence for the behavior they supplied.

Similar assistance can still support `repeatable` only when the user's own target behavior is visible in both attempts and the assistance did not become more substitutive. Two polished AI-led outputs do not establish repeatability.

## Apply the capability ladder conservatively

Use only these earned states:

- `emerging`: one effective instance of the target behavior is visible, with assistance and provenance disclosed.
- `repeatable`: another effective instance is visible on a similar task, and assistance did not become more substitutive.
- `transfer-evidenced`: an effective first attempt is visible on an adjacent new problem under `clean` transfer isolation.

Before `emerging`, record that no state has been earned; do not invent another capability label.

Remain at the lower earned state when evidence is missing, contradictory, or contaminated. A failed or contaminated attempt adds information and capability debt. Revisit an earlier state only when new evidence materially undermines the original record.

## Grade transfer isolation explicitly

Record transfer isolation as:

- `clean`: fresh adjacent problem, prior answers and artifacts unavailable, no pre-attempt hints, and the user's first attempt preserved;
- `partial`: some prior structure, examples, or artifacts remain visible without directly supplying the new answer;
- `contaminated`: an answer, template, solution pattern, or coaching was supplied before the first attempt;
- `unknown`: the isolation conditions cannot be established.

Only `clean` transfer can support `transfer-evidenced`. `partial`, `contaminated`, and `unknown` attempts may support practice or lower-level evidence and must retain their limitation.

Do not claim independence when the same model or conversation supplied the target reasoning before the user's attempt.

## Mode: start

Establish a lightweight learning contract:

1. Preserve the user's delivery goal. Keep it `unknown` when absent.
2. Define one bounded capability goal in the person's terms. Mark tentative framing as `proposed`.
3. Identify observable evidence without inventing thresholds.
4. Choose one deliberate next challenge that makes the user's behavior visible.
5. Ask one focused question when a missing fact blocks the next useful step.

Do not turn `start` into a complete project plan or expose the full ledger unless another exposure trigger applies.

## Mode: checkpoint

Inspect the latest real attempt:

1. Resolve the delivery goal and target capability from explicit context.
2. Separate delivery evidence from the behavior visible in the user's attempt.
3. Record the assistance phase, source, and substitutive effect.
4. Compare assistance with the prior comparable attempt when evidence supports comparison.
5. Update capability debt and choose the next deliberate challenge.
6. Show the ledger for a requested checkpoint review or before proposing a transition.

If no user first attempt or artifact is available, say what cannot be assessed. Do not infer independence from the final output.

## Mode: transfer

Test the same capability on one bounded adjacent new problem:

1. Define why the new problem belongs to the same capability family.
2. Prefer a fresh session or equivalent context isolation.
3. Withhold solution patterns, templates, and hints until the user's first attempt is complete.
4. Preserve or request the first-attempt artifact before critique.
5. Evaluate adaptation, reasoning, and independent reuse.
6. Record isolation level and contamination sources.
7. Keep the lower state when isolation is not `clean`.

If the user chooses guided practice, proceed and label it as practice rather than independent transfer evidence.

## Use cognitive quadrants only as an optional diagnostic

Use `known-known`, `known-unknown`, `unknown-known`, and `unknown-unknown` only when a shift in first-person capability awareness clarifies the conversation. Do not make them mandatory, update them every turn, use them for project status, or substitute them for evidence states.

## Load references when needed

- Read [references/evidence-ledger.md](references/evidence-ledger.md) for evidence records and transition semantics.
- Read [references/multi-round-example.md](references/multi-round-example.md) before guiding a complete multi-round loop.
- Read [references/behavioral-tests.md](references/behavioral-tests.md) when reviewing trigger boundaries or regression behavior.
- Read [references/evaluation-protocol.md](references/evaluation-protocol.md) when running or reporting evaluations.

## Keep integrations optional

Do not require or automatically invoke a CLI, MCP server, database, fixed path, host SDK, external account, or state backend. FlowGrid may be recommended for authorized cross-session state and remains optional.
