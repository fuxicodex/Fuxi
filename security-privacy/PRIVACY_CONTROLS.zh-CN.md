# FuXi 隐私控制

**Privacy Controls**

*最后更新：2026-09-12 · 版本 1.0 · 层级：L1 政策*

本页列出 FuXi 为你提供的隐私与网络控制项，以及如何使用它们。FuXi 在本地
运行，不收集、不存储、不保留你的代码与对话 —— 但少数功能会访问网络，本页
明确说明这些功能是什么、以及如何更改。

> 相关文档：[隐私政策](PRIVACY_POLICY.zh-CN.md) ·
> [安全白皮书](SECURITY.zh-CN.md) ·
> [环境变量](../docs/environment.zh-CN.md)

---

## 1. 始终留在本地的数据

| 数据 | 位置 | 是否上传到 FuXi |
|---|---|---|
| 代码、提示词、对话 | 你的设备 | **否** —— 绝不收集、存储或保留 |
| 提供商凭据（API Key、OAuth token） | `~/.fuxi/` | **否** |
| 会话、检查点、项目记忆 | `~/.fuxi/`、项目目录 | **否** |
| 审计日志 | `~/.fuxi/` | **否** |

**自带密钥**时，请求直达你选择的提供商；使用 **FuXi 托管模型**时，请求仅为
服务该次请求而传输，不留存、不用于训练模型。

---

## 2. 隐私设置

在 TUI 内管理隐私偏好：

```
/privacy-settings
```

（也可用 `/privacy`）。这些偏好通过 FuXi 的隐私设置处理器读写。

---

## 3. 隐私级别

FuXi 将网络行为归为三档之一：

| 级别 | 含义 |
|---|---|
| **default** | 启用遥测 —— 可能发送匿名产品使用信号以改进产品（不含代码、提示词、文件路径或命令输出） |
| **no-telemetry** | 关闭分析与遥测 |
| **essential-traffic** | 关闭全部非必要网络流量 |

---

## 4. 开关

| 设置项 | 默认 | 作用 |
|---|---|---|
| `telemetry` | 在 **default** 级别下默认开启 | 匿名使用与诊断信号。关闭后不再发送相应事件。 |
| `crash_reports` | 关闭 | 发送崩溃/错误摘要，帮助修复缺陷。 |
| `send_conversations` | **关闭** | 发送对话内容用于支持、质量或安全调查。**必须由你显式启用。** |

除非你显式启用 `send_conversations`（或另行书面同意），**FuXi 绝不会把你的
对话内容发送给任何一方用于模型训练**。

---

## 5. 环境变量与部署控制

面向 CI、企业或加固部署，以下设置生效：

| 变量 | 作用 |
|---|---|
| `FUXI_DISABLE_TELEMETRY` | 关闭分析与遥测 |
| `FUXI_DISABLE_NONESSENTIAL_TRAFFIC` | 关闭全部非必要网络流量 |
| `FUXI_ANALYTICS_MAX_EVENTS` | 限制分析事件数量上限 |
| `--no-update-notifier` / `NO_UPDATE_NOTIFIER=1` | 关闭后台更新检查 |

---

## 6. 其他网络请求

- **更新检查** —— 仅获取版本元数据，不含用户内容。可用 `--no-update-notifier`
  或 `NO_UPDATE_NOTIFIER=1` 关闭。
- **托管模型请求** —— 仅在你使用 FuXi 托管模型时发生。
- **账号认证** —— 使用 FuXi 所必需；见[认证标准](standards/AUTHENTICATION.zh-CN.md)。

---

## 7. 你可用的一站式控制

1. 密钥留在本地：凭据存于 `~/.fuxi/`；切勿粘贴到 issue 或日志中。
2. 检查设置：运行 `/privacy-settings` 查看并修改。
3. 减少流量：把级别设为 `essential-traffic`，或设置 §5 的环境变量。
4. 删除本地数据：删除配置目录
   （`rm -rf "${FUXI_CONFIG_DIR:-$HOME/.fuxi}"`）。
5. 行使权利：见[数据主体请求处理](procedures/DATA_SUBJECT_REQUEST.zh-CN.md)。

---

*本页确保保护你隐私的控制项可见、可用。*
