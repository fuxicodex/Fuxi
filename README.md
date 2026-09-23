# FuXi

[English](README.md) | [简体中文](README.zh-CN.md)

[![GitHub stars](https://img.shields.io/github/stars/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=stars)](https://github.com/fuxicodex/Fuxi/stargazers)
[![Release](https://img.shields.io/github/v/release/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=release)](https://github.com/fuxicodex/Fuxi/releases)
[![Last commit](https://img.shields.io/github/last-commit/fuxicodex/Fuxi?style=flat-square&color=0a6fe7)](https://github.com/fuxicodex/Fuxi/commits/main)
[![License](https://img.shields.io/badge/license-Proprietary-0a6fe7?style=flat-square)](LICENSE)

FuXi is a fast, self-contained **terminal AI coding agent**. It reads code, edits
files, runs commands, and drives tools from a rich TUI, with cost-aware routing
across LLM providers and automatic failover. Built in Go, it ships as one static
binary with no runtime dependencies.

**Terminal-first** · **Provider-agnostic** · **Bring your own key** · **MCP client** · **Self-updating**

Homepage: **https://www.fuxicode.com**

FuXi's roughly **2 million lines of code** were written entirely by FuXi itself.

![FuXi in action](docs/fuxi-demo.gif)

## Install

**macOS / Linux**

```bash
curl -fsSL https://downloads.fuxicode.com/bootstrap.sh | bash
```

**Windows (PowerShell)**

```powershell
irm https://downloads.fuxicode.com/bootstrap.ps1 | iex
```

**Windows (CMD)**

```bat
curl -fsSL https://downloads.fuxicode.com/install.cmd -o "%TEMP%\fuxi-install.cmd" && "%TEMP%\fuxi-install.cmd"
```

Then verify and launch:

```bash
fuxi --version
fuxi doctor    # environment sanity checks
fuxi           # start a session
```

Install and upgrade are the same command. Full options, uninstall steps, and
troubleshooting: [setup docs](docs/usage.md#installation).

## Get started

A FuXi account is required. Run `fuxi`, then:

1. **Register and sign in** — `fuxi login` (or `fuxi setup-token` for
   headless/CI). Registration processes only minimal account data.
2. **Connect a model (optional)** — sign-in gives access to FuXi-managed models;
   to use your own provider instead, set an API key via environment variable or
   `~/.fuxi/config.yaml` (`fuxi init` generates a template). Or run `fuxi wizard`.

Then type a prompt and press Enter, for example:

```text
Fix the failing tests in this repository.
```

Useful commands: `/model` switch models · `/help` browse all commands ·
`/config` open settings · `/privacy-settings` privacy controls · `/exit` quit.

Full walkthrough: [usage guide](docs/usage.md).

## Data, privacy, and retention

FuXi runs on your machine and keeps your work local.

- **By default, your code and conversations are never collected, stored, or
  retained by FuXi.** With your own key they go straight to the provider you
  choose; with FuXi-managed models they are transmitted only to serve that
  request. Conversation content is sent to FuXi only if you explicitly enable
  `send_conversations` (off by default).
- **Credentials stay in local `~/.fuxi/`** and are never uploaded.
- **Sessions, checkpoints, memory, and audit logs** live on your device and can
  be deleted at any time by removing the config directory.
- FuXi processes limited account and technical information to operate the
  service; the available analytics are disclosed and can be turned off. See
  [Privacy Controls](security-privacy/DATA_PROTECTION.md).

Full details: [Privacy Policy](security-privacy/PRIVACY_POLICY.md) ·
[Security Whitepaper](security-privacy/SECURITY.md) ·
[Terms of Service](security-privacy/TERMS_OF_SERVICE.md).

## Documentation

| Guide | What it covers |
|---|---|
| [Usage guide](docs/usage.md) | First session, permissions, sessions & memory, tools & MCP, CLI reference, troubleshooting |
| [Architecture](docs/architecture.md) | Execution base, persistence, routing, multi-window coordination, extensibility |
| [Keyboard shortcuts](docs/keybindings.md) | Terminal-UI key reference |
| [Environment variables](docs/environment.md) | Full environment-variable reference |
| [FAQ](docs/faq.md) | Common questions |
| [Benchmark report](benchmark/REPORT.md) | Reproducible evaluation methodology and results |
| [Security & privacy](security-privacy/README.md) | Privacy Policy, Security Whitepaper, Terms of Service, Usage Policy, compliance and governance |
| [Changelog](CHANGELOG.md) | Release history |
| [Support](SUPPORT.md) | Where to get help |

## Usage policy

**You must use FuXi in accordance with the laws applicable to you.** FuXi is
aimed at developers and professional users and is not directed at children under
14; users aged 14–17 require a parent or guardian.

Disallowed uses and full requirements:
[Usage Policy](security-privacy/USAGE_POLICY.md). If you are unsure
whether a use is lawful, take advice before proceeding.

## Contributing

The product source is proprietary; this repository hosts the documentation,
installers, and issue tracker, which are open to contributions. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

**Proprietary.** Copyright © 2026 FUXI. All rights reserved.
