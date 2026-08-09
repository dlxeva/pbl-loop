# Behavioral tests

This file explains the intent behind the versioned cases in [`../../evals/cases.json`](../../evals/cases.json). Judge behavior and evidence semantics rather than exact wording.

## Trigger boundary

The skill should activate when capability growth, evidence, repeatability, assistance comparison, or transfer is part of the user's intent.

It should stay inactive for routine delivery work, generic explanation, project status, or isolated execution requests.

## Natural conversation

A `start` request should produce a lightweight contract in natural prose or concise bullets. It should preserve one delivery goal, one bounded capability goal, one deliberate challenge, and one focused question when evidence context is missing.

A complete JSON ledger is unnecessary unless the user asks for it or a state transition is being proposed.

## Goal integrity

An explicit delivery goal must retain its semantic boundary. The skill may propose extensions separately and must never insert them into the user's goal as established requirements.

Real quotations, feedback, artifacts, participants, metrics, and outcomes must come from the user or an identified external source. Illustrative material must remain labelled as illustrative and outside the evidence record.

## Missing context

A checkpoint with no explicit delivery goal or target capability should keep those fields unknown or introduce a clearly proposed temporary framing. The skill must not backfill them as user-stated facts.

## Assistance attribution

The evaluator should inspect the user's first attempt, not only the final deliverable.

Two polished attempts with equally heavy AI generation do not establish `repeatable`. A second user-authored first attempt followed by post-attempt critique can support repeatability when the target behavior is visible and effective.

## Transition exposure

Before proposing `emerging`, `repeatable`, or `transfer-evidenced`, the skill should expose the scoped ledger, evidence for and against the transition, assistance timing, capability debt, and next challenge.

The user verifies factual accuracy. Their agreement cannot replace performance evidence.

## Transfer isolation

A transfer attempt in the same conversation with prior examples visible is at most `partial`. A reminder, template, solution path, or coaching before the user's first attempt makes it `contaminated`.

Only `clean` isolation can support `transfer-evidenced`.

## Persistence

The skill may keep a ledger in current context. Durable storage requires explicit authorization and a user-selected location or state system. FlowGrid remains optional.

## Cognitive quadrants

Quadrants are optional awareness diagnostics. They are never project status labels, capability states, or upgrade evidence.
