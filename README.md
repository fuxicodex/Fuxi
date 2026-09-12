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

> **New to FuXi?** Jump straight to the [Quickstart](#quickstart) — it takes
> about a minute to get a working session. The full walkthrough lives in the
> [usage guide](docs/usage.md).

---

## Contents

- [Quickstart](#quickstart)
- [Highlights](#highlights)
- [How FuXi compares](#how-fuxi-compares)
- [Documentation](#documentation)
- [Evaluation & benchmarks](#evaluation--benchmarks)
- [Project layout](#project-layout)
- [License](#license)

## Quickstart

### 1. Install

macOS / Linux:

```bash
curl -fsSL https://downloads.fuxicode.com/bootstrap.sh | bash
```

Windows (PowerShell):

```powershell
irm https://downloads.fuxicode.com/bootstrap.ps1 | iex
```

Windows (CMD):

```bat
curl -fsSL https://downloads.fuxicode.com/install.cmd -o "%TEMP%\fuxi-install.cmd" && "%TEMP%\fuxi-install.cmd"
```

The installers place FuXi in `~/.local/bin` (`%USERPROFILE%\.local\bin` on
Windows) and add it to your **user** `PATH` if it isn't there already. Rerun the
same command to upgrade later — install and upgrade are the same command.

### 2. Verify

```bash
fuxi --version
fuxi doctor      # environment sanity checks (config, API key, git, ripgrep, ...)
```

### 3. Launch

```bash
fuxi
```

On first run FuXi creates its config under `~/.fuxi/`, then you register and sign
in — **a FuXi account is required to use FuXi**:

1. **Register & sign in (required)** — `fuxi login` registers or authenticates
   your FuXi account and grants access. For headless/CI use, `fuxi setup-token`
   prints a token to export as `FUXI_OAUTH_TOKEN`. Registration processes only
   minimal account data — **your code and conversations are never uploaded**
   (zero content upload).

2. **Connect a model (optional)** — sign-in alone provides access to FuXi-managed
   models. To use your own provider instead, bring your own key: set a provider
   API key via environment variable, or write `~/.fuxi/config.yaml`
   (`fuxi init` generates a starter template):

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

   Or run `fuxi wizard` for an interactive setup flow — pick a provider, enter
   the base URL and key, choose a model, and test the connection.

> **Privacy at a glance:** the account is required, the content is not. Zero
> content upload — see the
> [Security & Privacy Program](security-privacy/README.md).

### 4. Go

Type a prompt and press Enter, for example:

```text
Fix the failing tests in this repository.
```

FuXi reasons, edits files, runs commands, and verifies the result. A few tips
for your first minutes:

- `/model` — switch models any time · `/help` — browse all commands · `/exit` — quit
- Tools may ask for permission the first time they run — review with `/permissions`
- `fuxi -r <sessionId>` or `fuxi -c` resumes a past conversation; sessions are
  saved automatically

That is the whole loop. For upgrading, uninstalling, keyboard shortcuts, MCP,
and the full command-line reference, see the [usage guide](docs/usage.md).

---

## Highlights

**The model is the engine. FuXi is the vehicle.** A model alone answers
questions; FuXi turns it into a worker — reasoning, acting on your real
codebase, verifying results, and doing it affordably and under your control.

![FuXi architecture](docs/architecture.png)

### Built around the loop

- **Think → Act → Verify** — FuXi reasons about a task, acts with tools, checks
  the result, and iterates until the work is verified: a failing test fixed, a
  suite green, a PR ready.

  ![Think → Act → Verify loop](docs/loop.png)

- **Cost-aware smart routing** — every request is scored by complexity and
  routed to the right model tier: cheap models handle simple tasks, powerful
  models are reserved for hard ones, with automatic failover.

  ![Intelligent routing](docs/routing.png)

### 50+ tools, one static binary

- **Work on real codebases** — file read/write/edit, shell (`bash` /
  PowerShell), ripgrep search, web fetch, LSP diagnostics, Jupyter, browser
  use, background tasks, and parallel sub-agents — no runtime dependencies.
- **Extensible by design** — MCP client, hooks, skills, plugins, and slash
  commands, all hot-reloadable.
- **Safe by default** — shell commands pass an AST safety classifier before
  they run; fine-grained permissions and local audit logs keep autonomous work
  under your control.
- **Your work persists** — transcripts saved to disk, checkpoints to resume,
  roll back, or fork, auto-compaction of long conversations, and "dreaming"
  memory consolidation across sessions.

### Yours: key, data, and cost

- **Bring your own key, or use managed models** — a FuXi account is required to
  use FuXi; connect any OpenAI-compatible, Gemini, Bedrock, or Vertex API key, or
  use FuXi-managed models.
- **Zero content upload & local-first** — your code, prompts, and conversations
  are never uploaded to FuXi; config, credentials, sessions, and memory stay on
  your device under `~/.fuxi/`, and requests go straight to the provider you
  choose.
- **Self-updating** — a background version check and one-command `fuxi update`,
  with checksum verification before it replaces the running binary.

### The proof

The same **Think → Act → Verify** loop and smart routing let any
OpenAPI-compatible model perform above its raw benchmark — measured
head-to-head against another coding agent on a reproducible task set
([benchmark](benchmark/REPORT.md)).

![Elevating any model's capability](docs/elevation.png)

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

## Documentation

Full reference material lives under `docs/`, mirrored in 简体中文.

| Guide | What it covers |
|---|---|
| [Usage guide](docs/usage.md) | The complete walkthrough: first session, permissions & safety, sessions & memory, tools & MCP, the full command-line reference, updating, and troubleshooting |
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