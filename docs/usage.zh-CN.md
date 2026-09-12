# FuXi 使用指南

安装、配置与使用 FuXi（终端 AI 编程智能体）的完整指南。本文档覆盖从首次
安装到高级特性的完整流程，并特意为第一次使用的新手编写。

> **赶时间？** 用 [快速开始](../README.zh-CN.md#快速开始) 在几分钟内完成
> 安装、启动并开启会话。之后再回到这里深入。
>
> 配套参考：
> [键盘快捷键](keybindings.zh-CN.md) · [环境变量](environment.zh-CN.md) ·
> [常见问题](faq.zh-CN.md) · [安全与隐私](../security-privacy/README.md)

---

## 目录

- [概述](#概述)
- [安装](#安装)
- [首次运行与配置](#首次运行与配置)
- [你的第一次会话](#你的第一次会话)
- [权限与安全](#权限与安全)
- [会话、记忆与恢复](#会话记忆与恢复)
- [工具与 MCP](#工具与-mcp)
- [命令行参考](#命令行参考)
- [更新](#更新)
- [故障排查](#故障排查)
- [进阶](#进阶)

---

## 概述

FuXi 以 **思考 → 行动 → 验证** 循环工作：它推理任务、用 50+ 内置工具行动
（文件编辑、shell、搜索、网页抓取等）、查看结果，并不断迭代直到工作完成
且被验证 —— 失败的测试被修复、测试套件全绿、PR 就绪。

核心特性：

- **终端优先** —— 在终端中运行的丰富 TUI。
- **不绑定提供商** —— 可使用任意 OpenAI 兼容端点、Gemini、Bedrock/Vertex
  或其他 OpenAI 兼容提供商，或通过 FuXi OAuth 登录。
- **自带密钥** —— 你的代码与提示词直接发往你选择的提供商，FuXi 不居中。
- **本地优先** —— 配置、凭据、会话与记忆默认存储在你的设备 `~/.fuxi/` 下。
- **单个静态二进制** —— 无运行时依赖。

---

## 安装

### macOS / Linux

```bash
curl -fsSL https://downloads.fuxicode.com/bootstrap.sh | bash
```

### Windows（PowerShell）

```powershell
irm https://downloads.fuxicode.com/bootstrap.ps1 | iex
```

### Windows（CMD）

```bat
curl -fsSL https://downloads.fuxicode.com/install.cmd -o "%TEMP%\fuxi-install.cmd" && "%TEMP%\fuxi-install.cmd"
```

所有安装方式都会把 FuXi 放到 `~/.local/bin`（Windows 为
`%USERPROFILE%\.local\bin`），并在尚未加入时自动加进你的**用户** `PATH`。

### 验证安装

```bash
fuxi --version
fuxi doctor      # 环境自检（配置、API Key、git、ripgrep 等）
```

### 升级

重跑同一条安装命令 —— 安装与升级是同一条命令。或在会话内运行 `fuxi update`
（见[更新](#更新)）。

### 卸载

```bash
# macOS / Linux
rm -f "$HOME/.local/bin/fuxi"
rm -rf "$HOME/.fuxi"   # 可选：连同配置/状态一起删除

# Windows（PowerShell）
Remove-Item -Force "$env:USERPROFILE\.local\bin\fuxi.exe"
Remove-Item -Recurse -Force "$env:USERPROFILE\.fuxi"   # 可选
```

---

## 首次运行与配置

启动 TUI：

```bash
fuxi
```

首次运行时，FuXi 会在 `~/.fuxi/` 下创建配置。你需要一个可对话的模型，有两条
路径可选。

### 1. 登录

```bash
fuxi login
```

`fuxi login` 用你的 FuXi 账号完成认证，随后自动开通 FuXi 托管模型。
无需 API Key。用 `fuxi logout` 退出登录。

无交互/CI 场景用 `fuxi setup-token`，它会打印一个可导出为
`FUXI_OAUTH_TOKEN` 的令牌。

### 2. 自带密钥

通过环境变量设置提供商 API Key，或直接编写 `~/.fuxi/config.yaml`。
`fuxi init` 会生成一份初始模板，并根据当前已设置的环境变量自动探测提供商：

```yaml
provider: openapi
base_url: https://your-endpoint/v1
api_key: <your-key>       # 或改用 export FUXI_API_KEY
model: your-model
```

需要同时管理多个提供商/模型？使用分层 schema —— 一份 `providers:` 目录
加一层 `model:` 选择：

```yaml
providers:
  custom:
    type: openapi
    base_url: https://your-endpoint/v1
    api_key: <your-key>
    models:
      - id: your-model-id
model:
  active: { provider: custom, id: your-model-id }
```

或运行交互式向导：

```bash
fuxi wizard
```

向导会逐步引导：提供商、base URL、密钥、模型与连接测试。

### 配置参考

- **配置目录：** `~/.fuxi/`（可用 `FUXI_CONFIG_DIR` 覆盖）。
- **配置文件：** `~/.fuxi/config.yaml` —— 提供商、模型、thinking/effort、
  路由偏好，以及按端点的覆盖。FuXi 运行期间修改会热加载。
- **优先级：** 环境变量 > `config.yaml` > 内置默认值。
- **项目设置：** 项目内提交的项目设置文件（权限、hooks）会按项目生效。
- **插件：** 官方插件市场位于 `fuxicode.com/plugins`。

最常用的环境变量：

| 变量 | 作用 |
|---|---|
| `FUXI_BASE_URL` / `FUXI_API_KEY` / `FUXI_MODEL` | OpenAPI 兼容提供商配置 |
| `ANTHROPIC_API_KEY` / `ANTHROPIC_MODEL` | Anthropic 提供商配置 |
| `FUXI_THINKING_MODE` / `FUXI_THINKING_EFFORT` | `auto\|enabled\|disabled` / `low\|medium\|high\|max` |
| `FUXI_CONFIG_DIR` | 覆盖配置目录（默认 `~/.fuxi`） |
| `FUXI_DEBUG` | 设为 `1` 开启调试日志 |
| `NO_UPDATE_NOTIFIER` | 设为 `1` 时关闭后台更新检查提示 |
| `FUXI_TEMPERATURE` / `FUXI_TOP_P` / `FUXI_SEED` | 采样控制参数 |

完整参考（包括桥接/远程控制、沙箱限制、MCP 资源上限等）见
[environment.zh-CN.md](environment.zh-CN.md)。

---

## 你的第一次会话

配置好模型后，输入提示词并回车。FuXi 会推理任务、用工具行动，并验证结果。
一个典型的初次请求：

```text
修复这个仓库里失败的测试。
```

### 基本操作

- **发送消息** —— 输入提示词后按 `Enter`。按 `Ctrl+J` 或 `Shift+Enter`
  插入换行。
- **浏览命令** —— 在空提示符开头输入 `/` 并回车（或 Tab 补全），即可看到
  FuXi 能做的所有事情。
- **切换模型** —— 随时用 `/model` 选择当前使用的模型。
- **帮助与退出** —— `/help` 列出全部命令；`/exit` 退出。
- **取消** —— `Esc` 取消当前操作或关闭弹窗。
- **权限提示** —— 工具首次执行敏感操作时会请求你批准。见
  [权限与安全](#权限与安全)。

### 斜杠命令

| 命令 | 作用 |
|---|---|
| `/help`, `/commands`, `/menu` | 显示或搜索全部命令 |
| `/model` | 切换当前使用的模型 |
| `/config` | 打开配置 |
| `/status` | 显示提供商状态 |
| `/context` | 显示当前上下文窗口占用情况 |
| `/cost`, `/usage` | 会话花费 / 套餐用量 |
| `/compact` | 压缩对话历史以释放上下文空间 |
| `/clear` | 清空对话 |
| `/history`, `/resume` | 浏览或恢复历史会话/检查点 |
| `/tools` | 列出可用工具 |
| `/permissions` | 显示当前权限配置 |
| `/memory` | 显示项目记忆文件 |
| `/fork` | 显示 fork 子智能体统计信息 |
| `/away` | 列出或查看已保存的会话 away 摘要 |
| `/commit` | 创建一次 git 提交 |
| `/review` | 审查代码 / 创建 PR |
| `/doctor` | 运行诊断检查 |
| `/copy`, `/paste` | 复制上一条回复 / 将剪贴板文本作为下一条提示发送 |
| `/exit` | 退出 |

### 键盘快捷键

`/` 加回车打开命令浏览器 · `Tab` 补全斜杠命令 · `Ctrl+R` 搜索历史提示词 ·
`Ctrl+V` 或终端粘贴直接粘贴到输入框。完整快捷键速查见
[keybindings.zh-CN.md](keybindings.zh-CN.md)。

---

## 权限与安全

FuXi 能够改文件、运行 shell 命令，因此内置了明确的权限模型与安全护栏。
工具首次接触到敏感操作时会弹出权限提示；之后随时可用 `/permissions`
查看并调整所有规则。

### 权限模式

| 模式 | 行为 |
|---|---|
| `default` | 敏感操作逐项提示批准 |
| `plan` | 先规划再行动，不做任何更改 |
| `bypassPermissions` | 自动批准一切 |

在 TUI 内用 `Shift+Tab` 循环切换，或在启动时用 `--permission-mode <mode>`
指定。

`--auto` 只自动批准安全分类器判定为安全的工具调用，且带熔断机制。
`--dangerously-skip-permissions` 会跳过**所有**权限检查 —— 仅在完全可信、
隔离的环境中使用，风险自负。

### 命令安全如何运作

shell 命令（`bash` / PowerShell）在执行前会经过 AST 安全分类器与规则集过滤。
每次执行的操作都会记录在本地审计日志中供查阅。用 `/permissions` 管理规则。

完整的威胁模型与防护措施见
[安全白皮书](../security-privacy/SECURITY.zh-CN.md)。

---

## 会话、记忆与恢复

- **会话记录持久化到磁盘** —— 对话保存在本地。
- **检查点** 支持恢复、回滚或分叉会话。
- **自动压缩** —— 长对话会自动压缩以节省 token。
- **梦境整理** —— 空闲期整理并跨会话整合记忆。

从命令行恢复：

```bash
fuxi -r <sessionId>    # 恢复指定会话
fuxi -c                # 继续当前目录下最近一次对话
```

或在 TUI 内使用 `/history` 或 `/resume`。用 `/memory` 查看项目记忆文件。

---

## 工具与 MCP

FuXi 内置 50+ 工具 —— 文件读/写/改、shell（`bash` / PowerShell）、ripgrep
搜索、网页抓取、LSP 诊断、Jupyter、通过 MCP 的浏览器控制、后台任务，
以及并行子智能体。

### 限制工具

```bash
fuxi --tools ""               # 无工具
fuxi --tools default          # 全部内置工具
fuxi --tools <name1> <name2>  # 指定子集
fuxi --allowed-tools <list>   # 逗号分隔的允许清单
fuxi --disallowed-tools <list> # 逗号分隔的禁用清单
```

### MCP 服务器

只有在你显式配置时，MCP 服务器才会被加载。

```bash
fuxi --mcp-config <configs...>   # 从 JSON 字符串或文件路径加载 MCP 服务器
fuxi --strict-mcp-config         # 仅使用 --mcp-config 指定的服务器
fuxi mcp                         # 配置与管理 MCP 服务器
```

---

## 命令行参考

> 你安装的二进制上的 `fuxi --help` 始终是权威来源。下表覆盖最常用的参数
> 与命令。

### 参数

| 类别 | 参数 | 作用 |
|---|---|---|
| 模型 | `-m, --model <name>` | 覆盖本次运行使用的模型 |
| | `-P, --provider <type>` | 提供商类型：`anthropic` \| `openapi` |
| | `-b, --base-url <url>` | 覆盖 base URL（启用 OpenAPI 提供商） |
| | `-k, --api-key <key>` | 覆盖本次运行使用的 API Key |
| | `--fallback-model <model>` | 默认模型过载时自动回退到该模型 |
| 会话 | `-r, --resume <sessionId>` | 恢复某个指定的历史会话 |
| | `-c, --continue` | 继续当前目录下最近一次会话 |
| | `--session-id <uuid>` | 使用指定的会话 ID（必须是合法 UUID） |
| | `--fork-session` | 恢复时新建会话 ID，而非复用原会话 |
| | `--from-pr [value]` | 恢复与某个 PR（编号/URL）关联的会话 |
| | `--prefill <text>` | 预填充提示输入框（不自动提交） |
| | `-d, --dir <path>` | 工作目录 |
| 权限 | `--permission-mode <mode>` | `default` \| `plan` \| `bypassPermissions` |
| | `--auto` | 自动批准安全的工具调用（经分类器判定，带熔断机制） |
| | `--dangerously-skip-permissions` | 跳过所有权限检查（危险） |
| 思考 | `--thinking <mode>` | `enabled` \| `adaptive` \| `disabled` |
| | `--effort <level>` | `low` \| `medium` \| `high` \| `max` |
| | `--max-tokens <n>` | 每次 API 调用的最大输出 token 数 |
| | `--max-thinking-tokens <n>` | 思考预算 token 上限 |
| | `--max-budget-usd <amount>` | API 调用的最大花费上限（美元） |
| 工具与 MCP | `--tools <tools...>` | 限制内置工具集（`""` = 无，`default` = 全部，或工具名） |
| | `--allowed-tools` / `--disallowed-tools <list>` | 逗号分隔的工具允许 / 禁用清单 |
| | `--mcp-config <configs...>` | 从 JSON 字符串或文件路径加载 MCP 服务器 |
| | `--strict-mcp-config` | 仅使用 `--mcp-config` 指定的 MCP 服务器 |
| | `--plugin-dir <path>` | 本次会话从指定目录加载插件 |
| 打印 | `-p, --print` | 打印回答后退出（适合管道） |
| | `--output-format` / `--input-format <format>` | `text` / `json` / `stream-json`（需配合 `--print`） |
| 检查 | `--status` | 打印解析后的提供商状态并退出 |
| | `--config` | 打印解析后的配置并退出 |
| 调试 | `--debug [pattern]` | 开启调试日志，可选按 pattern 过滤 |
| | `--verbose` | 开启详细日志 |
| | `-v, --version` / `-h, --help` | 版本信息 / 完整的参数与命令参考 |

`fuxi --help` 中还包含系统提示词覆盖（`--system-prompt`、
`--append-system-prompt` 等）、hook 触发（`--init`、`--init-only`、
`--maintenance`）、swarm/agent 参数（`--team`、`--agents`、`--name` 等）、
worktree 参数（`--worktree`、`--tmux`）以及采样控制。

### 子命令

| 命令 | 作用 |
|---|---|
| `fuxi`（或 `fuxi tui`） | 启动交互式 TUI |
| `fuxi login` / `fuxi logout` | 登录 FuXi 账号（stdin 流程）/ 退出登录 |
| `fuxi setup-token` | 登录并打印一个用于 `FUXI_OAUTH_TOKEN` 的 token（无交互/CI 场景） |
| `fuxi wizard` | TUI 配置向导：提供商、base URL、密钥、模型、连接测试 |
| `fuxi init [--force]` | 生成一份 `~/.fuxi/config.yaml` 模板（从环境变量自动探测提供商） |
| `fuxi doctor` | 对运行环境进行诊断检查 |
| `fuxi verify` | 验证与已配置提供商的连通性 |
| `fuxi info` | 显示提供商与模型信息 |
| `fuxi agents` | 按来源列出已配置的 agent |
| `fuxi auto-mode <sub>` | 查看自动模式分类器规则（`defaults` \| `config` \| `critique`） |
| `fuxi proxy` | 启动智能路由代理（Anthropic ↔ OpenAI 协议转换） |
| `fuxi launch [args]` | 通过代理启动被代理的二进制，使用你的 FuXi 配置 |
| `fuxi mcp` | 配置与管理 MCP 服务器 |
| `fuxi plugin` | 管理 FuXi 插件 |
| `fuxi workflow` | 管理工作流定义 |
| `fuxi relay-server` | 启动中继服务器（用 `FUXI_RELAY_TOKEN` 鉴权） |
| `fuxi remote-control` | 作为云端远程控制 worker 运行（`--remote-control` 的别名） |
| `fuxi update [version]` | 下载并安装版本（校验和验证、原子替换） |

---

## 更新

FuXi 会在后台检查新版本，一旦有可用更新会打印一行提示。原地更新：

```bash
fuxi update            # 最新版本
fuxi update 0.1.2      # 指定版本
```

`fuxi update` 会下载目标版本，对照已发布的 manifest 校验 SHA-256，并原子性地
替换正在运行的二进制文件 —— 不会留下安装到一半的中间状态。可通过
`--no-update-notifier` 或 `NO_UPDATE_NOTIFIER=1` 关闭后台检查提示。

---

## 故障排查

### 环境自检

```bash
fuxi doctor     # 配置、API Key、git、ripgrep 等
fuxi verify     # 提供商连通性
```

### 命令或工具被阻止

shell 命令在执行前会经过 AST 安全分类器与规则集过滤。若某命令被意外阻止，
用 `/permissions` 查看权限规则并在 TUI 内调整。

### 报告 bug

使用 **Bug report** 模板提交 issue，附上 `fuxi --version`、你的 OS/终端 与
shell，以及最小复现步骤。

### 报告安全问题

请通过 [GitHub 安全通告](https://github.com/fuxicodex/Fuxi/security/advisories/new)
私下报告。**不要**公开提交 issue。

---

## 进阶

- **智能路由** —— 每个请求按复杂度评分并路由到合适的模型档位；简单任务
  交给廉价模型，困难任务保留给强模型，并带自动故障转移。
- **子智能体** —— 为大型任务并行执行；`/fork` 显示 fork 子智能体统计。
- **Hooks、skills 与插件** —— 可扩展且支持热重载；官方插件市场位于
  `fuxicode.com/plugins`。
- **远程控制** —— 用 `fuxi remote-control` 或 `--remote-control` 作为云
  worker 运行。
- **代理** —— `fuxi proxy` 启动智能路由代理（Anthropic ↔ OpenAI 协议转换）；
  `fuxi launch` 通过它运行被代理的二进制。
- **Worktree 与 swarm** —— `--worktree` 为会话创建 git worktree；
  `--team` 加入 swarm 协同，与队友协作。
- **多窗口** —— 不打断当前工作的前提下，在多个并发会话间切换。
- **图片与语音** —— 从剪贴板粘贴图片（`Ctrl+V`）、图片说明，以及按住说话
  的语音捕获（`Alt+V`）。

按版本逐个查看细节见 [CHANGELOG.md](../CHANGELOG.md)，完整快捷键速查见
[keybindings.zh-CN.md](keybindings.zh-CN.md)。