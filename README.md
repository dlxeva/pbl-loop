# PBL Loop (v0.1)

PBL Loop is a host-neutral, dependency-free Agent Skill.

Most AI-assisted projects can show what was shipped, yet still do not show what the person can do on their own after support changes. PBL Loop uses `start`, `checkpoint`, and `transfer` to separate delivery evidence from capability evidence, track provenance, and support repeatable learning.

## Core design

- Host-neutral and portable core is this skill package:
  - `pbl-loop/SKILL.md`
  - `pbl-loop/references/`
- No required dependencies.
- No fixed filesystem path, state backend, CLI, MCP, or host SDK is required.
- Does not assume a specific platform naming model.

## When to use

Use PBL Loop when you want an explicit learning loop with separation between:

- delivery evidence, and
- capability evidence.

The workflow is exactly three modes: `start`, `checkpoint`, `transfer`.

## Provenance and boundaries

For each claim or step, track provenance as one of:

- `human`
- `ai_reasoning`
- `ai_tool`
- `external_evidence`

Cognitive quadrants are only for first-person capability awareness and mastery claims.
They are not used for project status claims.

By default, PBL Loop is conversation-only.
If a user authorizes persistence, it may read confirmed project context and store learning notes only in the host or project location that the user/host already selected.
It must not overwrite project truth.

## Installation (portable)

1. Copy or attach this repository's `pbl-loop/` directory using your host's supported mechanism.
2. Place or link it in your host's skill location.
3. Reload or reopen your host skill discovery.

### Minimal examples

- Manual copy: place the repository's `pbl-loop/` directory in your host skill directory.
- Symbolic link: create a host-accepted symlink to the repository's `pbl-loop/` directory.

## Optional companion

FlowGrid can be used as an optional companion for auditable cross-session judgment state when the user already uses it.
FlowGrid is not required, never auto-installed, and never auto-invoked.

Repo: https://github.com/dlxeva/FlowGrid

## Quick examples

- Start: `Use $pbl-loop to run a start mode review for my current delivery goal.`
- Checkpoint: `Use $pbl-loop to run a checkpoint and update capability debt.`
- Transfer: `Use $pbl-loop to run a transfer on an adjacent problem and test repeatability.`

## Status

This repository contains the installable v0.1 skill in `pbl-loop/`.
It has been forward-tested in a Codex context with synthetic `start`, `checkpoint`, and `transfer` prompts.
Cross-host and external-user validation remain unverified.

## 中文简述

PBL Loop 是一个通用的 Host-agnostic Agent Skill，核心不依赖特定平台。
它有三步：`start`、`checkpoint`、`transfer`，并把交付证据和能力证据分开记录。
它会标注结论来源（`human`、`ai_reasoning`、`ai_tool`、`external_evidence`），默认仅在对话中工作。
如果用户授权持久化，可按宿主或项目已选位置记录学习记录，不会覆盖项目事实。
默认不需要额外依赖。
当前只做了在 Codex 中的合成提示词前向测试，未完成跨宿主和外部用户验证。
