# self-tracker — 自我追踪 Skill

一个记录与自我觉察工具。通过 5 级渐进式记录和周期性回看，帮助你发现情绪周期和行为规律。

> **不是写下来就觉察了，是回看的时候，才真正看见自己。**

## 这是什么

self-tracker 是一个 Agent Skill，引导你记录每天的内在状态（情绪、触发事件、感受），并在周/月回看时自动分析数据，发现隐藏的情绪模式。

与普通日记不同，self-tracker 的核心价值在于**回看分析**——单独的记录是一个点，连续的回看是一条线。

## 核心功能

- **5 级渐进记录**：从 10 秒的情绪打分（Level 1）到 5 分钟的结构化记录（Level 5），按当天精力选择深度
- **周回看分析**：情绪走势图、高频情绪词、最好/最差日分析、模式发现
- **月回看分析**：趋势对比、触发场景归类、自动标记重复模式
- **模式沉淀**：≥3 次出现的触发场景自动写入 `review/patterns/`，持续追踪

## 安装

### 前置要求

- [Claude Code](https://claude.ai/code) 已安装并配置（或其他 skills-compatible 的 AI agent runtime）
- Python 3.x（用于数据提取脚本）

self-tracker 基于开放的 Agent Skills 协议，可在任何 skills-compatible 的 AI agent runtime 中运行。

### 方式一：一行命令（推荐，跨 runtime）

打开你正在用的 agent（Claude Code、Codex、Cursor、OpenClaw、CodeBuddy 等），告诉它：

> 帮我安装这个 skill：https://github.com/<owner>/self-tracker

或者用通用 CLI 安装器（[vercel-labs/skills](https://github.com/vercel-labs/skills)，支持 55+ runtime）：

```bash
npx skills add <owner>/self-tracker -a claude-code
```

它会自动识别你当前的 runtime 并把 skill 放到正确目录。需要指定时加 `-a claude-code` / `-a codex` / `-a cursor` 等参数。

### 方式二：手动安装

<details>
<summary>展开查看各 runtime 的 skills 目录</summary>

| Runtime | 安装路径 |
|---|---|
| Claude Code | `~/.claude/skills/self-tracker/` |
| Codex CLI | `~/.codex/skills/self-tracker/` |
| Cursor | `~/.cursor/skills/self-tracker/` |
| OpenClaw | `~/.openclaw/workspace/skills/self-tracker/` |
| 其他 runtime | clone 到对应 runtime 的 `skills/` 目录 |

</details>

```bash
git clone https://github.com/<owner>/self-tracker <上面对应的路径>
```

> **Windows 用户注意**：标准 Claude Code 路径为 `%APPDATA%\Claude\skills\`。如在 CherryStudio 中使用，路径为 `%APPDATA%\CherryStudio\Data\Skills\`。

## 使用方法

### 日常记录

直接跟 Agent 说：

- 「记录一下今天的情绪」→ 自动匹配适合你的记录深度
- 「今天状态不好」→ AI 会引导你用最省力的方式记录
- 「我总觉得被催的时候会烦躁」→ 引导三级记录，挖出反应模式

### 回顾分析

- 「回顾一下我这周的状态」→ 生成周分析报告
- 「帮我看看这个月有什么规律」→ 生成月分析报告
- 「最近情绪怎么样」→ 快速概览近期趋势

### AI 不会做的事

- ❌ 不会主动提醒你记录（记录是你的自由，不是任务）
- ❌ 不会评判你的情绪评分（只做趋势对比，不给绝对值评价）
- ❌ 不会把你的记录写入 tracking/ 目录（那是你的私人空间）

## Skill 结构

```
self-tracker/
├── SKILL.md              # 导航页：路由规则 + 核心立场 + Gotchas
├── references/
│   ├── levels.md         # 5 种记录方式详解
│   └── reviews.md        # 周/月回看方法论 + 模式发现规则
├── examples/
│   └── insights.md       # 3 个觉察案例
├── assets/
│   ├── tracking-template.md   # 每日记录模板
│   └── review-template.md     # 月度分析报告模板
└── scripts/
    └── extract_tracking.py    # tracking 数据提取脚本
```

## 设计理念

本 Skill 遵循 [Anthropic 的 Skill 方法论](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)：

- **Context Engineering**：SKILL.md 只做导航（~1.5k tokens），详细内容按需渐进加载，避免一次塞满上下文
- **Description 即路由**：描述"什么时候应该加载"而非"我能干什么"，让模型准确触发
- **Instructions + Scripts 分工**：Instructions 提供判断和经验（Gotchas），Scripts 处理可重复的数据提取
- **Gotchas 优先**：沉淀"老师傅经验"——用户不记录时不催促、Level 1 也是有效记录、同一情绪词含义可能不同

## 数据隐私

所有记录数据保存在你本地的 `tracking/` 目录中。self-tracker 不会上传或同步任何数据。你拥有完全的控制权。

## 贡献

欢迎提交 Issue 和 PR。

如果你想基于 self-tracker 做二次开发，建议先阅读 `references/` 中的设计文档，理解 5 级记录和回看分析的设计逻辑。

## 致谢

- 灵感来源：公众号推文[觉察自己最快的方式，不是想，是记](https://mp.weixin.qq.com/s/IsLxmTyHCu_5CC5sB0KKcA)
- 方法论参考：[Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)

## License

MIT
