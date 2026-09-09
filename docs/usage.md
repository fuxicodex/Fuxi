# FuXi Usage Guide

A complete guide to installing, configuring, and using FuXi — the terminal AI
coding agent. This document covers the full workflow, from first install to
advanced features. It is written from public, user-facing behavior only.

> Companion references:
> [Keyboard shortcuts](keybindings.md) · [FAQ](faq.md) ·
> [Security & privacy](../security-privacy/README.md)

---

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [First run & configuration](#first-run--configuration)
- [The TUI](#the-tui)
- [Permissions & safety](#permissions--safety)
- [Sessions, memory & resume](#sessions-memory--resume)
- [Tools & MCP](#tools--mcp)
- [Command-line reference](#command-line-reference)
- [Updating](#updating)
- [Troubleshooting](#troubleshooting)
- [Advanced](#advanced)

---

## Overview

FuXi works in a **Think → Act → Verify** loop: it reasons about a task, acts
with 50+ built-in tools (file editing, shell, search, web fetch, and more),
inspects the result, and iterates until the work is verified — a failing test
fixed, a suite green, a PR ready.

Key properties:

- **Terminal-first** — a rich TUI that runs in your terminal.
- **Provider-agnostic** — use any OpenAI-compatible endpoint, Gemini,
  Bedrock/Vertex, or other OpenAI-compatible providers, or sign in with FuXi
  OAuth.
- **Bring your own key** — your code and prompts go directly to the provider
  you choose; FuXi does not sit in between.
- **Local-first** — config, credentials, sessions, and memory live on your
  device under `~/.fuxi/` by default.
- **One static binary** — no runtime dependencies.

---

## Installation

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

All installers place FuXi in `~/.local/bin` (`%USERPROFILE%\.local\bin` on
Windows) and add it to your **user** `PATH` if it isn't there already.

### Verify the install

```bash
fuxi --version
fuxi doctor      # environment sanity checks (config, API key, git, ripgrep, ...)
```

### Upgrade

Rerun the same installer command — install and upgrade are the same command. Or
run `fuxi update` from inside a session (see [Updating](#updating)).

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

## First run & configuration

Launch the TUI:

```bash
fuxi
```

On first run FuXi creates its config under `~/.fuxi/`. You need a model to talk
to, via one of two paths:

### 1. Sign in

```bash
fuxi login
```

`fuxi login` opens a browser to authenticate with your FuXi account, which
provisions FuXi-managed models automatically. No API key needed.

For headless/CI use, `fuxi setup-token` prints a token to export as
`FUXI_OAUTH_TOKEN`.

### 2. Bring your own key

Set a provider API key via environment variable, or write
`~/.fuxi/config.yaml` directly. `fuxi init` generates a starter template,
auto-detecting a provider from the environment variables already set:

```yaml
provider: openapi
base_url: https://your-endpoint/v1
api_key: <your-key>       # or export FUXI_API_KEY instead
model: your-model
```

To manage several providers/models, use the layered schema — a `providers:`
catalog plus a `model:` selection layer:

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

Or run the interactive wizard:

```bash
fuxi wizard
```

The wizard walks through provider, base URL, key, model, and a connection test.

### Configuration reference

- **Config directory:** `~/.fuxi/` (override with `FUXI_CONFIG_DIR`).
- **Config file:** `~/.fuxi/config.yaml` — provider, model, thinking/effort,
  routing preferences, and per-endpoint overrides. Changes hot-reload while
  FuXi is running.
- **Precedence:** environment variables > `config.yaml` > built-in defaults.
- **Project settings:** a checked-in project settings file (permissions, hooks)
  is honored per-project.
- **Plugins:** first-party marketplace at `fuxicode.com/plugins`.

Common environment variables:

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

## The TUI

Type your prompt and press Enter. FuXi reasons, acts with tools, and verifies.

### Slash commands

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

### Keyboard shortcuts

`/` then Enter opens the command browser · `Tab` autocompletes a slash command ·
`Ctrl+R` searches prompt history · `Ctrl+V` or terminal paste pastes directly
into the input. The full reference is in [keybindings.md](keybindings.md).

---

## Permissions & safety

FuXi can edit files and run shell commands, so it ships an explicit permission
model and safety guardrails.

### Permission modes

| Mode | Behavior |
|---|---|
| `default` | Prompts for approval of sensitive actions |
| `plan` | Plans before acting; no changes are made |
| `bypassPermissions` | Auto-approves everything |

Cycle through modes with `Shift+Tab` inside the TUI, or set one at launch with
`--permission-mode <mode>`.

`--auto` auto-approves only tool calls the safety classifier deems safe, gated
behind a circuit breaker. `--dangerously-skip-permissions` skips **all**
permission checks — use it only in fully trusted, isolated environments, at
your own risk.

### How command safety works

Shell commands (`bash` / PowerShell) pass an AST safety classifier and a rule
set before execution. Every executed action is recorded in local audit logs for
review. Manage the rules with `/permissions`.

See the [Security Whitepaper](../security-privacy/SECURITY.md) for the full
threat model and safeguards.

---

## Sessions, memory & resume

- **Transcripts persist to disk** — conversations are saved locally.
- **Checkpoints** let you resume, roll back, or fork a session.
- **Auto-compact** — long conversations compact automatically to save tokens.
- **Dreaming** — an idle pass consolidates memory across sessions.

Resume from the command line:

```bash
fuxi -r <sessionId>    # resume a specific session
fuxi -c                # continue the most recent conversation in this directory
```

Or inside the TUI with `/history` or `/resume`. Use `/memory` to view the
project memory file.

---

## Tools & MCP

FuXi ships 50+ built-in tools — file read/write/edit, shell (`bash` /
PowerShell), ripgrep search, web fetch, LSP-backed diagnostics, Jupyter,
browser use via MCP, background tasks, and parallel sub-agents.

### Restricting tools

```bash
fuxi --tools ""               # no tools
fuxi --tools default          # all built-in tools
fuxi --tools <name1> <name2>  # a specific subset
```

### MCP servers

```bash
fuxi --mcp-config <configs...>   # load MCP servers from JSON strings or file paths
fuxi --strict-mcp-config         # only use servers from --mcp-config
```

MCP servers are only loaded when you explicitly configure them.

---

## Command-line reference

### Flags

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
| | `--prefill <text>` | Pre-fill the prompt input without submitting it |
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

---

## Updating

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

---

## Troubleshooting

### Environment self-checks

```bash
fuxi doctor     # config, API key, git, ripgrep, ...
fuxi verify     # provider connectivity
```

### A command or tool is blocked

Shell commands pass an AST safety classifier and a rule set before execution.
If something is blocked unexpectedly, review the rules with `/permissions` and
adjust them in the TUI.

### Reporting bugs

Open an issue using the **Bug report** template, including `fuxi --version`,
your OS/shell/terminal, and a minimal reproduction.

### Reporting security issues

Report privately via
[GitHub security advisories](https://github.com/fuxicodex/Fuxi/security/advisories/new).
Do **not** open a public issue.

---

## Advanced

- **Smart routing** — each request is scored by complexity and routed to the
  right model tier; cheap models handle simple tasks, powerful models are
  reserved for hard ones, with automatic failover.
- **Sub-agents** — parallel agents for larger tasks; `/fork` shows fork-agent
  stats.
- **Hooks, skills & plugins** — extensible and hot-reloadable; first-party
  marketplace at `fuxicode.com/plugins`.
- **Remote control** — run as a cloud worker with `fuxi remote-control`.
- **Proxy** — `fuxi proxy` starts the smart routing proxy (protocol bridging
  between providers).
- **Multi-window** — switch between concurrent sessions without interrupting
  current work.
- **Image & voice** — paste images from the clipboard, image captioning, and
  hold-to-talk voice capture.

See [CHANGELOG.md](../CHANGELOG.md) for release-by-release details and
[keybindings.md](keybindings.md) for the complete shortcut reference.
