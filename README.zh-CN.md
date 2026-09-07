# FuXi

[English](README.md) | [简体中文](README.zh-CN.md)

[![GitHub stars](https://img.shields.io/github/stars/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=stars)](https://github.com/fuxicodex/Fuxi/stargazers)
[![Release](https://img.shields.io/github/v/release/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=release)](https://github.com/fuxicodex/Fuxi/releases)
[![Last commit](https://img.shields.io/github/last-commit/fuxicodex/Fuxi?style=flat-square&color=0a6fe7)](https://github.com/fuxicodex/Fuxi/commits/main)
[![License](https://img.shields.io/badge/license-Proprietary-0a6fe7?style=flat-square)](LICENSE)

> **一个住在你终端里的 AI 编程智能体。**

FuXi 是一个快速、自包含的**终端 AI 编程智能体**：在丰富的 TUI 中读代码、改
文件、运行命令、驱动工具，并在多个 LLM 提供商之间进行成本感知的路由与自动
故障转移。FuXi 使用 Go 语言开发，交付为单个静态二进制文件，无运行时依赖。
可以把它理解为不绑定单一提供商的 Claude Code 替代方案：接入任意 OpenAI 兼容
模型，就能在其上获得 思考 → 行动 → 验证 的智能体循环。

凭借 思考 → 行动 → 验证 的智能体循环与智能路由，任意支持 OpenAPI 的模型
都能发挥出高于其原生基准的表现——这一点已在可复现的任务集上与一款主流
编码智能体做了对照评测（见 [benchmark](benchmark/REPORT.md)）。

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
- [使用指南](docs/usage.zh-CN.md)
- [快捷键速查](docs/keybindings.zh-CN.md)
- [常见问题](docs/faq.zh-CN.md)
- [安全与隐私](security-privacy/README.md)
- [更新日志](CHANGELOG.md)
- [支持](SUPPORT.md)
- [项目结构](#项目结构)
- [License](#license)

## 亮点

**模型只是引擎，FuXi 才是整车。** 模型单独只能回答问题；FuXi 让它成为真正
的工人 —— 推理、在你真实的代码库上行动、验证结果，并且成本可控、尽在你
掌握之中。

![FuXi 架构](docs/architecture.png)

![思考 → 行动 → 验证循环](docs/loop.png)

![智能路由](docs/routing.png)

![提升任意模型的能力](docs/elevation.png)

- **50+ 内置工具** —— 文件读/写/改、shell（`bash` / PowerShell）、ripgrep
  搜索、网页抓取、LSP 诊断、Jupyter、浏览器控制、后台任务，以及并行子智能体
  —— 全部装在一个二进制里。
- **安全护栏** —— shell 命令在执行前会经过 AST 安全分类器；细粒度权限和
  审计日志让自主执行始终处于你的掌控中。
- **持久会话与记忆** —— 会话记录持久化到磁盘；检查点支持恢复、回滚或
  分叉；空闲期"梦境"整理跨会话整合记忆；长对话自动压缩以节省 token。
- **自带密钥，或直接登录** —— 任意提供商 API Key（OpenAPI 兼容、Gemini、
  Bedrock/Vertex），或通过 FuXi OAuth 登录。
- **可扩展** —— MCP 客户端、hooks、skills、plugins 与斜杠命令，全部支持热重载。
- **永久免费** —— 单个静态二进制，无运行时依赖，个人、团队、企业均无需许可费用。
- **自动更新** —— 后台版本检查加一条 `fuxi update`，替换二进制前先做校验和验证。

---

## 与同类产品的对比

FuXi 是一个终端优先、设计上不绑定任何单一提供商的 AI 编程智能体。
能力对照基于各产品官方公开定位（2026 年中）；产品迭代很快，
请将其作为定位参考。

### 实测对比

![FuXi 与 Claude Code 实测对比](docs/headtohead.png)

两个系统各自通过原生客户端、在相同 baseline 与相同客观评分工具
（pytest + coverage）下，于 15 个微观维度与 4 个大型项目维度上进行对比。
完整方法、原始数据、环境版本、具体命令与已知局限都记录在
[`benchmark/REPORT.zh-CN.md`](benchmark/REPORT.zh-CN.md)，可供核实或自行复现。

> 坦率说明：这是一套自测的小规模任务集，并非第三方基准，且衡量的是
> **智能体循环**而非模型裸分。请把它当作一个参考数据点，而非结论性标题。

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
curl -fsSL https://fuxicode.com/install.sh | bash
```

### Windows（PowerShell）

```powershell
irm https://fuxicode.com/install.ps1 | iex
```

### Windows（CMD）

```bat
curl -fsSL https://fuxicode.com/install.cmd -o "%TEMP%\fuxi-install.cmd" && "%TEMP%\fuxi-install.cmd"
```

以上三种方式都会安装到 `~/.local/bin`（Windows 上为
`%USERPROFILE%\.local\bin`），并在尚未加入时自动加进你的**用户** `PATH`。
再次运行同一条命令即可原地升级已有安装 —— 安装和升级是同一条命令。

默认安装最新版本；也可以带参数指定具体版本，例如
`./bootstrap.sh 0.1.2` 或 `./bootstrap.ps1 0.1.2`。

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
   model:
     active: { provider: custom, id: your-model-id }
   ```

   分层 schema 支持多个提供商与按模型的设置。

   或者运行 `fuxi wizard` 进入交互式配置流程（选择提供商、输入
   base URL/密钥、选择模型、测试连接）。

配置好模型后，随时可用 `/model` 切换，用 `/config` 管理其余设置 ——
权限、hooks、skills、plugins 等一切都通过 TUI 内的斜杠命令驱动。

---

## 使用指南

> 完整的、逐步的使用指南 —— 从安装到高级特性 —— 见
> [docs/usage.zh-CN.md](docs/usage.zh-CN.md)。本节为速查参考。

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
括号粘贴用于处理大段粘贴内容。完整快捷键速查见
[docs/keybindings.md](docs/keybindings.md)。

### 更新

FuXi 会在后台检查新版本，一旦有可用更新会打印一行提示。原地更新：

```bash
fuxi update            # 最新版本
fuxi update 0.1.2      # 指定版本
```

`fuxi update` 会下载目标版本，对照已发布的 manifest 校验 SHA-256，
并原子性地替换正在运行的二进制文件 —— 不会留下安装到一半的中间状态。
可通过 `--no-update-notifier` 或 `NO_UPDATE_NOTIFIER=1` 关闭后台检查提示。

### 配置

- **配置目录：** `~/.fuxi/`（可用 `FUXI_CONFIG_DIR` 覆盖）。
- **配置文件：** `~/.fuxi/config.yaml` —— 提供商、模型、
  thinking/effort、路由偏好，以及按端点的覆盖。FuXi 运行期间修改会热加载。
  `fuxi init` 会生成初始模板，`/config` 可在 TUI 内管理设置。
- **优先级：** 环境变量 > `config.yaml` > 内置默认值。
- **项目设置：** 项目内提交的项目设置文件（权限、hooks）会按项目生效。
- **插件：** 官方插件市场位于 `fuxicode.com/plugins`。

常用环境变量：

| 变量 | 作用 |
|---|---|
| `FUXI_BASE_URL` / `FUXI_API_KEY` / `FUXI_MODEL` | OpenAPI 兼容提供商配置 |
| `FUXI_THINKING_MODE` / `FUXI_THINKING_EFFORT` | `auto\|enabled\|disabled` / `low\|medium\|high\|max` |
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

- `README.md` / `README.zh-CN.md` — 主文档（英文 / 简体中文）
- `docs/` — 演示 GIF、对比图、使用指南、快捷键速查、常见问题
- `CHANGELOG.md` — 版本发布记录
- `CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`SECURITY.md`、`SUPPORT.md` —
  社区与支持指南
- `security-privacy/` — 安全与隐私保护体系：治理章程、政策、标准、流程、
  全球合规矩阵与信任中心

---

## License

**闭源。** Copyright © 2026 FUXI。保留所有权利。
