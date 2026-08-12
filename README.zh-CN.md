# FuXi

[English](README.md) | [简体中文](README.zh-CN.md)

> **一个住在你终端里的 AI 编程智能体。**
> 代号 **一画开天 (YiHuaKaiTian)**。

FuXi 是一个快速、自包含的 AI 开发者终端：在丰富的 TUI 中读代码、改文件、
运行命令、驱动工具，并在多个 LLM 提供商之间进行成本感知的路由与自动故障
转移。单个静态二进制文件，无运行时依赖。

**终端优先** · **不绑定提供商** · **自带密钥** · **MCP 客户端** · **自动更新**

主页：**https://fuxicode.com**

![FuXi 实际演示](docs/fuxi-demo.gif)

---

## 目录

- [亮点](#亮点)
- [与同类产品的对比](#与同类产品的对比)
- [评估与基准](#评估与基准)
- [安装](#安装)
- [快速开始](#快速开始)
- [使用指南](#使用指南)
- [项目结构](#项目结构)
- [License](#license)

## 亮点

**模型只是引擎，FuXi 才是整车。** 模型单独只能回答问题；FuXi 让它成为真正
的工人 —— 推理、在你真实的代码库上行动、验证结果，并且成本可控、尽在你
掌握之中。

- **思考 → 行动 → 验证循环** —— FuXi 不只是回答。它在一个循环中工作：
  推理任务、用工具行动（改文件、跑命令、搜代码）、查看结果，并不断迭代
  直到工作完成且被验证 —— 失败的测试被修复、测试套件全绿、PR 就绪。
- **智能路由** —— 每个请求按复杂度评分，路由到合适的模型档位：
  简单任务交给轻量模型，困难任务才动用强大模型。自动故障转移与可选的主备
  竞速，让提供商出问题时你的工作也不中断。
- **50+ 内置工具** —— 文件读/写/改、shell（`bash` / PowerShell）、ripgrep
  搜索、网页抓取、基于 LSP 的诊断、Jupyter、通过 MCP 的浏览器控制、
  后台任务，以及并行**子智能体** —— 全部装在一个二进制里。
- **安全护栏** —— shell 命令在执行前会经过 AST 安全分类器与规则集过滤；
  细粒度权限、操作审计和显式的权限模型，让自主执行始终处于你的掌控中。
- **持久会话与记忆** —— 会话记录持久化到磁盘；检查点支持恢复、回滚或
  分叉；空闲期的"梦境"整理会跨会话整合记忆；长对话自动压缩以节省 token。
- **自带密钥，或直接登录** —— 使用任意提供商 API Key（OpenAI 兼容、
  Gemini、Bedrock/Vertex，或其他 OpenAI 兼容端点），或通过 FuXi OAuth
  登录。数据始终由你掌控。
- **可扩展** —— MCP 客户端、hooks、skills、plugins 与自定义斜杠命令，
  全部支持热重载。
- **永久免费** —— 单个静态二进制，无运行时依赖，个人、团队、企业均
  无需许可费用。
- **自动更新** —— 后台版本检查加一条 `fuxi update` 命令即可保持安装是
  最新的，替换正在运行的二进制文件前会先做校验和验证。

---

## 与同类产品的对比

FuXi 是一个终端优先、设计上不绑定任何单一提供商的 AI 编程智能体。
下表反映的是各产品官方公开的定位，以及 FuXi 目前实际提供的能力；
产品迭代很快，请将其作为定位参考，而非详细规格。✓ = 支持，
△ = 部分支持 / 非原生，✗ = 不支持。

| | FuXi | Claude Code | GitHub Copilot CLI | Cursor | Aider |
|---|---|---|---|---|---|
| 终端优先的 CLI / TUI | ✓ | ✓ | ✓ | ✗（基于 IDE） | ✓ |
| 多提供商支持 | ✓ | ✗（仅 Anthropic） | ✗（需 Copilot 套餐） | ✓ | ✓ |
| 成本感知分层路由 | ✓ | ✗ | ✗ | △（部分实现） | ✗ |
| 故障转移与主备竞速 | ✓ | ✗ | ✗ | ✗ | ✗ |
| 自带 API Key | ✓ | ✓ | ✗（订阅制） | ✓ | ✓ |
| MCP 客户端 | ✓ | ✓ | ✗ | ✓ | ✗ |
| 并行子智能体 | ✓ | ✓ | ✗ | ✓ | ✗ |
| 持久会话与检查点 | ✓ | ✓ | ✗ | ✓ | ✗ |
| 单个静态二进制、无运行时依赖 | ✓ | ✗（依赖 Node） | ✗（依赖 Node） | ✗（IDE 应用） | ✗（依赖 Python） |

```mermaid
quadrantChart
    title AI 编程智能体 —— 定位
    x-axis "单一提供商" --> "多提供商"
    y-axis "IDE 优先" --> "终端优先"
    quadrant-1 "终端 · 多提供商"
    quadrant-2 "终端 · 单一提供商"
    quadrant-3 "IDE · 单一提供商"
    quadrant-4 "IDE · 多提供商"
    "FuXi": [0.9, 0.92]
    "Aider": [0.8, 0.75]
    "Claude Code": [0.25, 0.85]
    "GitHub Copilot CLI": [0.15, 0.7]
    "Cursor": [0.7, 0.12]
```

---

## 评估与基准

FuXi 以可复现、可自行验证的评估为原则。目前它尚未在第三方基准
（如 SWE-bench、Terminal-Bench、Aider polyglot 等）上公布官方分数；
我们更愿意提供可自行操作的评估方法，而不是一个孤立的数字。
下面是在你自己的项目上评估 FuXi 的方法：

**一份可操作的评估清单**

1. **安装与自检** —— 安装后先运行 `fuxi doctor` 验证环境
   （配置、API Key、git、ripgrep），再运行 `fuxi verify` 确认与提供商
   的连接。自检通过是评估的基准线。
2. **复现一个真实任务** —— 在你自己的项目中挑一个失败的测试，让 FuXi
   修复它；随后扩展模块并重新运行测试套件（上方演示动画就是这一流程）。
   再用日常任务重复几轮：代码审查、提交、PR、重构。
3. **同条件对比** —— 用完全相同的任务、模型与上下文，让另一款工具执行
   同样的工作，再比较正确性、工具覆盖、成本与迭代时间。同一起跑线上
   的对比才公平。

FuXi 提供了对比所需的一切手段 —— TUI 内的 `/cost`、`/usage`、`/context`、
`/status` —— 以及内置的环境自检（`fuxi doctor`）。未来若公布基准成绩，
将在此章节附上链接。

---

## 安装

### macOS / Linux

```bash
curl -fsSL https://releases.fuxicode.com/bootstrap.sh | bash
```

### Windows（PowerShell）

```powershell
irm https://releases.fuxicode.com/bootstrap.ps1 | iex
```

### Windows（CMD）

```bat
curl -fsSL https://releases.fuxicode.com/install.cmd -o "%TEMP%\fuxi-install.cmd" && "%TEMP%\fuxi-install.cmd"
```

以上三种方式都会安装到 `~/.local/bin`（Windows 上为
`%USERPROFILE%\.local\bin`），并在尚未加入时自动加进你的**用户** `PATH`。
再次运行同一条命令即可原地升级已有安装 —— 安装和升级是同一条命令。

默认安装最新版本；也可以带参数指定具体版本，例如
`./bootstrap.sh 2.202.194` 或 `./bootstrap.ps1 2.202.194`。

### 验证安装

```bash
fuxi --version
fuxi doctor      # 环境自检（配置、API Key、git、ripgrep 等）
```

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

## 快速开始

启动 TUI：

```bash
fuxi
```

首次运行时，FuXi 会在 `~/.fuxi/` 下创建配置。你需要一个可对话的模型，
有两条路径可选：

1. **登录** —— `fuxi login` 会打开浏览器，用你的 FuXi 账号完成认证，
   随后自动开通 FuXi 托管模型。无需任何 API Key。
2. **自带密钥** —— 通过环境变量设置提供商 API Key，或直接编写
   `~/.fuxi/config.yaml`（`fuxi init` 会生成一份初始模板，并根据当前
   已设置的环境变量自动探测提供商）：

   ```yaml
   provider: openapi
   base_url: https://your-endpoint/v1
   api_key: <your-key>       # 或改用 export FUXI_API_KEY
   model: your-model
   ```

   需要同时管理多个提供商/模型？使用分层 schema —— 一份 `providers:`
   目录加一层 `model:` 选择：

   ```yaml
   providers:
     custom:
       type: openapi
       base_url: https://your-endpoint/v1
       api_key: <your-key>
       models:
         - id: your-model-id
           model_canonical_name: your-model   # 可选：用于能力查询
   model:
     active: { provider: custom, id: your-model-id }
   ```

   完整的分层 schema（多提供商、按模型的能力覆盖、路由角色）请参见本仓库
   的 `config.full.example.yaml`。

   或者运行 `fuxi wizard` 进入交互式配置流程（选择提供商、输入
   base URL/密钥、选择模型、测试连接）。

配置好模型后，随时可用 `/model` 切换，用 `/config` 管理其余设置 ——
权限、hooks、skills、plugins 等一切都通过 TUI 内的斜杠命令驱动。

---

## 使用指南

### 命令行参数

启动 `fuxi` 时常用参数，按用途分组。完整参考见 `fuxi --help`。

| 类别 | 参数 | 作用 |
|---|---|---|
| 模型 | `-m, --model <name>` | 本次运行覆盖使用的模型 |
| | `-P, --provider <type>` | 提供商类型：`anthropic` \| `openapi` |
| | `-b, --base-url <url>` | 覆盖 base URL（启用 OpenAPI 提供商） |
| | `-k, --api-key <key>` | 本次运行覆盖使用的 API Key |
| 会话 | `-r, --resume <sessionId>` | 恢复某个指定的历史会话 |
| | `-c, --continue` | 继续当前目录下最近一次会话 |
| | `--session-id <uuid>` | 使用指定的会话 ID（必须是合法 UUID） |
| | `--fork-session` | 恢复时新建会话 ID，而非复用原会话 |
| | `--prefill <text>` | 预填充提示输入框（不自动提交） |
| | `-d, --dir <path>` | 工作目录 |
| 权限 | `--permission-mode <mode>` | `default` \| `plan` \| `bypassPermissions` |
| | `--auto` | 自动批准安全的工具调用（经分类器判定，带熔断机制） |
| | `--dangerously-skip-permissions` | 跳过所有权限检查（危险） |
| 思考 | `--thinking <mode>` | `enabled` \| `adaptive` \| `disabled` |
| | `--effort <level>` | `low` \| `medium` \| `high` \| `max` |
| | `--max-tokens <n>` | 每次 API 调用的最大输出 token 数 |
| 工具与 MCP | `--tools <tools...>` | 限制内置工具集（`""` = 无，`default` = 全部，或工具名） |
| | `--mcp-config <configs...>` | 从 JSON 字符串或文件路径加载 MCP 服务器 |
| | `--strict-mcp-config` | 仅使用 `--mcp-config` 指定的 MCP 服务器 |
| 检查 | `--status` | 打印解析后的提供商状态并退出 |
| | `--config` | 打印解析后的配置并退出 |
| 调试 | `--debug [pattern]` | 开启调试日志，可选按 pattern 过滤 |
| | `--verbose` | 开启详细日志 |
| | `-v, --version` / `-h, --help` | 版本信息 / 完整的参数与命令参考 |

`fuxi --help` 中还包含系统提示词覆盖、工具限制、采样控制，以及
swarm/agent 相关参数。

### 子命令

| 命令 | 作用 |
|---|---|
| `fuxi`（或 `fuxi tui`） | 启动交互式 TUI |
| `fuxi login` | 登录 FuXi 账号，然后配置 API 凭据 |
| `fuxi setup-token` | 登录并打印一个用于 `FUXI_OAUTH_TOKEN` 的 token（无交互/CI 场景） |
| `fuxi wizard` | TUI 配置向导：提供商、base URL、密钥、模型、连接测试 |
| `fuxi init [--force]` | 生成一份 `~/.fuxi/config.yaml` 模板（从环境变量自动探测提供商） |
| `fuxi doctor` | 对运行环境进行诊断检查 |
| `fuxi verify` | 验证与已配置提供商的连通性 |
| `fuxi info` | 显示提供商与模型信息 |
| `fuxi update [version]` | 下载并安装版本（校验和验证、原子替换） |
| `fuxi agents` | 按来源列出已配置的 agent |
| `fuxi auto-mode <sub>` | 查看 auto-mode 分类器规则（`defaults` \| `config` \| `critique`） |
| `fuxi proxy` | 启动智能路由代理（提供商转换） |
| `fuxi launch [args]` | 通过代理启动被代理的二进制，使用你的 FuXi 配置 |
| `fuxi mcp serve` | 将 FuXi 自身作为 MCP stdio 服务器运行 |
| `fuxi remote-control` | 作为云端远程控制 worker 运行（`--remote-control` 的别名） |

### TUI 内斜杠命令

输入 `/` 并回车（或 Tab 补全）浏览全部命令：

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

**键盘与输入：** `/` 加回车打开命令浏览器 · `Tab` 补全斜杠命令 ·
`Ctrl+R` 搜索历史提示词 · `Ctrl+V` 或终端粘贴直接粘贴到输入框 ·
括号粘贴用于处理大段粘贴内容。

### 更新

FuXi 会在后台检查新版本，一旦有可用更新会打印一行提示。原地更新：

```bash
fuxi update            # 最新版本
fuxi update 2.203.0    # 指定版本
```

`fuxi update` 会下载目标版本，对照已发布的 manifest 校验 SHA-256，
并原子性地替换正在运行的二进制文件 —— 不会留下安装到一半的中间状态。
可通过 `--no-update-notifier` 或 `NO_UPDATE_NOTIFIER=1` 关闭后台检查提示。

### 配置

- **配置目录：** `~/.fuxi/`（可用 `FUXI_CONFIG_DIR` 覆盖）。
- **配置文件：** `~/.fuxi/config.yaml` —— 提供商、模型、
  thinking/effort、智能路由、脱敏，以及按端点的能力覆盖。FuXi 运行期间
  修改会热加载。每个字段的完整说明见本仓库的 `config.full.example.yaml`。
- **优先级：** 环境变量 > `config.yaml` > 内置默认值。
- **项目设置：** 项目内提交的项目设置文件（权限、hooks）会按项目生效。
- **插件：** 官方插件市场位于 `fuxicode.com/plugins`。

常用环境变量：

| 变量 | 作用 |
|---|---|
| `FUXI_BASE_URL` / `FUXI_API_KEY` / `FUXI_MODEL` | OpenAPI 兼容提供商配置 |
| `FUXI_THINKING_MODE` / `FUXI_THINKING_EFFORT` | `auto\|enabled\|disabled` / `low\|medium\|high\|max` |
| `FUXI_THINKING_STRATEGY` | `auto\|native\|prompt_inject\|two_phase` |
| `FUXI_CONFIG_DIR` | 覆盖配置目录（默认 `~/.fuxi`） |
| `FUXI_DEBUG` | 设为 `1` 开启调试日志 |
| `NO_UPDATE_NOTIFIER` | 设为 `1` 时关闭后台更新检查提示 |
| `FUXI_TEMPERATURE` / `FUXI_TOP_P` / `FUXI_SEED` | 采样控制参数 |

完整的环境变量参考（包括沙箱限制、MCP 资源上限等）请运行
`fuxi --help`。

---

## 项目结构

本仓库承载 FuXi 的文档、安装包与 issue 追踪。产品源码为闭源，未在本仓库
发布（见 License）。

---

## License

**闭源。** Copyright © 2026 FUXI（上海翊太科技有限公司 / Shanghai YiTai Technology Co., Ltd.）。保留所有权利。
