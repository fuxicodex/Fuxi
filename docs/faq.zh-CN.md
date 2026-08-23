# 常见问题

关于 FuXi 的常见问题。安装、使用与配置详情见 [README](../README.zh-CN.md)。

## 安装

**如何安装 FuXi？**

macOS / Linux：

```bash
curl -fsSL https://releases.fuxicode.com/bootstrap.sh | bash
```

Windows（PowerShell）：

```powershell
irm https://releases.fuxicode.com/bootstrap.ps1 | iex
```

所有安装方式都会把 FuXi 放到 `~/.local/bin`（Windows 为
`%USERPROFILE%\.local\bin`），并加入你的用户 `PATH`。

**如何验证安装？**

```bash
fuxi --version
fuxi doctor      # 环境自检（配置、API Key、git、ripgrep 等）
```

**如何升级？**

重跑同一条安装命令 —— 安装与升级是同一条命令。或在会话内运行
`fuxi update`；它会在替换二进制前对照已发布的 manifest 校验 SHA-256。

**如何卸载？**

删除 `~/.local/bin/fuxi`，可选删除 `~/.fuxi` 以清除配置与状态。

## 快速开始

**首次运行需要什么？**

一个可对话的模型，两条路径可选：

1. **登录** —— `fuxi login` 用你的 FuXi 账号认证并自动开通模型。无需 API Key。
2. **自带密钥** —— 通过环境变量设置提供商 API Key，或编写
   `~/.fuxi/config.yaml`（`fuxi init` 生成初始模板）。或运行 `fuxi wizard`
   进入交互式配置流程。

**支持哪些模型提供商？**

OpenAI 兼容端点、Gemini、Bedrock、Vertex，以及其他 OpenAI 兼容提供商 ——
或通过 FuXi OAuth 登录。使用你选择的任意提供商 API Key。

**如何切换模型？**

在 TUI 内按 `Ctrl+L` 或运行 `/model`。用 `/config` 管理其余设置；一切
（权限、hooks、skills、plugins）都在 TUI 内通过斜杠命令驱动。

## 使用

**FuXi 能做什么？**

FuXi 以 思考 → 行动 → 验证 循环工作：它推理任务、用 50+ 内置工具行动
（文件编辑、shell、搜索、网页抓取等）、查看结果，并迭代直到工作被验证。

**有哪些权限模式？**

- `default` —— 敏感操作逐项提示批准
- `plan` —— 先规划再行动
- `bypassPermissions` —— 自动批准一切

在 TUI 内用 `Shift+Tab` 循环切换，或在启动时用 `--permission-mode` 指定。
`--auto` 在分类器门控检查（带熔断）下自动批准安全的工具调用。

**如何恢复过去的对话？**

- `fuxi -r <sessionId>` 恢复指定会话
- `fuxi -c` 继续当前目录下最近一次对话
- 在 TUI 内用 `/history` 或 `/resume` 浏览过去的会话/检查点

**完整的斜杠命令列表在哪里？**

在空提示符开头输入 `/` 打开命令面板，或查看 README 使用指南里的斜杠命令表。

**我的会话会保存吗？**

会。转录持久化到磁盘；检查点支持恢复、回滚或分叉。长对话自动压缩以节省
token，空闲期的"梦境"整理会跨会话整合记忆。

## 故障排查

**命令或工具被阻止 —— 为什么？**

shell 命令在执行前会经过 AST 安全分类器与规则集过滤。若某命令被意外阻止，
用 `/permissions` 查看权限规则并在 TUI 内调整。

**我发现了一个 bug，在哪里报告？**

使用 **Bug report** 模板提交 issue，附上 `fuxi --version`、你的 OS 与 shell，
以及最小复现步骤。安全问题请通过
[GitHub 安全通告](https://github.com/fuxicodex/Fuxi/security/advisories/new)
私下报告。
