# Capability Loop · 能力成长闭环 (v0.2)

[English](README.md) | **简体中文**

Capability Loop 是一个面向 AI 协作场景的 Agent Skill，处理一个具体问题：项目已经交付，个人能力是否真正增长仍缺少证据。

> 交付证据不等于能力证据。

一份完成度很高的成果，可以证明工作已经交付。它无法单独证明用户能够复现其中的判断、适应新的条件，或在较少帮助下处理相邻问题。Capability Loop 将两类证据分开记录，并保留足够的信息，供用户检查能力判断是否过度。

## 范围

Capability Loop 借鉴项目式学习、刻意练习、反思与迁移评估。它聚焦于 AI 协作项目中的轻量能力证据闭环。

完整的教育 PBL 还包括持续探究、学习者选择、批评与修订、公开成果、教学引导和评估设计。这些内容不属于当前 Skill 的承诺范围。

## 三种模式

- `start`：保留原始交付目标，定义一项边界明确的目标能力，并选择下一项刻意挑战。
- `checkpoint`：检查一次真实尝试，分开记录交付证据与能力证据，并比较本次与上次使用的帮助。
- `transfer`：在一个相邻新问题上测试同一项能力，并明确记录上下文泄漏情况。

日常对话默认保持自然。只有在用户主动要求、发起 checkpoint review、要求导出，或 AI 准备提出能力状态变化时，Skill 才展示完整证据账本。

## 能力状态

每个状态都绑定一项明确能力、一个任务族和当前已有证据。

- `emerging`：目标行为已经出现过一次有效实例。
- `repeatable`：目标行为在相似任务中再次出现，AI 或其他帮助没有变得更具替代性。
- `transfer-evidenced`：用户在 `clean` 迁移条件下，对相邻新问题提交了有效的独立首稿。

这些状态用于汇总证据，不构成证书，也不能外推为通用熟练度。一次失败会增加能力债务，并可能缩小能力声明的适用范围。它不会自动抹去此前有效的低阶证据。

## 援助与迁移控制

证据账本会记录帮助介入尝试的时间：

- 用户首次尝试之前；
- 尝试过程中；
- 首次尝试完成后的批评阶段；
- 工具执行或外部反馈阶段。

如果 AI 在用户首次尝试前已经提供目标行为，这部分内容不能算作用户的独立能力证据。

迁移隔离分为四级：

- `clean`：使用新的相邻问题，旧答案不可见，首次尝试前没有提示，并保留用户首稿；
- `partial`：部分旧结构、案例或材料仍然可见；
- `contaminated`：首次尝试前已经提供答案、模板、推理模式或分步辅导；
- `unknown`：无法确认隔离条件。

只有 `clean` 迁移可以支持 `transfer-evidenced`。

## 安装

将仓库中的 `capability-loop/` 目录复制或链接到兼容 Agent Skills 的宿主。

示例提示词：

- `使用 $capability-loop，围绕这个项目启动一次能力成长闭环。`
- `使用 $capability-loop 做一次 checkpoint，保持自然对话。`
- `在提出状态变化前，先展示证据账本。`
- `为这项能力设计一次 clean transfer 测试。`

核心 Skill 不依赖 CLI、MCP server、数据库、固定文件路径、网络或外部账号。

## 持久化与可选协作工具

默认状态边界是宿主当前可用的对话上下文。跨会话持久化需要用户明确授权，并由用户指定保存位置或状态系统。Skill 不得暗示存在隐藏存储，也不得覆盖项目事实源。

[FlowGrid](https://github.com/dlxeva/FlowGrid) 可以作为持久、可审计的跨会话判断状态工具。它始终是可选项，不会被自动安装或调用。

## 仓库内容

- [`capability-loop/SKILL.md`](capability-loop/SKILL.md)：可安装的 Skill 指令。
- [`capability-loop/references/evidence-ledger.md`](capability-loop/references/evidence-ledger.md)：证据和状态转换语义。
- [`capability-loop/references/multi-round-example.md`](capability-loop/references/multi-round-example.md)：虚构的完整多轮示例。
- [`capability-loop/references/behavioral-tests.md`](capability-loop/references/behavioral-tests.md)：便于人工阅读的行为回归说明。
- [`capability-loop/references/evaluation-protocol.md`](capability-loop/references/evaluation-protocol.md)：可复现的宿主与模型评测流程。
- [`evals/cases.json`](evals/cases.json)：版本化、机器可读的行为用例。
- [`scripts/validate_repo.py`](scripts/validate_repo.py)：零依赖仓库校验脚本。

## 校验

运行本地校验：

```bash
python scripts/validate_repo.py
```

使用官方 Agent Skills reference implementation 校验 Skill：

```bash
python -m pip install \
  'git+https://github.com/agentskills/agentskills.git@217be548739f21d6008915c29aefe320ea1a90af#subdirectory=skills-ref'
skills-ref validate ./capability-loop
```

GitHub Actions 会在每个 PR 和每次向 `main` 推送时运行两项检查。

## 当前评测状态

- 结构与仓库检查已经自动化。
- 行为回归用例已经写入 `evals/cases.json` 并纳入版本控制。
- 示例文件只描述预期行为，不能作为真实场景证据。
- 跨宿主结果、真实用户纵向数据、跨会话持久化测试和 clean transfer 现场研究仍待完成。

公开评测结果时，应使用精确表述，例如：在 commit Z 上，使用 host X 与 model Y 完成测试。更广泛的验证结论需要对应的公开证据。

## 从 v0.1 迁移

v0.2 将可安装目录和 Skill 标识从 `pbl-loop` 改为 `capability-loop`。旧安装需要替换原目录，并改用 `$capability-loop` 调用。

仓库名称继续保留 `pbl-loop`。
