# FuXi 架构

**Architecture**

*最后更新：2026-09-12 · 版本 1.0*

本页说明 FuXi 的构建方式：让模型能够行动的**执行底座**、让长任务不中断的
**持久化引擎**、选择模型的**路由层**，以及**多窗口**与**可扩展**体系。它覆盖
[README](../README.zh-CN.md) 中概述的产品维度。

> 相关文档：[使用指南](usage.zh-CN.md) ·
> [安全白皮书](../security-privacy/SECURITY.zh-CN.md) ·
> [隐私控制](../security-privacy/DATA_PROTECTION.zh-CN.md)

---

## 1. 执行底座：模型在你的真实环境中行动

FuXi 把模型从"能回答"升级为"能干活" —— 直接在你的代码库、Shell 与浏览器中。

| 能力 | 说明 |
|---|---|
| **读写真实文件** | 直接在磁盘上读写代码、配置与文档 —— 模型看到并修改的是你的真实文件 |
| **执行真实 Shell 命令** | 执行 `Bash` / `PowerShell` 并观察输出，经 **AST 安全分类器**与**规则集**过滤；高风险命令需确认 |
| **搜索整个代码库** | 快速模式搜索（`Glob` 找路径、`Grep` 找内容），不论代码库规模 |
| **抓取实时网页** | 抓取 URL，具备 **SSRF 防护** —— 私有地址段被屏蔽 |
| **实时 LSP 诊断** | 调用语言服务器获取错误、警告、悬停信息与定义跳转 |
| **并行子智能体** | 将大型任务拆分给并行子智能体，各自独立运行并协作 |

### 工具集

FuXi 内置约五十个工具。下表按用途分组；括号内名称即 FuXi 向模型与权限规则
暴露的标识符。

| 分类 | 工具 |
|---|---|
| 文件与代码 | `Read`、`Write`、`Edit`、`Glob`、`Grep`、`NotebookEdit`、`LSP` |
| Shell | `Bash`（AST 防护）、`PowerShell` |
| 网络 | `WebFetch`（SSRF 防护）、`WebSearch`、`WebBrowser` |
| 智能体与团队 | `Agent`、`Skill`、`SendMessage`、`TeamCreate`、`TeamDelete`、`ListPeers` |
| 任务 | `TaskCreate`、`TaskGet`、`TaskList`、`TaskUpdate`、`TaskStop`、`TaskOutput`、`TodoWrite` |
| 交互与控制 | `AskUserQuestion`、`EnterPlanMode`、`ExitPlanMode`、`EnterWorktree`、`ExitWorktree`、`Sleep`、`VerifyPlan`、`StructuredOutput` |
| MCP | `MCP`、`ListMcpResources`、`ReadMcpResource` |
| 自动化 | `CronCreate`、`CronDelete`、`CronList`、`Monitor`、`RemoteTrigger`、`Workflow`、`ToolSearch`、`subscribePR`、`SuggestBackgroundPR` |
| 会话 | `Brief`、`ctxInspect`、`pushNotification`、`sendUserFile`、`terminalCapture` |

任一时刻只有一部分工具会发送给模型，其余通过 `ToolSearch` 按需发现；
`--tools`、`--allowed-tools`、`--disallowed-tools` 用于控制哪些工具可用。

### 沙箱

命令执行受文件系统规则约束，读/写路径均有允许与拒绝清单
（`allowWrite`、`denyWrite`、`denyRead`、`allowRead`）。沙箱限制见
[环境变量](environment.zh-CN.md)。

---

## 2. 持久化引擎：长任务不中断

FuXi 的设计目标是让持续数小时的任务不会崩掉：

- **持久化转录** —— 每次对话写入磁盘；重启后会话完整恢复，一条消息也不丢失。
- **检查点、恢复与回滚** —— 任意时刻创建检查点，随时恢复或回滚，并支持
  **分叉** —— 从同一检查点探索不同方向。
- **"梦境"记忆整合** —— 空闲时跨会话整合记忆与学习内容，使智能体随时间成长。
- **自动上下文压缩** —— 长对话自动压缩，保留关键信息并降低 token 成本。

---

## 3. 路由：成本感知，带故障转移

FuXi 对每个请求进行复杂度评分，并路由到合适的模型分级，使简单任务不必为
顶级模型付费：

| 分级 | 典型用途 |
|---|---|
| Free / 本地 | 本地或缓存模型 |
| Cheap | 小型、快速的托管模型 |
| Standard | 平衡的通用模型 |
| Premium | 用于难题的强模型 |

指数退避式自动故障转移在提供商被限流或宕机时保持工作继续；竞速模式并行运行
主备模型，先返回者胜出。

---

## 4. 多窗口与跨机器协同

同一项目上的多个 FuXi 窗口彼此感知：

- **本机感知** —— 窗口通过 Unix domain socket 广播文件变更，一个窗口保存后
  其余窗口自动重读该文件。
- **时间戳兜底** —— 写入前检查修改时间，冲突写入被拒绝，旧写入无法覆盖新内容。
- **跨机器中继** —— 自托管 `fuxi relay-server` 让不同地点的机器交换消息，
  以 bearer token 认证；无需任何第三方云服务。
- **共享任务列表** —— 窗口共享按项目（以 git 根目录隔离）的任务列表，原子
  文件锁确保同一任务只会被一个窗口认领。

---

## 5. 可扩展性

四种正交的扩展机制，全部支持热重载：

| 机制 | 作用 |
|---|---|
| **MCP 服务器** | 连接任意 MCP 服务器（stdio、HTTP、WebSocket；支持 OAuth），其工具立即可用 |
| **钩子（Hooks）** | 在生命周期事件上挂入自定义逻辑 —— 包括 `SessionStart`、`SessionEnd`、`UserPromptSubmit`、`PreToolUse`、`PostToolUse`、`PreCompact`、`PostCompact`、`Notification`、`Stop`、`SubagentStop` |
| **Skills 与斜杠命令** | 将工作流封装为 Skill 或自定义斜杠命令，存入代码仓库并随团队共享 |
| **插件** | 安装与管理插件（`fuxi plugin`），支持插件市场 |

---

## 6. 各部分如何协同

- **思考 → 行动 → 验证** —— 智能体推理、决定用哪个工具、行动、观察结果、反思
  —— 循环推进，直到工作被验证（测试通过、构建为绿）。
- **人在环中** —— 敏感操作需经批准且可中断；每个动作都记录在本地审计日志中。

如何驱动这些功能见[使用指南](usage.zh-CN.md)；适用于它们的隐私设置见
[隐私控制](../security-privacy/DATA_PROTECTION.zh-CN.md)。
