# FuXi

[English](README.md) | [简体中文](README.zh-CN.md)

[![GitHub stars](https://img.shields.io/github/stars/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=stars)](https://github.com/fuxicodex/Fuxi/stargazers)
[![Release](https://img.shields.io/github/v/release/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=release)](https://github.com/fuxicodex/Fuxi/releases)
[![Last commit](https://img.shields.io/github/last-commit/fuxicodex/Fuxi?style=flat-square&color=0a6fe7)](https://github.com/fuxicodex/Fuxi/commits/main)
[![License](https://img.shields.io/badge/license-Proprietary-0a6fe7?style=flat-square)](LICENSE)

> **An AI coding agent that lives in your terminal.**

FuXi is a fast, self-contained **terminal AI coding agent** — read code, edit
files, run commands, and drive tools from a rich TUI, with cost-aware routing
across LLM providers and automatic failover. Built in Go, it ships as one
static binary with no runtime dependencies. Think of it as a provider-agnostic
alternative to Claude Code: bring any OpenAI-compatible model and get an
agentic Think → Act → Verify loop on top of it.

**Terminal-first** · **Provider-agnostic** · **Bring your own key** · **MCP client** · **Self-updating**

Homepage: **https://www.fuxicode.com**

![FuXi in action](docs/fuxi-demo.gif)

---

## Contents

- [Highlights](#highlights)
- [How FuXi compares](#how-fuxi-compares)
- [Install](#install)
- [Getting started](#getting-started)
- [Documentation](#documentation)
- [Evaluation & benchmarks](#evaluation--benchmarks)
- [Project layout](#project-layout)
- [License](#license)

## Highlights

**The model is the engine. FuXi is the vehicle.** A model alone answers
questions; FuXi turns it into a worker — reasoning, acting on your real
codebase, verifying results, and doing it affordably and under your control.

![FuXi architecture](docs/architecture.png)

![Think → Act → Verify loop](docs/loop.png)

![Intelligent routing](docs/routing.png)

![Elevating any model's capability](docs/elevation.png)

- **50+ built-in tools** — file read/write/edit, shell (`bash` / PowerShell),
  ripgrep search, web fetch, LSP diagnostics, Jupyter, browser use, background
  tasks, and parallel sub-agents — all in one binary.
- **Safety guardrails** — shell commands pass an AST safety classifier before
  execution; fine-grained permissions and audit logging keep autonomous work
  under your control.
- **Durable sessions & memory** — transcripts persist to disk; checkpoints let
  you resume, roll back, or fork; idle "dreaming" consolidates memory across
  sessions; long conversations auto-compact to save tokens.
- **Bring your own key, or log in** — any provider API key (OpenAPI-compatible,
  Gemini, Bedrock/Vertex), or sign in with FuXi OAuth.
- **Extensible** — MCP client, hooks, skills, plugins, and slash commands, all
  hot-reloadable.
- **Free forever** — one static binary, no runtime dependencies, no license
  cost for individuals, teams, or enterprises.
- **Self-updating** — a background version check and one-command `fuxi update`,
  with checksum verification before it replaces the running binary.

Its agentic **Think → Act → Verify** loop and intelligent routing let any
OpenAPI-compatible model perform above its raw benchmark — verified against
another coding agent on a reproducible task set (see
[benchmark](benchmark/REPORT.md)).

---

## How FuXi compares

FuXi is a terminal-first AI coding agent designed to be provider-agnostic.
Feature availability reflects each product's publicly documented positioning
as of mid-2026; details evolve quickly, so treat it as an orientation.

### Measured head-to-head

![FuXi vs Claude Code head-to-head](docs/headtohead.png)

Both systems were driven through their own native clients, on identical
baselines and the same objective scorer (pytest + coverage), across 15 micro
dimensions and 4 large-project dimensions. Full methodology, raw results,
environment versions, exact commands, and known limitations are in
[`benchmark/REPORT.md`](benchmark/REPORT.md) so you can verify or re-run it.

> An honest caveat: this is a small, self-run task set — not a third-party
> benchmark — and it measures the *agent loop*, not raw model scores. Treat it
> as a data point, not a headline.

---

## Install

### macOS / Linux

```bash
curl -fsSL https://downloads.fuxicode.com/bootstrap.sh | bash
```

### Windows (PowerShell)

```powershell
irm https://downloads.fuxicode.com/bootstrap.ps1 | iex
```

### Windows (CMD)

```bat
curl -fsSL https://downloads.fuxicode.com/install.cmd -o "%TEMP%\fuxi-install.cmd" && "%TEMP%\fuxi-install.cmd"
```

All three install to `~/.local/bin` (`%USERPROFILE%\.local\bin` on Windows) and
add it to your **user** `PATH` if it isn't there already. Rerun the same command
to upgrade in place — install and upgrade are the same command. By default they
install the latest version; pin a specific one with an argument, e.g.
`./bootstrap.sh 0.1.2` or `./bootstrap.ps1 0.1.2`.

### Verify the install

```bash
fuxi --version
fuxi doctor      # environment sanity checks (config, API key, git, ripgrep, ...)
```

For uninstall instructions, see the [usage guide](docs/usage.md#installation).

---

## Getting started

Launch the TUI:

```bash
fuxi
```

On first run FuXi creates its config under `~/.fuxi/`. You need a model to talk
to, via one of two paths:

1. **Sign in** — `fuxi login` authenticates with your FuXi account, which
   provisions FuXi-managed models automatically. No API key needed. For
   headless/CI use, `fuxi setup-token` prints a token to export as
   `FUXI_OAUTH_TOKEN`.
2. **Bring your own key** — set a provider API key via environment variable, or
   write `~/.fuxi/config.yaml` directly (`fuxi init` generates a starter
   template, auto-detecting a provider from whatever env vars are already set):

   ```yaml
   provider: openapi
   base_url: https://your-endpoint/v1
   api_key: <your-key>       # or export FUXI_API_KEY instead
   model: your-model
   ```

   Managing several providers/models instead of one? Use the layered schema — a
   `providers:` catalog plus a `model:` selection layer:

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

   The layered schema supports multiple providers and per-model settings.

   Or run `fuxi wizard` for an interactive setup flow — pick a provider, enter
   the base URL and key, choose a model, and test the connection.

Once a model is configured, pick it any time with `/model`, and manage the rest
of your settings with `/config` — everything (permissions, hooks, skills,
plugins) is driven from inside the TUI via slash commands.

---

## Documentation

| Guide | What it covers |
|---|---|
| [Usage guide](docs/usage.md) | The complete walkthrough: configuration, the TUI, permissions & safety, sessions & memory, tools & MCP, the full command-line reference, updating, and troubleshooting |
| [Keyboard shortcuts](docs/keybindings.md) | Terminal-UI key reference |
| [Environment variables](docs/environment.md) | Full environment-variable reference, including bridge/remote control, sandbox limits, and MCP resource caps |
| [FAQ](docs/faq.md) | Answers to common questions |
| [Security & privacy](security-privacy/README.md) | Governance charter, policies, standards, procedures, global compliance matrix, and trust center |
| [Changelog](CHANGELOG.md) | Release history |
| [Support](SUPPORT.md) | Where to get help and how to report problems |

> Tip: run `fuxi --help` on your installed binary for the always-authoritative
> flag, command, and environment-variable reference.

---

## Evaluation & benchmarks

FuXi is built to be measured honestly. It currently ships without a published
score on third-party benchmarks (e.g. SWE-bench, Terminal-Bench, or the Aider
polyglot benchmark). We prefer reproducible, self-verifiable evaluation over
headline numbers — so here is how to evaluate FuXi yourself, on your own work.

**A practical evaluation checklist**

1. **Install & self-check** — after installing, run `fuxi doctor` to verify your
   environment (config, API key, git, ripgrep) and `fuxi verify` to confirm the
   provider connection. A clean bill here is the baseline.
2. **Reproduce a real task** — pick a failing test in one of your own projects
   and let FuXi fix it; then extend the module and re-run the suite (the demo
   above shows exactly this flow). Repeat across a handful of daily tasks:
   code review, commits, PRs, refactors.
3. **Compare side by side** — run the identical task, model, and context through
   another tool and compare: correctness, tool coverage, cost, and iteration
   time. Judging on the same ground keeps the comparison fair.

FuXi exposes everything needed for that comparison — `/cost`, `/usage`,
`/context`, and `/status` inside the TUI — and ships its own environment
self-check (`fuxi doctor`). Benchmarks that are published in the future will
be linked from this section.

---

## Project layout

This repository hosts FuXi's documentation, release installers, and the issue
tracker. The product source is proprietary and is not published here (see
License).

- `README.md` / `README.zh-CN.md` — the main documentation (English / 简体中文)
- `docs/` — demo GIF, comparison graphics, usage guide, keyboard reference,
  environment-variable reference, and FAQ
- `security-privacy/` — the Security & Privacy Program: governance charter,
  policies, standards, procedures, global compliance matrix, and trust center
- `benchmark/` — reproducible evaluation methodology and results
- `CHANGELOG.md` — release history
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md` —
  community and support guides

---

## License

**Proprietary.** Copyright © 2026 FUXI. All
rights reserved.