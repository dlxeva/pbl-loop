# Capability Loop · 能力成长闭环 (v0.2)

Capability Loop is a host-neutral Agent Skill for one specific problem in AI-assisted work:

> Delivery evidence is not capability evidence.

A polished output can prove that work shipped. It does not prove that the person can repeat the reasoning, adapt it, or perform it on an adjacent problem with less help. Capability Loop keeps those claims separate and records enough evidence to challenge overconfidence.

## Scope

Capability Loop draws from project-based learning, deliberate practice, reflection, and transfer assessment. Its scope is deliberately narrower than a complete educational PBL system. A full PBL implementation also needs sustained inquiry, learner voice and choice, critique and revision, public products, facilitation, and assessment design.

This repository packages a lightweight capability-evidence loop for real AI-assisted projects.

## Three modes

- `start`: preserve the delivery goal, define one bounded target capability, and choose one deliberate next challenge.
- `checkpoint`: inspect a real attempt, separate delivery evidence from capability evidence, and compare the assistance used.
- `transfer`: test the same capability on one adjacent problem with explicit leakage controls.

Conversation stays natural by default. The skill exposes its evidence ledger only when the user asks for it, requests a checkpoint review or export, or when the AI is about to propose a capability-state transition.

## Capability states

Every state is scoped to one named capability, one task family, and the evidence currently on record.

- `emerging`: one effective instance of the target behavior is visible.
- `repeatable`: the target behavior is visible again on a similar task, with assistance that did not become more substitutive.
- `transfer-evidenced`: the target behavior is visible on an adjacent new problem under clean transfer conditions.

These states are evidence summaries, not credentials or general mastery claims. A failed attempt adds capability debt and can narrow the claim. It does not automatically erase earlier valid evidence.

## Assistance and transfer controls

The ledger records when help entered the attempt:

- before the user's first attempt;
- during the attempt;
- after the first attempt as critique;
- through tool execution or external feedback.

AI generation that supplies the target behavior before the user's first attempt cannot count as independent capability evidence for that behavior.

Transfer isolation is recorded as:

- `clean`: fresh adjacent problem, prior answers unavailable, no pre-attempt hints, and the user's first attempt preserved;
- `partial`: some prior structure or artifacts remain visible;
- `contaminated`: an answer, template, reasoning pattern, or coaching was supplied before the first attempt;
- `unknown`: the isolation conditions cannot be established.

Only a clean transfer can support `transfer-evidenced`.

## Installation

Copy or link the repository's `capability-loop/` directory into an Agent Skills-compatible host.

Example prompts:

- `Use $capability-loop to start a capability loop around this project.`
- `Use $capability-loop for a checkpoint. Keep the conversation lightweight.`
- `Show the evidence ledger before suggesting a state change.`
- `Design a clean transfer test for this capability.`

The core requires no CLI, MCP server, database, fixed filesystem path, network access, or external account.

## Persistence and optional companions

The default operating boundary is the context currently available to the host. Cross-session persistence requires explicit user authorization and a user-selected location or state system. The skill must never imply hidden storage or overwrite project truth.

[FlowGrid](https://github.com/dlxeva/FlowGrid) can serve as an optional companion for durable, auditable judgment state. It is never installed or invoked automatically.

## Repository contents

- [`capability-loop/SKILL.md`](capability-loop/SKILL.md): installable skill instructions.
- [`capability-loop/references/evidence-ledger.md`](capability-loop/references/evidence-ledger.md): canonical evidence and transition semantics.
- [`capability-loop/references/multi-round-example.md`](capability-loop/references/multi-round-example.md): fictional end-to-end example.
- [`capability-loop/references/behavioral-tests.md`](capability-loop/references/behavioral-tests.md): human-readable regression guidance.
- [`capability-loop/references/evaluation-protocol.md`](capability-loop/references/evaluation-protocol.md): repeatable host/model evaluation procedure.
- [`evals/cases.json`](evals/cases.json): versioned machine-readable behavior cases.
- [`scripts/validate_repo.py`](scripts/validate_repo.py): dependency-free repository checks.

## Validation

Run the local checks:

```bash
python scripts/validate_repo.py
```

Validate the skill against the official Agent Skills reference implementation:

```bash
python -m pip install \
  "git+https://github.com/agentskills/agentskills.git@217be548739f21d6008915c29aefe320ea1a90af#subdirectory=skills-ref"
skills-ref validate ./capability-loop
```

GitHub Actions runs both checks on every pull request and on pushes to `main`.

## Evaluation status

- Structural and repository checks are automated.
- Behavioral regression cases are versioned in `evals/cases.json`.
- The example files describe intended behavior and do not count as field evidence.
- Published cross-host runs, real-user longitudinal results, cross-session persistence tests, and clean transfer studies are still pending.

Use precise result language such as “tested on host X with model Y at commit Z.” Reserve broader validation claims for published evidence.

## Migration from v0.1

Version 0.2 renames the installable directory and skill identifier from `pbl-loop` to `capability-loop`. Existing installations must replace the old directory and invoke `$capability-loop`.

The repository name remains `pbl-loop` for continuity.

## 中文简述

Capability Loop 面向 AI 协作中的一个具体问题：项目已经交付，个人能力是否真正增长仍缺少证据。

它通过 `start → checkpoint → transfer` 三种模式，分别记录交付目标、目标能力、真实尝试、AI 介入时点、能力证据、能力债务与迁移污染。每个能力状态都绑定具体能力和任务范围，不能外推为通用熟练度或职业认证。

v0.2 将强制表格式输出改为自然对话，并加入证据账本、援助阶段、迁移隔离等级、机器可读评测用例与 CI 校验。当前已经具备结构化测试基础，真实用户与跨宿主验证仍待开展。
