# Multi-round example

This synthetic, fictional example demonstrates intended behavior. It is not field validation. Every event described below belongs only to the illustrative scenario; never copy its goals, feedback, artifacts, or results into a real user's ledger.

## Scenario

The fictional user is preparing a community reading event. In the prompt below, the user explicitly states both the delivery goal and target capability. Do not infer either goal from the topic alone in a real conversation.

## Start

User:

> My delivery goal is to run the community reading event. Separately, I want to practise this capability: turning vague resident feedback into decisions I can test.

Assistant, naturally:

> We will keep two outcomes separate: whether the event runs, and whether you can turn an ambiguous comment into a decision with an observable test. For the first attempt, choose one real comment, write what is ambiguous, what decision it could change, and what you would observe afterward. I will critique only after your first pass. What is the closest thing you have to a resident's original wording?

The assistant does not invent a plausible resident quote. If the user has no real source statement, it may offer a clearly labelled illustrative exercise, but that exercise is not external evidence and cannot be recorded as resident feedback. The working ledger remains compact in context. No capability state is earned yet because no performance has been observed.

## Checkpoint 1

Within this fictional example, the user supplies a source-attributed real comment but asks the AI to supply the ambiguity analysis and test design. The example does not fabricate or quote the comment. The event plan improves and is used.

Natural response:

> The plan moved forward, so there is delivery evidence. For the capability goal, the useful judgment was mostly produced by AI after you selected the source comment. That gives us a worked example, not evidence that you can yet perform the full reasoning. Next time, write the ambiguity and test before asking for critique.

Ledger change:

- Delivery evidence: the event plan incorporated a feedback-driven change.
- Capability evidence: the user selected relevant source material.
- Assistance: substantial AI reasoning; no prior comparison.
- State: none assigned; the `emerging` threshold has not been met for the full target behavior.
- Capability debt: independent ambiguity analysis and test design remain unseen.

## Checkpoint 2 and transition proposal

On a similar planning decision, the user writes the ambiguity, proposed design change, and observable test before the AI responds. The AI only points out one untested assumption; the user revises it.

Before proposing a transition, expose the ledger:

> **Evidence ledger**
>
> - Delivery goal: run the community reading event.
> - Target capability: turn ambiguous resident feedback into a testable event-design judgment.
> - Current state: none assigned; `emerging` evidence is not yet complete.
> - Delivery evidence: two planning decisions were changed using resident feedback (`human` and `external_evidence`).
> - Capability evidence: on the second attempt, you independently identified the ambiguity, linked it to a decision, and proposed an observable test (`human`); AI supplied one critique after the first attempt (`ai_reasoning`).
> - Assistance change: reduced from AI-generated reasoning to post-attempt critique.
> - Capability debt: only one complete effective instance; repeatability is untested.
> - Next challenge: perform the same reasoning on another similar comment before critique.
>
> This supports a proposed transition to `emerging`, not mastery. Does this ledger accurately describe what you and the AI each did?

The user's confirmation can correct provenance, but cannot create the transition evidence. If the ledger is accurate, the state becomes `emerging` because one effective instance already exists.

## Checkpoint 3 and transition proposal

The user repeats the behavior on another feedback item. They complete the first pass independently, and the AI critique does not change the core judgment.

Expose the ledger before proposing another transition:

- Two effective instances now exist on similar planning tasks.
- Assistance was reduced on checkpoint 2 and remained similar on checkpoint 3.
- The capability evidence concerns the user's first drafts, not the polished final plan.
- Capability debt now centers on adjacent-problem transfer and context isolation.

This supports a proposed transition from `emerging` to `repeatable`, subject to factual verification of the ledger. It does not support `transfer-evidenced`.

## Contaminated transfer

The user stays in the same conversation, can see both previous analyses, and receives a reminder of the three-part pattern before attempting a new volunteer-onboarding problem. They perform well.

Natural response:

> This is useful evidence that you can reuse the pattern with the prior examples visible. It is not clean independent-transfer evidence because the current conversation contains the earlier reasoning and I reminded you of the structure. We should keep the state at `repeatable`. The remaining debt is a fresh adjacent problem under stronger isolation, with your first attempt completed before any hints.

Ledger change:

- Transfer result: effective but contaminated.
- Isolation: same session; prior examples visible; AI reminder supplied before the attempt.
- State: remains `repeatable`.
- Capability debt: clean adjacent transfer remains untested.

## Clean transfer

In a new session, the user receives only a fresh adjacent problem about interpreting ambiguous volunteer feedback. Prior answers and artifacts are unavailable. The user completes a first version before AI evaluation and independently identifies ambiguity, connects it to an operational decision, and specifies an observable test.

Before proposing the final transition, expose the ledger, including:

- the adjacent problem and why it belongs to the same capability family;
- the user's first-attempt artifact;
- the absence of pre-attempt AI hints;
- the isolation controls used;
- any external result or unresolved quality issue;
- the accumulated evidence and remaining debt.

If the evidence is accurate and effective, the AI may propose `transfer-evidenced`. The user verifies the record; neither the AI's confidence nor the user's agreement substitutes for the performance evidence.

## Missing-goal checkpoint variant

If a real checkpoint begins without an explicit delivery goal or target capability in available context, do not borrow the goals from this scenario. Keep them unknown, or say that a framing is tentative and proposed. For example:

> The delivery goal is unknown from the context I have. For this round, I am tentatively treating “turn feedback into a testable decision” as the capability under review; that is my proposed framing, not a goal you previously stated. What delivery were you trying to complete?
