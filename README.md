# FuXi

[English](README.md) | [简体中文](README.zh-CN.md)

> **An AI coding agent that lives in your terminal.**
> Codename **YiHuaKaiTian** — "one stroke opens the heavens."

FuXi is a fast, self-contained AI developer terminal: read code, edit files, run
commands, and drive tools from a rich TUI, with cost-aware routing across many
LLM providers and automatic failover. One static binary, no runtime
dependencies.

**Terminal-first** · **Provider-agnostic** · **Bring your own key** · **MCP client** · **Self-updating**

Homepage: **https://www.fuxicode.com**

![FuXi in action](docs/fuxi-demo.gif)

---

## Contents

- [Highlights](#highlights)
- [How FuXi compares](#how-fuxi-compares)
- [Evaluation & benchmarks](#evaluation--benchmarks)
- [Install](#install)
- [Getting started](#getting-started)
- [Usage guide](#usage-guide)
- [Project layout](#project-layout)
- [License](#license)

## Highlights

**The model is the engine. FuXi is the vehicle.** A model alone answers
questions; FuXi turns it into a worker — reasoning, acting on your real
codebase, verifying results, and doing it affordably and under your control.

- **Think → Act → Verify loop** — FuXi does not just answer. It works in a
  loop: reason about the task, act with tools (edit files, run commands,
  search code), inspect the result, and iterate until the work is done and
  verified — a failing test fixed, a suite green, a PR ready.
- **Intelligent routing** — every request is scored by complexity and routed
  to the right model tier: cheap models handle simple tasks, powerful models
  are reserved for hard ones. Automatic failover and optional primary-vs-
  fallback racing keep you working when a provider stumbles.
- **50+ built-in tools** — file read/write/edit, shell (`bash` / PowerShell),
  ripgrep search, web fetch, LSP-backed diagnostics, Jupyter, browser use via
  MCP, background tasks, and parallel **sub-agents** — all in one binary.
- **Safety guardrails** — shell commands pass an AST safety classifier and a
  rule set before execution; fine-grained permissions, audit logging, and an
  explicit permission model keep autonomous work under your control.
- **Durable sessions & memory** — transcripts persist to disk; checkpoints let
  you resume, roll back, or fork; an idle "dreaming" pass consolidates memory
  across sessions; long conversations auto-compact to save tokens.
- **Bring your own key, or log in** — use any provider API key (OpenAI-
  compatible, Gemini, Bedrock/Vertex, or other OpenAI-compatible endpoints), or
  sign in with FuXi OAuth. Data stays under your control.
- **Extensible** — MCP client, hooks, skills, plugins, and user-defined slash
  commands, all hot-reloadable.
- **Free forever** — one static binary, no runtime dependencies, no license
  cost for individuals, teams, or enterprises.
- **Self-updating** — a background version check and a one-command `fuxi
  update` keep your install current, with checksum verification before it ever
  replaces the running binary.

---

## How FuXi compares

FuXi is a terminal-first AI coding agent designed to be provider-agnostic.
Feature availability reflects each product's publicly documented positioning
as of mid-2026; details evolve quickly, so treat it as an orientation.

![FuXi vs. other AI coding agents](docs/comparison.svg)

![Positioning of AI coding agents](docs/positioning.svg)

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

## Install

### macOS / Linux

```bash
curl -fsSL https://releases.fuxicode.com/bootstrap.sh | bash
```

### Windows (PowerShell)

```powershell
irm https://releases.fuxicode.com/bootstrap.ps1 | iex
```

### Windows (CMD)

```bat
curl -fsSL https://releases.fuxicode.com/install.cmd -o "%TEMP%\fuxi-install.cmd" && "%TEMP%\fuxi-install.cmd"
```

All three install to `~/.local/bin` (`%USERPROFILE%\.local\bin` on Windows) and add
it to your **user** `PATH` if it isn't there already. Running the same command again
later upgrades an existing install in place — it's the same command for install and
upgrade.

By default they install the latest version; pin a specific one with an argument, e.g.
`./bootstrap.sh 0.1.2` or `./bootstrap.ps1 0.1.2`.

### Verify the install

```bash
fuxi --version
fuxi doctor      # environment sanity checks (config, API key, git, ripgrep, ...)
```

### Uninstall

```bash
# macOS / Linux
rm -f "$HOME/.local/bin/fuxi"
rm -rf "$HOME/.fuxi"   # optional: also drop config/state

# Windows (PowerShell)
Remove-Item -Force "$env:USERPROFILE\.local\bin\fuxi.exe"
Remove-Item -Recurse -Force "$env:USERPROFILE\.fuxi"   # optional
```

---

## Getting started

Launch the TUI:

```bash
fuxi
```

On first run FuXi creates its config under `~/.fuxi/`. You need a model to talk to,
via one of two paths:

1. **Sign in** — `fuxi login` opens a browser to authenticate with your FuXi
   account, which provisions FuXi-managed models automatically. No API key needed.
2. **Bring your own key** — set a provider API key via environment variable, or
   write `~/.fuxi/config.yaml` directly (`fuxi init` generates a starter template,
   auto-detecting a provider from whatever env vars are already set):

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

   Or run `fuxi wizard` for an interactive setup flow (pick a provider, enter the
   base URL/key, choose a model, test the connection).

Once a model is configured, pick it any time with `/model`, and manage the rest of
your settings with `/config` — everything (permissions, hooks, skills, plugins) is
driven from inside the TUI via slash commands.

---

## Usage guide

### Command-line flags

Common flags when launching `fuxi`, grouped by purpose. The complete reference
is in `fuxi --help`.

| Area | Flag | Purpose |
|---|---|---|
| Model | `-m, --model <name>` | Override the model for this run |
| | `-P, --provider <type>` | Provider type: `anthropic` \| `openapi` |
| | `-b, --base-url <url>` | Override the base URL (enables the OpenAPI provider) |
| | `-k, --api-key <key>` | Override the API key for this run |
| Session | `-r, --resume <sessionId>` | Resume a specific past conversation |
| | `-c, --continue` | Continue the most recent conversation in this directory |
| | `--session-id <uuid>` | Use a specific session ID (must be a valid UUID) |
| | `--fork-session` | When resuming, create a new session ID instead of reusing the original |
| | `--prefill <text>` | Pre-fill the prompt input with text without submitting it |
| | `-d, --dir <path>` | Working directory |
| Permissions | `--permission-mode <mode>` | `default` \| `plan` \| `bypassPermissions` |
| | `--auto` | Auto-approve safe tool calls (classifier-gated, with a circuit breaker) |
| | `--dangerously-skip-permissions` | Skip all permission checks (DANGEROUS) |
| Thinking | `--thinking <mode>` | `enabled` \| `adaptive` \| `disabled` |
| | `--effort <level>` | `low` \| `medium` \| `high` \| `max` |
| | `--max-tokens <n>` | Max output tokens per API call |
| Tools & MCP | `--tools <tools...>` | Restrict the built-in tool set (`""` = none, `default` = all, or names) |
| | `--mcp-config <configs...>` | Load MCP servers from JSON strings or file paths |
| | `--strict-mcp-config` | Only use MCP servers from `--mcp-config` |
| Inspect | `--status` | Print resolved provider status and exit |
| | `--config` | Print resolved configuration and exit |
| Debug | `--debug [pattern]` | Enable debug logging, optionally filtered by pattern |
| | `--verbose` | Enable verbose logging |
| | `-v, --version` / `-h, --help` | Version / full flag & command reference |

`fuxi --help` also lists system-prompt overrides, tool restrictions, sampling
controls, and swarm/agent flags.

### Subcommands

| Command | What it does |
|---|---|
| `fuxi` (or `fuxi tui`) | Launch the interactive TUI |
| `fuxi login` | Sign in to a FuXi account, then configure API credentials |
| `fuxi setup-token` | Sign in and print a token to export as `FUXI_OAUTH_TOKEN` (headless/CI) |
| `fuxi wizard` | TUI setup wizard: provider, base URL, key, model, connection test |
| `fuxi init [--force]` | Generate a `~/.fuxi/config.yaml` template (auto-detects provider from env) |
| `fuxi doctor` | Run diagnostic checks on your environment |
| `fuxi verify` | Verify provider connectivity |
| `fuxi info` | Show provider and model information |
| `fuxi update [version]` | Download and install a release (checksum-verified, atomic) |
| `fuxi agents` | List configured agents grouped by source |
| `fuxi proxy` | Start the smart routing proxy (protocol bridging between providers) |
| `fuxi launch [args]` | Launch a proxied binary via the proxy, using your FuXi config |
| `fuxi mcp serve` | Run FuXi itself as an MCP stdio server |
| `fuxi remote-control` | Run as a cloud remote-control worker (alias for `--remote-control`) |

### In-TUI slash commands

Type `/` and press Enter (or Tab-autocomplete) to browse all commands:

| Command | What it does |
|---|---|
| `/help`, `/commands`, `/menu` | Show or search all commands |
| `/model` | Switch the active model |
| `/config` | Open configuration |
| `/status` | Show provider status |
| `/context` | Show current context-window usage |
| `/cost`, `/usage` | Session cost / plan usage limits |
| `/compact` | Compact conversation history to free up context |
| `/clear` | Clear the conversation |
| `/history`, `/resume` | Browse or resume a past session/checkpoint |
| `/tools` | List available tools |
| `/permissions` | Show the current permission configuration |
| `/memory` | Show the project memory file |
| `/fork` | Show fork-agent stats |
| `/away` | List or show stored session away-summaries |
| `/commit` | Create a git commit |
| `/review` | Review code / create a PR |
| `/doctor` | Run diagnostic checks |
| `/copy`, `/paste` | Copy the last reply / send clipboard text as the next prompt |
| `/exit` | Quit |

**Keyboard & input:** `/` then Enter opens the command browser · `Tab`
autocompletes a slash command · `Ctrl+R` searches prompt history · `Ctrl+V` or
terminal paste pastes directly into the input · bracketed paste handles large
pastes.

### Updating

FuXi checks for new versions in the background and prints a one-line notice when
one is available. Update in place with:

```bash
fuxi update            # latest
fuxi update 0.1.2      # a specific version
```

`fuxi update` downloads the target build, verifies its SHA-256 against the
published manifest, and atomically replaces the running binary — it never leaves
you with a partially-installed version. Suppress the background check with
`--no-update-notifier` or `NO_UPDATE_NOTIFIER=1`.

### Configuration

- **Config directory:** `~/.fuxi/` (override with `FUXI_CONFIG_DIR`).
- **Config file:** `~/.fuxi/config.yaml` — provider, model, thinking/effort,
  routing preferences, and per-endpoint overrides. Changes hot-reload while
  FuXi is running. `fuxi init` generates a starter template, and `/config`
  manages settings from inside the TUI.
- **Precedence:** environment variables > `config.yaml` > built-in defaults.
- **Project settings:** a checked-in project settings file (permissions, hooks)
  is honored per-project.
- **Plugins:** first-party marketplace at `fuxicode.com/plugins`.

Key environment variables:

| Variable | Purpose |
|---|---|
| `FUXI_BASE_URL` / `FUXI_API_KEY` / `FUXI_MODEL` | OpenAPI-compatible provider config |
| `FUXI_THINKING_MODE` / `FUXI_THINKING_EFFORT` | `auto\|enabled\|disabled` / `low\|medium\|high\|max` |
| `FUXI_CONFIG_DIR` | Override the config directory (default `~/.fuxi`) |
| `FUXI_DEBUG` | Set to `1` to enable debug logging |
| `NO_UPDATE_NOTIFIER` | Set to `1` to suppress the background update-check notice |
| `FUXI_TEMPERATURE` / `FUXI_TOP_P` / `FUXI_SEED` | Sampling controls |

Run `fuxi --help` for the full environment-variable reference, including
sandbox limits and MCP resource caps.

---

## Project layout

This repository hosts FuXi's documentation, release installers, and the issue
tracker. The product source is proprietary and is not published here (see
License).

---

## License

**Proprietary.** Copyright © 2026 FUXI (Shanghai YiTai Technology Co., Ltd.). All
rights reserved.
