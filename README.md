# FuXi

[English](README.md) | [简体中文](README.zh-CN.md)

> **An AI coding agent that lives in your terminal.**
> Codename **YiHuaKaiTian** — "one stroke opens the heavens."

FuXi is a fast, self-contained AI developer terminal — a coding agent you drive
from a rich TUI. It reads your codebase, edits files, runs commands, drives tools,
and routes every request across multiple LLM providers with cost-aware routing and
automatic failover. It ships as a single static binary with no runtime
dependencies.

Homepage: **https://www.fuxicode.com**

![FuXi in action](docs/fuxi-demo.gif)

---

## Contents

- [Highlights](#highlights)
- [How FuXi compares](#how-fuxi-compares)
- [Install](#install)
- [Getting started](#getting-started)
- [Usage guide](#usage-guide)
- [Project layout](#project-layout)
- [License](#license)

## Highlights

- **Multi-LLM routing** — one agent, many providers. First-class support for:
  - **Anthropic** (native Messages API) and Anthropic on **AWS Bedrock** / **Google Vertex**
  - **OpenAI-compatible** endpoints (OpenAI, **Azure OpenAI**, and any OpenAI-style API)
  - **Google Gemini**
  - Popular open/China-hosted models via OpenAI-compatible endpoints — **GLM **, **DeepSeek**, **Qwen**, **Hunyuan**, **Doubao**, **Ernie**, **Grok (xAI)**, and more
- **Intelligence layer** — cost-aware routing, automatic **failover** to a healthy
  provider, optional **racing** of primary vs. fallback, and role-based model tiers
  (fast / primary / reasoning) resolved from your config.
- **A deep tool suite** — file read/edit/write, shell (`bash` / PowerShell) with a
  safety classifier, web fetch, code search, LSP-backed diagnostics, Jupyter
  notebooks, computer/browser use via MCP, background tasks, and parallel
  **sub-agents**.
- **MCP client** — connect any Model Context Protocol server (stdio, HTTP, or
  WebSocket) and its tools become available to the agent.
- **Extensible** — hooks, skills, plugins, and user-defined slash commands.
- **Durable sessions** — persistent transcripts, checkpoints/resume, an idle
  "dreaming" memory, and automatic context compaction for long conversations.
- **Bring your own key, or log in** — use a provider API key, or sign in with FuXi
  OAuth. Keys are never required for the FuXi-managed path.
- **Self-updating** — a background version check and a one-command `fuxi update`
  keep your install current, with checksum verification before it ever replaces
  the running binary.

---

## How FuXi compares

FuXi is a terminal-first AI coding agent designed to be provider-agnostic. The
table below reflects each product's publicly documented positioning and the
features FuXi ships today; details evolve quickly, so treat it as an orientation
rather than a specification.

| | FuXi | Claude Code | GitHub Copilot CLI | Cursor | Aider |
|---|---|---|---|---|---|
| Terminal-first CLI / TUI | ✓ | ✓ | ✓ | ✗ (IDE-based) | ✓ |
| Multi-provider support | ✓ | ✗ (Anthropic-only) | ✗ (Copilot plan) | ✓ | ✓ |
| Bring your own API key | ✓ | ✓ | ✗ (subscription) | ✓ | ✓ |
| Cost-aware routing & failover | ✓ | ✗ | ✗ | ✗ | ✗ |
| MCP client | ✓ | ✓ | ✗ | ✓ | ✗ |
| Parallel sub-agents | ✓ | ✓ | ✗ | ✓ | ✗ |
| Durable sessions & checkpoints | ✓ | ✓ | ✗ | ✓ | ✗ |
| Single static binary, no runtime deps | ✓ | ✗ (Node) | ✗ (Node) | ✗ (IDE app) | ✗ (Python) |

```mermaid
quadrantChart
    title AI Coding Agents — Positioning
    x-axis "Single provider" --> "Multi-provider"
    y-axis "IDE-first" --> "Terminal-first"
    quadrant-1 "Terminal · Multi-provider"
    quadrant-2 "Terminal · Single provider"
    quadrant-3 "IDE · Single provider"
    quadrant-4 "IDE · Multi-provider"
    "FuXi": [0.9, 0.92]
    "Aider": [0.8, 0.75]
    "Claude Code": [0.25, 0.85]
    "GitHub Copilot CLI": [0.15, 0.7]
    "Cursor": [0.7, 0.12]
```

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
`./bootstrap.sh 2.202.194` or `./bootstrap.ps1 2.202.194`.

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
   model: glm-4.6
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
         - id: deepseek-v4-pro-260425
           model_canonical_name: deepseek-v4-pro   # optional: for capability lookup
   model:
     active: { provider: custom, id: deepseek-v4-pro-260425 }
   ```

   See `config.full.example.yaml` for the full layered schema (multiple providers,
   per-model capability overrides, routing roles).

   Or run `fuxi wizard` for an interactive setup flow (pick a provider, enter the
   base URL/key, choose a model, test the connection).

Once a model is configured, pick it any time with `/model`, and manage the rest of
your settings with `/config` — everything (permissions, hooks, skills, plugins) is
driven from inside the TUI via slash commands.

---

## Usage guide

### Command-line flags

The most commonly used flags when launching `fuxi`:

| Flag | Purpose |
|---|---|
| `-m, --model <name>` | Override the model for this run |
| `-k, --api-key <key>` | Override the API key for this run |
| `-b, --base-url <url>` | Override the base URL (enables the OpenAPI provider) |
| `-P, --provider <type>` | Provider type: `anthropic` \| `openapi` |
| `-r, --resume <sessionId>` | Resume a specific past conversation |
| `-c, --continue` | Continue the most recent conversation in this directory |
| `-d, --dir <path>` | Working directory |
| `--permission-mode <mode>` | `default` \| `plan` \| `bypassPermissions` |
| `--auto` | Auto-approve safe tool calls (classifier-gated, with a circuit breaker) |
| `--dangerously-skip-permissions` | Skip all permission checks (use with care) |
| `--worktree` | Create a git worktree for this session |
| `--thinking <mode>` | `enabled` \| `adaptive` \| `disabled` |
| `--mcp-config <configs...>` | Load MCP servers from JSON strings or file paths |
| `--status` | Print resolved provider status and exit |
| `--config` | Print resolved configuration and exit |
| `--debug [pattern]` | Enable debug logging, optionally filtered by tag |
| `-v, --version` / `-h, --help` | Version / full flag & command reference |

Run `fuxi --help` for the complete list (there are many more — sampling controls,
tool restrictions, system-prompt overrides, hook triggers, and swarm/agent flags).

### Subcommands

| Command | What it does |
|---|---|
| `fuxi` | Launch the interactive TUI (same as `fuxi tui`) |
| `fuxi login` | Sign in to a FuXi account and configure credentials |
| `fuxi setup-token` | Sign in and print a token for `FUXI_OAUTH_TOKEN` (headless/CI) |
| `fuxi wizard` | Interactive setup wizard: provider, base URL, key, model, connection test |
| `fuxi init [--force]` | Generate a `~/.fuxi/config.yaml` template |
| `fuxi doctor` | Diagnose your environment (config, key, git, ripgrep, env overrides) |
| `fuxi verify` | Verify connectivity to the configured provider |
| `fuxi info` | Show resolved provider and model information |
| `fuxi update [version]` | Download, checksum-verify, and install a new version |
| `fuxi agents` | List configured agents grouped by source |
| `fuxi proxy` | Start the local Anthropic↔OpenAI smart-routing proxy |
| `fuxi launch [args]` | Launch another tool through the proxy, using your FuXi config |
| `fuxi mcp serve` | Run FuXi itself as an MCP stdio server |
| `fuxi remote-control` | Run as a cloud remote-control worker (alias for `--remote-control`) |

### In-TUI slash commands

Type `/` and press Enter (or Tab-autocomplete) to browse all commands. The
essentials:

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
| `/fork` | Show sub-agent (fork) stats |
| `/commit` | Create a git commit |
| `/review` | Review code / open a PR |
| `/doctor` | Run diagnostic checks |
| `/copy`, `/paste` | Copy the last reply / send clipboard text as the next prompt |
| `/exit` | Quit |

**Keyboard:** `/` then Enter opens the command browser · `Tab` autocompletes a slash
command · `Ctrl+R` searches prompt history · terminal paste / bracketed paste is
supported for large pastes.

### Updating

FuXi checks for new versions in the background and prints a one-line notice when
one is available. Update in place with:

```bash
fuxi update            # latest
fuxi update 2.203.0    # a specific version
```

`fuxi update` downloads the target build, verifies its SHA-256 against the
published manifest, and atomically replaces the running binary — it never leaves
you with a partially-installed version. Suppress the background check with
`--no-update-notifier` or `NO_UPDATE_NOTIFIER=1`.

### Configuration

- **Config directory:** `~/.fuxi/` (override with `FUXI_CONFIG_DIR`).
- **Config file:** `~/.fuxi/config.yaml` — provider, model, thinking/effort,
  intelligence routing, redaction, and per-endpoint capability overrides. Changes
  hot-reload while FuXi is running. See `config.full.example.yaml` in this repo for
  every available field with inline documentation.
- **Precedence:** environment variables > `config.yaml` > built-in defaults.
- **Project settings:** a checked-in `.claude/settings.json` (permissions, hooks)
  is honored per-project.
- **Plugins:** first-party marketplace at `fuxicode.com/plugins`.

Key environment variables:

| Variable | Purpose |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `FUXI_BASE_URL` / `FUXI_API_KEY` / `FUXI_MODEL` | OpenAPI-compatible provider config |
| `ANTHROPIC_MODEL` | Model name for the Anthropic provider |
| `FUXI_THINKING_MODE` / `FUXI_THINKING_EFFORT` | `auto\|enabled\|disabled` / `low\|medium\|high\|max` |
| `FUXI_CONFIG_DIR` | Override the config directory (default `~/.fuxi`) |
| `NO_UPDATE_NOTIFIER` | Set to `1` to suppress the background update-check notice (same as `--no-update-notifier`) |
| `FUXI_TEMPERATURE` / `FUXI_TOP_P` / `FUXI_SEED` | Sampling controls |

Run `fuxi --help` for the full environment-variable reference, including bridge/
remote-control, sandbox limits, and MCP resource caps.

---

## Project layout

This repository hosts FuXi's documentation, release installers, and the issue
tracker. The product source is proprietary and is not published here (see
License).

---

## License

**Proprietary.** Copyright © 2026 FUXI (Shanghai YiTai Technology Co., Ltd.). All
rights reserved.
