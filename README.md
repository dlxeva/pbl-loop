# Capability Loop · 能力成长闭环 (v0.2)

Inspired by Project-Based Learning, deliberate practice, and transfer assessment — but designed for the specific failure mode of AI-assisted work: **high delivery, low transferable capability**.

Capability Loop is not a complete educational PBL system. It does not provide teachers, peer review, portfolios, curricula, or institutional assessment. It adapts one useful idea from Project-Based Learning—learning through real work—and adds a lightweight evidence loop for AI-assisted practice.

> Delivery evidence is not capability evidence.

Shipping a polished result with AI support does not prove that a person can repeat the work, adapt it, or perform it independently on an adjacent problem. Capability Loop keeps that distinction visible without turning every conversation into a form.

## What it does

Capability Loop is a host-neutral, dependency-free Agent Skill with three modes:

- `start`: establish one delivery goal, one bounded capability goal, and an observable next challenge.
- `checkpoint`: inspect what happened, distinguish delivery from capability evidence, and compare the assistance used with the previous attempt.
- `transfer`: test the capability on an adjacent new problem with meaningful context isolation.

Conversation is natural by default. The skill maintains only a compact working ledger in the context currently available to the host. It shows the full ledger only when the user requests it, asks for a checkpoint review or export, or before the AI proposes a capability-state transition.

The three capability states are:

- `emerging`: one effective instance, possibly with substantial help.
- `repeatable`: another effective instance on a similar task with no increase in help, preferably less.
- `transfer-evidenced`: independent performance on an adjacent new problem under credible isolation.

The AI may propose an evidence-based transition, but cannot certify it alone. User confirmation verifies whether the record is accurate; confirmation by itself is not upgrade evidence.

## Installation

Copy or link the repository's `capability-loop/` directory into any host that supports Agent Skills or equivalent instruction packages. No CLI, MCP server, database, fixed filesystem path, account, or host SDK is required.

Example prompts:

- `Use $capability-loop to start a capability loop around this real project.`
- `Use $capability-loop for a checkpoint. Keep the conversation lightweight.`
- `Use $capability-loop to design a transfer test for this capability.`
- `Show me the evidence ledger before suggesting an upgrade.`

## Persistence and optional companions

Capability Loop works in the current conversation context by default. Cross-session persistence is optional and must be explicitly authorized by the user. The skill must use only a location or state system the user has selected and must not overwrite project truth.

[FlowGrid](https://github.com/dlxeva/FlowGrid) can be used as an optional companion for durable, auditable cross-session judgment state. It is not a dependency and is never installed or invoked automatically.

## Included references

- [`capability-loop/references/multi-round-example.md`](capability-loop/references/multi-round-example.md): a complete `start → checkpoint → checkpoint → transfer` example, including a contaminated transfer that does not earn an upgrade.
- [`capability-loop/references/behavioral-tests.md`](capability-loop/references/behavioral-tests.md): trigger, boundary, anti-fabrication, upgrade, and contaminated-transfer test cases.

## Status

Capability Loop v0.2 has completed independent synthetic forward tests in Codex. The tested behaviors cover a natural `start`, refusing to promote two AI-completed attempts to `repeatable`, refusing to promote a contaminated transfer, and the corrected goal-boundary regressions. Cross-host behavior, real-user multi-round use, cross-session persistence, and transfer under real isolation conditions remain unvalidated. The included example documents intended behavior; it is not evidence that the method has worked in the field.

## 中文简述

能力成长闭环（Capability Loop）受项目式学习、刻意练习和迁移评估启发，针对 AI 协作中交付很多、真正可迁移到个人身上的能力很少这个问题。

它不是一套完整的教育 PBL 体系，也不假装替代教师、同伴互评或长期档案。它只保留一个轻量闭环：在真实工作中区分交付证据与能力证据，观察 AI 和工具提供了多少帮助，并用相邻新问题检验能力能否复现和迁移。

默认对话保持自然；完整证据账本只在用户要求、checkpoint review、导出或准备提出状态升级时展示。FlowGrid 只是可选的跨会话状态伙伴，不是依赖。
