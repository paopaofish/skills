<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

# 真实工程师的技能库

[![skills.sh](https://skills.sh/b/mattpocock/skills)](https://skills.sh/mattpocock/skills)

我每天用于真实工程开发的 Agent 技能——不是靠运气编程。

开发真实的应用程序非常困难。像 GSD、BMAD 和 Spec-Kit 这样的方法试图通过掌控流程来提供帮助。但在这样做的过程中，它们剥夺了你的控制权，使得流程中的 bug 难以解决。

这些技能被设计为小巧、易于调整且可组合。它们适用于任何模型。它们基于数十年的工程经验。随意修改它们，让它们成为你自己的工具。享受吧。

如果你想了解这些技能的更新动态以及我创建的任何新技能，可以加入我的新闻通讯，与约 60,000 名开发者一起：

[注册新闻通讯](https://www.aihero.dev/s/skills-newsletter)

## 快速开始（30 秒设置）

1. 运行 skills.sh 安装程序：

```bash
npx skills@latest add mattpocock/skills
```

2. 选择你想要的技能，以及你想要安装它们的编码 Agent。**确保选择 `/setup-matt-pocock-skills`**。

3. 在你的 Agent 中运行 `/setup-matt-pocock-skills`。它将：
   - 询问你想使用哪个问题跟踪器（GitHub、Linear 或本地文件）
   - 询问你在分类问题时应用什么标签（`/triage` 使用标签）
   - 询问你想将创建的任何文档保存在哪里

4. 完成——你已准备就绪。

## 为什么这些技能存在

我构建了这些技能，以修复我在使用 Claude Code、Codex 和其他编码 Agent 时看到的常见失败模式。

### #1：Agent 没有按照我的意愿执行

> "没有人确切知道他们想要什么"
>
> David Thomas & Andrew Hunt，《[程序员修炼之道](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)》

**问题**。软件开发中最常见的失败模式是目标不一致。你认为开发人员知道你想要什么。然后你看到他们构建的东西——你意识到它完全没有理解你。

这在 AI 时代也是如此。你和 Agent 之间存在沟通鸿沟。解决这个问题的方法是**严格盘问环节**——让 Agent 向你提出关于你正在构建的内容的详细问题。

**解决方案**是使用：

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) - 用于非代码用途
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) - 与 [`/grill-me`](./skills/productivity/grill-me/SKILL.md) 相同，但添加了更多功能（见下文）

这是我最受欢迎的技能。它们帮助你在开始之前与 Agent 保持一致，并深入思考你正在做的更改。每次你想要进行更改时都要使用它们。

### #2：Agent 过于冗长

> 使用通用语言，开发人员之间的对话和代码表达都源自同一个领域模型。
>
> Eric Evans，《[领域驱动设计](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)》

**问题**：在项目开始时，开发人员和为他们构建软件的人（领域专家）通常说着不同的语言。

我对我的 Agent 也有同样的紧张感。Agent 通常被放入项目中，并被要求自行弄清楚行话。所以它们用 20 个词来表达本来 1 个词就能说清楚的内容。

**解决方案**是共享语言。它是一个帮助 Agent 解码项目中使用的行话的文档。

<details>
<summary>
示例
</summary>

这是一个来自我的 `course-video-manager` 仓库的 [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) 示例。哪一个更易读？

- **之前**："当一个课程内的章节中的课程被'实现'（即在文件系统中获得位置）时会出现问题"
- **之后**："物化级联存在问题"

这种简洁性在一次次会话中得到回报。

</details>

这已内置于 [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) 中。它是一个盘问环节，但帮助你与 AI 建立共享语言，并在 ADR 中记录难以解释的决策。

很难解释这有多强大。它可能是这个仓库中最酷的技术。试试看。

> [!TIP]
> 共享语言除了减少冗长之外还有许多其他好处：
>
> - **变量、函数和文件的命名保持一致**，使用共享语言
> - 因此，**代码库对 Agent 来说更易于导航**
> - Agent 还**在思考上花费更少的 token**，因为它可以使用更简洁的语言

### #3：代码无法工作

> "始终采取小而谨慎的步骤。反馈的频率是你的速度限制。永远不要承担太大的任务。"
>
> David Thomas & Andrew Hunt，《[程序员修炼之道](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)》

**问题**：假设你和 Agent 就构建什么达成了一致。当 Agent _仍然_ 产生垃圾代码时会发生什么？

是时候看看你的反馈循环了。如果没有关于它生成的代码实际如何运行的反馈，Agent 将盲目飞行。

**解决方案**：你需要通常的一系列反馈循环：静态类型、浏览器访问和自动化测试。

对于自动化测试，红 - 绿 - 重构循环至关重要。这是 Agent 首先编写一个失败的测试，然后修复测试。这有助于为 Agent 提供一致的反馈级别，从而产生更好的代码。

我构建了一个 **[`/tdd`](./skills/engineering/tdd/SKILL.md) 技能**，你可以将其插入任何项目。它鼓励红 - 绿 - 重构，并为 Agent 提供关于什么是好测试和坏测试的大量指导。

对于调试，我还构建了一个 **[`/diagnose`](./skills/engineering/diagnose/SKILL.md)** 技能，它将最佳调试实践封装到一个简单的循环中。

### #4：我们构建了一个泥球

> "每天都要投资于系统的设计。"
>
> Kent Beck，《[解析极限编程](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)》

> "最好的模块是深度的。它们允许通过简单的接口访问大量功能。"
>
> John Ousterhout，《[软件设计的哲学](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)》

**问题**：大多数用 Agent 构建的应用程序都很复杂且难以更改。因为 Agent 可以极大地加速编码，它们也加速了软件熵增。代码库以前所未有的速度变得更加复杂。

**解决方案**是对 AI 驱动的开发采用一种全新的方法：关心代码的设计。

这已构建到这些技能的每一层中：

- [`/to-prd`](./skills/engineering/to-prd/SKILL.md) 在创建 PRD 之前向你询问你正在接触哪些模块
- [`/zoom-out`](./skills/engineering/zoom-out/SKILL.md) 告诉 Agent 在整个系统的上下文中解释代码

至关重要的是，[`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) 帮助你拯救已成为泥球的代码库。我建议每隔几天在你的代码库上运行一次。

### 总结

软件工程基础比以往任何时候都更重要。这些技能是我将这些基础浓缩为可重复实践的最佳努力，以帮助你交付职业生涯中最好的应用程序。享受吧。

## 参考

### 工程技能

我每天用于代码工作的技能。

- **[diagnose](./skills/engineering/diagnose/SKILL.md)** — 针对严重 bug 和性能回归的纪律性诊断循环：复现 → 最小化 → 假设 → 仪器化 → 修复 → 回归测试。
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** — 盘问环节，根据现有领域模型挑战你的计划，精炼术语，并内联更新 `CONTEXT.md` 和 ADR。
- **[triage](./skills/engineering/triage/SKILL.md)** — 通过分类角色状态机对问题进行分类。
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** — 在代码库中寻找深化机会，参考 `CONTEXT.md` 中的领域语言和 `docs/adr/` 中的决策。
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** — 搭建其他工程技能使用的每仓库配置（问题跟踪器、分类标签词汇、领域文档布局）。在使用 `to-issues`、`to-prd`、`triage`、`diagnose`、`tdd`、`improve-codebase-architecture` 或 `zoom-out` 之前，每个仓库运行一次。
- **[tdd](./skills/engineering/tdd/SKILL.md)** — 测试驱动开发，采用红 - 绿 - 重构循环。一次一个垂直切片地构建功能或修复 bug。
- **[to-issues](./skills/engineering/to-issues/SKILL.md)** — 使用垂直切片将任何计划、规范或 PRD 分解为可独立获取的 GitHub issue。
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** — 将当前对话上下文转化为 PRD 并将其作为 GitHub issue 提交。无需访谈——只需综合你已经讨论过的内容。
- **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** — 告诉 Agent 放大并提供更广泛的上下文或对不熟悉代码部分的更高层次视角。
- **[prototype](./skills/engineering/prototype/SKILL.md)** — 构建一次性原型以阐明设计——可以是用于状态/业务逻辑问题的可运行终端应用程序，或者是可以从一个路由切换的几种截然不同的 UI 变体。

### 生产力技能

通用工作流工具，不特定于代码。

- **[caveman](./skills/productivity/caveman/SKILL.md)** — 超压缩通信模式。通过删除填充内容同时保持完整的技术准确性，减少约 75% 的 token 使用量。
- **[grill-me](./skills/productivity/grill-me/SKILL.md)** — 对计划或设计进行无情访谈，直到决策树的每个分支都得到解决。
- **[handoff](./skills/productivity/handoff/SKILL.md)** — 将当前对话压缩成交接文档，以便另一个 Agent 可以继续工作。
- **[teach](./skills/productivity/teach/SKILL.md)** — 通过多个会话教授用户新技能或概念，使用当前目录作为有状态的教学工作区。
- **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** — 创建具有适当结构、渐进式披露和捆绑资源的新技能。

### 杂项技能

我偶尔使用但不常用的工具。

- **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** — 设置 Claude Code 钩子，在执行之前阻止危险的 git 命令（push、reset --hard、clean 等）。
- **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** — 将测试文件从 `as` 类型断言迁移到 @total-typescript/shoehorn。
- **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** — 创建包含章节、问题、解决方案和解释器的练习目录结构。
- **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** — 设置带有 lint-staged、Prettier、类型检查和测试的 Husky pre-commit 钩子。

---

## 总结分析

### 核心理念

这套技能库体现了作者 Matt Pocock 对 AI 辅助软件开发的深刻思考。其核心理念可以概括为：**AI 应该增强而非取代工程师的判断力**。与传统的全流程自动化方案（如 GSD、BMAD、Spec-Kit）不同，这套技能强调保持人类对开发过程的控制权。

### 四大问题与解决方案的对应关系

| 问题 | 根本原因 | 解决方案 | 关键技能 |
|------|---------|---------|---------|
| Agent 不理解需求 | 沟通鸿沟 | 盘问环节 | `/grill-me`, `/grill-with-docs` |
| Agent 过于冗长 | 缺乏共享语言 | 建立领域术语 | `CONTEXT.md`, ADR |
| 代码无法工作 | 缺少反馈循环 | 测试驱动开发 | `/tdd`, `/diagnose` |
| 代码架构混乱 | 忽视设计 | 持续关注架构 | `/improve-codebase-architecture`, `/zoom-out` |

### 设计原则分析

1. **原子性与可组合性**
   - 每个技能都专注于单一职责，小巧精悍
   - 技能之间可以灵活组合，适应不同场景
   - 避免了大型框架的僵化问题

2. **反馈驱动开发**
   - 强调快速反馈循环（红 - 绿 - 重构）
   - 通过测试、类型检查、浏览器访问等多层次反馈
   - 让 AI 在明确的约束下工作

3. **知识沉淀**
   - 通过 `CONTEXT.md` 积累领域知识
   - 通过 ADR（架构决策记录）记录重要决策
   - 形成项目的共享语言，降低沟通成本

4. **渐进式改进**
   - 不追求一次性完美，而是持续改进
   - `/improve-codebase-architecture` 定期运行，防止技术债务累积
   - 符合敏捷开发和极限编程的理念

### 适用场景

这套技能特别适合以下场景：

- **中大型项目**：需要维护清晰的架构和领域语言
- **团队协作**：通过文档和共享语言降低沟通成本
- **复杂业务逻辑**：需要深入理解领域模型
- **长期维护项目**：需要控制软件熵增，保持代码质量

### 局限性思考

尽管这套技能设计精良，但也存在一些需要注意的方面：

1. **学习曲线**：需要团队理解和接受这些实践方法
2. **初期投入**：建立 `CONTEXT.md` 和 ADR 需要额外时间
3. **文化适配**：需要团队认同"慢即是快"的理念
4. **工具依赖**：依赖于支持 skill 系统的 Agent（如 Claude Code）

### 总体评价

这是一套经过深思熟虑的工程实践集合，它将经典的软件工程原则（如《程序员修炼之道》、《领域驱动设计》、《极限编程》等）与 AI 辅助开发相结合。其最大价值不在于具体的技能实现，而在于传达了一种理念：**AI 是强大的工具，但优秀的工程实践仍然是成功的关键**。

对于希望在 AI 时代保持工程卓越性的团队来说，这套技能提供了宝贵的参考框架和实践指南。
