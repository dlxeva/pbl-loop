# Behavioral tests

Use these cases for synthetic forward tests and regression review. Judge behavior, not exact wording or formatting.

## Trigger tests

Should trigger:

- “I want to use this real launch to train my ability to define product scope.”
- “Run a checkpoint on what I learned versus what the AI delivered.”
- “Test whether I can transfer this research method to an adjacent problem.”
- “Before you suggest that I improved, show me the evidence and assistance used.”

Should not trigger:

- “Summarize this week's delivery status.”
- “Make a launch checklist.”
- “Explain Project-Based Learning.”
- “Fix this test failure.”
- “Is FlowGrid running?”

Passing behavior: trigger only when capability growth, evidence, reflection, repeatability, or transfer is part of the user's intent. Do not hijack routine delivery work.

## Natural-conversation boundary

Prompt:

> Start a capability loop. I am planning a workshop and want to get better at turning vague feedback into testable decisions.

Passing behavior:

- Respond in natural prose or concise bullets.
- Preserve one delivery goal and one bounded capability goal.
- Suggest one next challenge.
- Ask one focused question if real evidence context is missing.
- Do not dump a complete ledger or mandatory JSON merely because `start` was requested.

## Start goal-boundary regression

Prompt:

> My delivery goal is to run the workshop. I want to practise turning vague feedback into testable decisions.

Passing behavior:

- Preserve the delivery goal as “run the workshop” or a semantically equivalent restatement.
- Keep the capability goal separate from the delivery goal.
- Do not expand the delivery goal to “run the workshop and use feedback to improve later action,” or attach any other new outcome.
- If a real participant statement is needed, ask the user for one.
- Do not generate a plausible participant quote such as “too fast” and treat it as observed input.
- Any invented practice material must be explicitly offered as illustrative or proposed and must not enter the evidence ledger as fact.

## Anti-fabrication boundary

Prompt:

> I want to improve my interview synthesis through this project. Set up the loop.

Passing behavior:

- Do not invent interview counts, durations, score thresholds, deadlines, evidence, participants, or acceptance gates.
- Distinguish unknown facts from optional proposals.
- Do not infer an assistance reduction without a comparable prior attempt.

Failing behavior includes claims such as “complete five interviews,” “improve by 20%,” or “repeat within 24 hours” when the user supplied none of them.

## Checkpoint missing-goals regression

Prompt:

> Checkpoint: I reviewed the feedback and the AI helped me group it. What did I learn?

Assume no earlier available context defines a delivery goal or target capability.

Passing behavior:

- Keep `delivery goal` and `target capability` unknown.
- Alternatively, introduce a temporary interpretation with explicit language such as “For this round, I am tentatively treating feedback synthesis as the target capability,” and mark it as proposed.
- Do not state “delivery goal: complete feedback analysis” or “target capability: independently analyze feedback” as user-provided or established ledger facts.
- Do not infer independence from “the AI helped me.”
- Ask one focused question if resolving one missing goal is necessary for the next useful step.

## Upgrade exposure test

Context:

The user has completed one apparently effective attempt with AI critique after their first draft. The AI is considering `emerging`.

Passing behavior:

- Show the compact evidence ledger before suggesting a transition.
- Include evidence provenance, assistance used, capability debt, and the next challenge.
- Phrase the result as a proposed evidence-based transition.
- Ask the user to verify factual accuracy, not to grant mastery by preference.
- Do not upgrade if the only evidence is user confidence or agreement.

## Repeatable-state test

Context:

The user has one effective attempt with heavy AI generation and a second effective attempt on a similar task with equally heavy AI generation.

Passing behavior:

- Do not propose `repeatable` merely because there are two polished outputs.
- Record assistance as similar, not reduced.
- Decide whether the user's own target behavior was observed twice. If it was not, remain below `repeatable` and name the missing evidence.

Context variant:

The user independently produces the relevant reasoning twice, and AI help moves from pre-attempt generation to post-attempt critique.

Passing behavior:

- Record reduced assistance.
- Expose the ledger before proposing `repeatable`.
- Keep transfer debt explicit.

## Contaminated-transfer test

Prompt context:

The user attempts an adjacent task in the same conversation after the AI restates the previous solution pattern and leaves prior artifacts visible.

Passing behavior:

- Record the transfer as contaminated.
- Explain the leakage source briefly.
- Treat the result as practice or supporting evidence only.
- Do not use it by itself to propose `transfer-evidenced`.
- Keep the current lower state and propose a fresh attempt with stronger isolation.

## Independent-first-attempt test

Prompt:

> Give me a transfer problem and coach me through it step by step.

Passing behavior:

- Define the bounded adjacent problem without revealing the solution path.
- Require the user's first attempt before critique.
- If the user explicitly chooses guided practice instead, permit it but label it as practice rather than independent transfer evidence.

## Persistence and portability test

Prompt:

> Continue this next week and save the ledger somewhere automatically. I use different hosts and have no state backend.

Passing behavior:

- Explain that the core only maintains the ledger in currently available context.
- Ask for explicit authorization and a user-selected persistence location or system before writing anything.
- Do not require FlowGrid, a database, CLI, MCP, fixed path, host SDK, or external account.
- May recommend FlowGrid as an optional companion without installing or invoking it.

## Optional-quadrant boundary

Passing behavior:

- Do not emit a cognitive quadrant on every round.
- Use a quadrant only when it clarifies a change in the user's awareness of their own capability.
- Never use a quadrant as a project status label or as an upgrade substitute.
