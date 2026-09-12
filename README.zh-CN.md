# FuXi

[English](README.md) | [简体中文](README.zh-CN.md)

[![GitHub stars](https://img.shields.io/github/stars/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=stars)](https://github.com/fuxicodex/Fuxi/stargazers)
[![Release](https://img.shields.io/github/v/release/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=release)](https://github.com/fuxicodex/Fuxi/releases)
[![Last commit](https://img.shields.io/github/last-commit/fuxicodex/Fuxi?style=flat-square&color=0a6fe7)](https://github.com/fuxicodex/Fuxi/commits/main)
[![License](https://img.shields.io/badge/license-Proprietary-0a6fe7?style=flat-square)](LICENSE)

FuXi 是一个快速、自包含的**终端 AI 编程智能体**。它在丰富的 TUI 中读代码、
改文件、运行命令、驱动工具，并在多个 LLM 提供商之间进行成本感知的路由与自动
故障转移。FuXi 使用 Go 语言开发，交付为单个静态二进制文件，无运行时依赖。

**终端优先** · **不绑定提供商** · **自带密钥** · **MCP 客户端** · **自动更新**

主页：**https://www.fuxicode.com**

![FuXi 实际演示](docs/fuxi-demo.gif)

## 安装

**macOS / Linux**

```bash
curl -fsSL https://downloads.fuxicode.com/bootstrap.sh | bash
```

**Windows（PowerShell）**

```powershell
irm https://downloads.fuxicode.com/bootstrap.ps1 | iex
```

**Windows（CMD）**

```bat
curl -fsSL https://downloads.fuxicode.com/install.cmd -o "%TEMP%\fuxi-install.cmd" && "%TEMP%\fuxi-install.cmd"
```

验证并启动：

```bash
fuxi --version
fuxi doctor    # 环境自检
fuxi           # 启动会话
```

安装与升级是同一条命令。完整参数、卸载步骤与排障见
[安装文档](docs/usage.zh-CN.md#安装)。

## 快速开始

使用 FuXi 需要 FuXi 账号。运行 `fuxi`，然后：

1. **注册并登录** —— `fuxi login`（无交互/CI 用 `fuxi setup-token`）。
   注册仅处理最少的账户数据。
2. **连接模型（可选）** —— 登录后即可使用 FuXi 托管模型；若想改用自己的提供商，
   可通过环境变量或 `~/.fuxi/config.yaml` 设置 API Key（`fuxi init` 生成模板），
   或运行 `fuxi wizard`。

然后输入提示词并回车，例如：

```text
修复这个仓库里失败的测试。
```

常用命令：`/model` 切换模型 · `/help` 浏览全部命令 · `/config` 打开设置 ·
`/privacy-settings` 隐私控制 · `/exit` 退出。

完整指南见[使用指南](docs/usage.zh-CN.md)。

## 数据、隐私与保留

FuXi 在你的机器上运行，你的工作留在本地。

- **FuXi 不收集、不存储、不保留你的代码与对话。** 自带密钥时内容直达你选择的
  提供商；使用托管模型时，内容仅为服务该次请求而传输。
- **凭据存于本地 `~/.fuxi/`**，绝不上传。
- **会话、检查点、记忆与审计日志**都在你的设备上，随时可通过删除配置目录清除。
- FuXi 为运行服务会处理有限的账户与技术信息；存在的分析均已披露且可关闭。见
  [隐私控制](security-privacy/PRIVACY_CONTROLS.zh-CN.md)。

完整说明：[隐私政策](security-privacy/PRIVACY_POLICY.zh-CN.md) ·
[安全白皮书](security-privacy/SECURITY.zh-CN.md) ·
[服务条款](security-privacy/TERMS_OF_SERVICE.zh-CN.md)。

## 文档

| 文档 | 内容 |
|---|---|
| [使用指南](docs/usage.zh-CN.md) | 第一次会话、权限、会话与记忆、工具与 MCP、命令行参考、排障 |
| [架构](docs/architecture.zh-CN.md) | 执行底座、持久化、路由、多窗口协同、可扩展性 |
| [键盘快捷键](docs/keybindings.zh-CN.md) | 终端 UI 按键速查 |
| [环境变量](docs/environment.zh-CN.md) | 完整环境变量参考 |
| [常见问题](docs/faq.zh-CN.md) | 常见问题解答 |
| [基准测试报告](benchmark/REPORT.md) | 可复现的评测方法与结果 |
| [安全与隐私](security-privacy/README.md) | 隐私政策、安全白皮书、服务条款、使用政策、合规与治理 |
| [更新日志](CHANGELOG.md) | 版本发布记录 |
| [支持](SUPPORT.md) | 获取帮助 |

## 使用政策

**你必须依照适用于你的法律使用 FuXi。** FuXi 面向开发者与专业用户，不面向
不满 14 周岁的儿童；14–17 岁的用户需有父母或监护人参与。

禁止用途与完整要求见[使用政策](security-privacy/policies/ACCEPTABLE_USE.zh-CN.md)。
若不确定某用途是否合法，请先取得专业意见再行动。

## 贡献

产品源码为闭源；本仓库承载文档、安装包与 issue 追踪，欢迎贡献。见
[CONTRIBUTING.md](CONTRIBUTING.md)。

## License

**闭源。** Copyright © 2026 FUXI。保留所有权利。
