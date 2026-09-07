# 环境变量

FuXi 按以下优先级解析配置：环境变量 > `~/.fuxi/config.yaml` > 内置默认值。
本页镜像 `fuxi --help` 的完整 `Environment` 章节，让安全评审或部署时最关心的
旋钮——远程控制、bash 沙箱与 MCP 资源上限——在此可见、可搜索。以你安装的
二进制上运行 `fuxi --help` 的输出为准。

## 提供商与凭据

| 变量 | 作用 |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic API 密钥 |
| `ANTHROPIC_MODEL` | Anthropic 提供商使用的模型名（默认 `claude-sonnet-4-6`） |
| `FUXI_BASE_URL` | OpenAPI 兼容基础 URL（如 `https://api.openai.com/v1`） |
| `FUXI_API_KEY` | OpenAPI 兼容提供商的 API 密钥 |
| `FUXI_MODEL` | OpenAPI 兼容提供商的模型名 |

## 推理（Reasoning）

| 变量 | 作用 |
|---|---|
| `FUXI_THINKING_MODE` | 思考模式：`auto` / `enabled` / `disabled` |
| `FUXI_THINKING_EFFORT` | 思考力度：`low` / `medium` / `high` / `max` |
| `FUXI_THINKING_STRATEGY` | 思考策略：`auto` / `native` / `prompt_inject` / `two_phase` |

## 配置与诊断

| 变量 | 作用 |
|---|---|
| `FUXI_CONFIG_DIR` | 覆盖配置目录（默认 `~/.fuxi`） |
| `FUXI_DEBUG` | 设为 `1` 开启调试日志 |

## 桥接 / 远程控制

| 变量 | 作用 |
|---|---|
| `FUXI_ENV_PROFILE` | 后端环境选择：`test` / `prod` |
| `FUXI_ENVIRONMENT_ID` | 已注册的环境 ID（自动保存到 `~/.fuxi/bridge.env`） |
| `FUXI_ENVIRONMENT_SECRET` | 用于任务轮询的环境密钥 |
| `FUXI_BRIDGE_TOKEN` | 用于桥接注册的 OAuth 访问令牌 |
| `FUXI_MAX_SESSIONS` | 最大并发远程会话数（默认 `32`） |
| `FUXI_DISABLE_BRIDGE` | 设为 `1` 关闭远程控制模式 |

## 功能开关

| 变量 | 作用 |
|---|---|
| `FUXI_FORK_MAX_CONCURRENCY` | 最大并发 fork agent 数（int，默认 `4`） |
| `FUXI_DISABLE_TOOL_USAGE` | 设为 `1` 关闭工具使用记录的持久化 |
| `FUXI_DISABLE_AWAY_SUMMARY` | 设为 `1` 关闭会话结束的 away 摘要持久化 |
| `FUXI_INLINE` | 设为 `1` 强制使用内联仪表盘作为回退界面 |
| `FUXI_INK` | 空操作（`1`）——Ink 已是默认主界面 |

## 采样控制

| 变量 | 作用 |
|---|---|
| `FUXI_TEMPERATURE` | 采样温度（0.0–2.0） |
| `FUXI_TOP_P` | Top-p 核采样（0.0–1.0） |
| `FUXI_SEED` | 可复现的采样种子（正整数） |

## Bash 沙箱（macOS）

| 变量 | 作用 |
|---|---|
| `FUXI_BASH_ALLOW_NETWORK` | 设为 `1` 允许 bash 工具访问网络 |
| `FUXI_BASH_MEM_LIMIT_MB` | bash 进程内存上限（MB） |

## MCP 资源上限

| 变量 | 作用 |
|---|---|
| `FUXI_MCP_MEM_LIMIT_MB` | MCP 服务器内存上限（MB） |
| `FUXI_MCP_CPU_LIMIT_SEC` | MCP 服务器 CPU 时间上限（秒） |

## 在参数文档中列出的环境变量

以下变量与对应参数一同说明、同样生效：

| 变量 | 适用场景 |
|---|---|
| `NO_UPDATE_NOTIFIER` | 关闭后台更新检查（`--no-update-notifier`） |
| `FUXI_TEAM_NAME` | 集群（swarm）团队名（`--team`） |
| `FUXI_OAUTH_TOKEN` | `fuxi setup-token` 输出的令牌，用于 headless/CI 认证 |
| `FUXI_RELAY_TOKEN` | `fuxi relay-server` 的鉴权令牌 |
