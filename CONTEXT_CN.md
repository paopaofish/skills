# Matt Pocock 技能库

由 Claude Code 加载的代理技能（斜杠命令和行为）集合。技能被组织到桶状文件夹中，并由 `/setup-matt-pocock-skills` 生成的每仓库配置消耗。

## 语言

**问题跟踪器（Issue tracker）**：
托管仓库问题的工具——GitHub Issues、Linear、本地 `.scratch/` markdown 约定或类似工具。像 `to-issues`、`to-prd`、`triage` 和 `qa` 这样的技能从中读取并写入。
_避免使用_：backlog manager、backlog backend、issue host

**问题（Issue）**：
**问题跟踪器**中的单个跟踪工作单元——错误、任务、PRD 或由 `to-issues` 产生的切片。
_避免使用_：ticket（仅在引用外部系统称其为 ticket 时使用）

**分类角色（Triage role）**：
在分类期间应用于 **问题** 的规范状态机标签（例如 `needs-triage`、`ready-for-afk`）。每个角色通过 `docs/agents/triage-labels.md` 映射到 **问题跟踪器** 中的实际标签字符串。

## 关系

- 一个 **问题跟踪器** 包含多个 **问题**
- 一个 **问题** 一次携带一个 **分类角色**

## 标记的歧义

- "backlog" 以前用于表示托管问题的 *工具* 和其中的 *工作主体*——已解决：工具是 **问题跟踪器**；"backlog" 不再用作领域术语。
- "backlog backend" / "backlog manager" ——已解决：合并为 **问题跟踪器**。

