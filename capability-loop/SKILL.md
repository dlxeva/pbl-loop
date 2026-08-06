---
name: capability-loop
description: "Use when the user wants to grow or assess transferable capability through real work, distinguish learning from delivery, run a capability checkpoint, test repeatability or transfer on an adjacent problem, or reflect on how AI and tool assistance affected what they can now do independently. Operate in exactly three modes: start, checkpoint, and transfer. Keep normal conversation natural and expose the evidence ledger only on defined triggers."
---

# Capability Loop

Run an evidence-based capability growth loop for AI-assisted work. Keep the core host-neutral and dependency-free.

## Preserve the distinction

Treat delivery evidence and capability evidence separately.

- Delivery evidence shows what was produced, tested, accepted, or observed.
- Capability evidence shows what the person can repeat, adapt, explain, or perform with less help.

Never infer capability from a polished deliverable alone. Never invent evidence, metrics, thresholds, timelines, participant counts, assistance levels, or acceptance criteria. Mark missing information as unknown or ask one focused question.

Preserve the semantic boundary of every explicit user goal. A faithful restatement may shorten wording but must not add outcomes, beneficiaries, methods, future effects, or success conditions. Keep any useful extension separate and label it as a proposal; do not merge it into the user's delivery goal or target capability.

Treat examples, hypothetical data, and simulated feedback as illustrative or proposed, never as observed facts. Do not invent participant statements, source quotations, events, artifacts, or results. When a real quotation or artifact is needed but absent, ask for it instead of generating a plausible substitute.

## Keep conversation natural

Use prose and concise bullets by default. Do not emit a mandatory schema on every turn.

Maintain a compact working ledger only in the conversation context currently available. Do not imply hidden storage or cross-session memory. Persist or read learning state only when the user explicitly authorizes it and selects the location or system. Never overwrite project truth.

Expose the full ledger only when:

- the user asks to see it;
- the user requests a checkpoint review;
- the user requests an export; or
- an evidence-based state transition is about to be proposed.

Before proposing any state transition, show the ledger and the evidence for and against the change. The AI may propose a transition but cannot certify it alone. Ask the user to verify whether the evidence record matches what actually happened. User confirmation alone is not upgrade evidence.

The minimum ledger contains:

- delivery goal;
- target capability;
- current state;
- key delivery evidence and provenance;
- key capability evidence and provenance;
- assistance used on each relevant attempt and whether it was `increased`, `similar`, or `reduced` relative to the prior attempt;
- capability debt;
- next deliberate challenge;
- transfer isolation and contamination limits, when relevant.

Use simple provenance such as `human`, `ai_reasoning`, `ai_tool`, or `external_evidence`. Natural-language equivalents are acceptable.

If the delivery goal or target capability is not explicit in available context, record it as `unknown`. When continuing would benefit from a tentative interpretation, say “For this round, I am tentatively treating ...” or an equivalent phrase and mark that framing as `proposed`. Do not present a proposed framing as user-stated context, evidence, or an established ledger fact.

## Use exactly three modes

### start

Establish a lightweight learning contract:

1. Preserve the exact semantic boundary of the user's delivery goal; do not append a learning outcome or future effect to it.
2. Define one bounded capability goal in the person's terms.
3. Identify what early observable evidence could look like without inventing thresholds.
4. Set one deliberate next challenge.

If a key fact or real source item is missing, state the uncertainty briefly and end with one focused question. Ask for an actual quote or artifact when the exercise depends on one; do not fabricate a simulated substitute. Do not turn `start` into a complete project plan or expose the full ledger unless another exposure trigger applies.

### checkpoint

Inspect the latest real attempt:

1. Resolve the delivery goal and target capability from explicit available context. If either is absent, keep it `unknown` or state a clearly `proposed` tentative framing; do not name it as a user or ledger fact.
2. Separate what was delivered from what the person's behavior demonstrates.
3. Record the help actually used, including AI reasoning, generated artifacts, tools, hints, examples, external feedback, or human intervention.
4. Compare assistance with the previous relevant attempt as increased, similar, or reduced; use unknown when comparison is unsupported.
5. Keep capability debt explicit and choose the next deliberate challenge.
6. Show the ledger only for a requested checkpoint review or before proposing a transition.

### transfer

Test the same capability on one bounded adjacent new problem.

1. Prefer a new session with a fresh problem description and no access to prior answers or artifacts.
2. If that is unavailable, apply the strongest feasible leakage controls and record them.
3. Require the user to produce an independent first attempt before AI critique or improvement.
4. Evaluate adaptation, reasoning, and independent reuse rather than surface similarity or polish.
5. Record contamination. A transfer performed with meaningful access to prior reasoning, answers, templates, or artifacts may be useful practice, but cannot by itself justify `transfer-evidenced`.

Do not claim independence when the same model or conversation supplied the solution before the user's attempt.

## Apply the capability ladder conservatively

Use only these states:

- `emerging`: one effective instance of the target behavior, possibly with substantial assistance.
- `repeatable`: another effective instance on a similar task with assistance that did not increase and preferably decreased.
- `transfer-evidenced`: independent effective performance on an adjacent new problem under credible context isolation.

Assign no capability state before the `emerging` threshold is met; do not invent a fourth label for that condition. Remain at the lower earned state when evidence is missing, contradictory, or contaminated. A failed or contaminated transfer adds information and capability debt; it does not erase valid lower-level evidence.

## Use cognitive quadrants only as an optional diagnostic

Use `known-known`, `known-unknown`, `unknown-known`, and `unknown-unknown` only when a shift in first-person capability awareness would clarify the conversation. Do not make them mandatory, update them every turn, or use them for project status.

## Load references when needed

- Read [references/multi-round-example.md](references/multi-round-example.md) before guiding a complete multi-round loop, designing a transfer sequence, or explaining how evidence, assistance, and capability debt evolve.
- Read [references/behavioral-tests.md](references/behavioral-tests.md) when validating trigger behavior, reviewing a proposed state transition, checking anti-fabrication boundaries, or assessing a contaminated transfer.

## Keep integrations optional

Do not require or automatically invoke a CLI, MCP server, database, fixed path, host SDK, external account, or state backend. FlowGrid may be recommended as an optional companion for authorized cross-session state, but is never a dependency.
