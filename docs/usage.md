# FuXi Usage Guide

A complete guide to installing, configuring, and using FuXi — the terminal AI
coding agent. This document covers the full workflow, from first install to
advanced features, and is written with first-time users in mind.

> **In a hurry?** Install, launch, and start a session in minutes with the
> [Quickstart](../README.md#quickstart). Come back here as you go deeper.
>
> Companion references:
> [Keyboard shortcuts](keybindings.md) · [Environment variables](environment.md)
> · [FAQ](faq.md) · [Security & privacy](../security-privacy/README.md)

---

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [First run & configuration](#first-run--configuration)
- [Your first session](#your-first-session)
- [Permissions & safety](#permissions--safety)
- [Sessions, memory & resume](#sessions-memory--resume)
- [Tools & MCP](#tools--mcp)
- [Command-line reference](#command-line-reference)
- [Updating](#updating)
- [Troubleshooting](#troubleshooting)
- [Usage policy](#usage-policy)
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
  Bedrock/Vertex, or other OpenAI-compatible providers, or use FuXi-managed
  models after signing in.
- **Zero content upload** — FuXi never collects, stores, or retains your code,
  prompts, or conversations, and never asks you to upload them. With your own
  key the content goes straight to your provider; with FuXi-managed models it is
  transmitted only to serve that request — not retained, not used for training.
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

On first run FuXi creates its config under `~/.fuxi/`, then you register and sign
in. **A FuXi account is required to use FuXi.**

### 1. Register and sign in (required)

```bash
fuxi login
```

`fuxi login` registers or authenticates your FuXi account and grants access. Sign
out with `fuxi logout`.

For headless/CI use, `fuxi setup-token` prints a token to export as
`FUXI_OAUTH_TOKEN`.

Registration processes only minimal account data — **your code and conversations
are never collected, stored, or retained by FuXi** (zero content upload).

### 2. Connect a model (optional)

Signing in already grants access to FuXi-managed models. To use your own provider
instead, bring your own key: set a provider API key via environment variable, or
write `~/.fuxi/config.yaml` directly. `fuxi init` generates a starter template,
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
- **Plugins:** first-party plugins, hot-reloadable.

The most common environment variables:

| Variable | Purpose |
|---|---|
| `FUXI_BASE_URL` / `FUXI_API_KEY` / `FUXI_MODEL` | OpenAPI-compatible provider config |
| `ANTHROPIC_API_KEY` / `ANTHROPIC_MODEL` | Anthropic provider config |
| `FUXI_THINKING_MODE` / `FUXI_THINKING_EFFORT` | `auto\|enabled\|disabled` / `low\|medium\|high\|max` |
| `FUXI_CONFIG_DIR` | Override the config directory (default `~/.fuxi`) |
| `FUXI_DEBUG` | Set to `1` to enable debug logging |
| `NO_UPDATE_NOTIFIER` | Set to `1` to suppress the background update-check notice |
| `FUXI_TEMPERATURE` / `FUXI_TOP_P` / `FUXI_SEED` | Sampling controls |

The complete reference — including bridge/remote control, sandbox limits, and
MCP resource caps — is in [environment.md](environment.md).

---

## Your first session

Once a model is configured, type a prompt and press Enter. FuXi reasons about
the task, uses tools to act on it, and verifies the result. A typical first
request:

```text
Fix the failing tests in this repository.
```

### The basics

- **Send a message** — type your prompt and press `Enter`. Press `Ctrl+J` or
  `Shift+Enter` to insert a newline.
- **Browse commands** — type `/` at the start of an empty prompt and press
  `Enter` (or Tab-autocomplete) to see everything FuXi can do.
- **Switch models** — `/model` picks the active model at any time.
- **Get help or quit** — `/help` lists all commands; `/exit` quits.
- **Cancel** — `Esc` cancels the current operation or closes a popup.
- **Permission prompts** — the first time a tool does something sensitive, you
  are asked to approve it. See [Permissions & safety](#permissions--safety).

### Slash commands

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
model and safety guardrails. Expect a permission prompt the first time a tool
touches something sensitive; you can review and adjust everything later with
`/permissions`.

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
fuxi --allowed-tools <list>   # comma-separated allow-list
fuxi --disallowed-tools <list> # comma-separated block-list
```

### MCP servers

MCP servers are only loaded when you explicitly configure them.

```bash
fuxi --mcp-config <configs...>   # load MCP servers from JSON strings or file paths
fuxi --strict-mcp-config         # only use servers from --mcp-config
fuxi mcp                         # configure and manage MCP servers
```

---

## Command-line reference

> `fuxi --help` on your installed binary is always authoritative. The tables
> below cover the flags and commands you are most likely to use.

### Flags

| Area | Flag | Purpose |
|---|---|---|
| Model | `-m, --model <name>` | Override the model for this run |
| | `-P, --provider <type>` | Provider type: `anthropic` \| `openapi` |
| | `-b, --base-url <url>` | Override the base URL (enables the OpenAPI provider) |
| | `-k, --api-key <key>` | Override the API key for this run |
| | `--fallback-model <model>` | Fall back to this model when the default is overloaded |
| Session | `-r, --resume <sessionId>` | Resume a specific past conversation |
| | `-c, --continue` | Continue the most recent conversation in this directory |
| | `--session-id <uuid>` | Use a specific session ID (must be a valid UUID) |
| | `--fork-session` | When resuming, create a new session ID instead of reusing the original |
| | `--from-pr [value]` | Resume a session linked to a PR by number/URL |
| | `--prefill <text>` | Pre-fill the prompt input without submitting it |
| | `-d, --dir <path>` | Working directory |
| Permissions | `--permission-mode <mode>` | `default` \| `plan` \| `bypassPermissions` |
| | `--auto` | Auto-approve safe tool calls (classifier-gated, with a circuit breaker) |
| | `--dangerously-skip-permissions` | Skip all permission checks (DANGEROUS) |
| Thinking | `--thinking <mode>` | `enabled` \| `adaptive` \| `disabled` |
| | `--effort <level>` | `low` \| `medium` \| `high` \| `max` |
| | `--max-tokens <n>` | Max output tokens per API call |
| | `--max-thinking-tokens <n>` | Max thinking budget tokens |
| | `--max-budget-usd <amount>` | Maximum dollar amount to spend on API calls |
| Tools & MCP | `--tools <tools...>` | Restrict the built-in tool set (`""` = none, `default` = all, or names) |
| | `--allowed-tools` / `--disallowed-tools <list>` | Comma-separated tool allow / block lists |
| | `--mcp-config <configs...>` | Load MCP servers from JSON strings or file paths |
| | `--strict-mcp-config` | Only use MCP servers from `--mcp-config` |
| | `--plugin-dir <path>` | Load plugins from a directory for this session |
| Print | `-p, --print` | Print the response and exit (useful for pipes) |
| | `--output-format` / `--input-format <format>` | `text` / `json` / `stream-json` (with `--print`) |
| Inspect | `--status` | Print resolved provider status and exit |
| | `--config` | Print resolved configuration and exit |
| Debug | `--debug [pattern]` | Enable debug logging, optionally filtered by pattern |
| | `--verbose` | Enable verbose logging |
| | `-v, --version` / `-h, --help` | Version / full flag & command reference |

`fuxi --help` also lists system-prompt overrides (`--system-prompt`,
`--append-system-prompt`, ...), hook triggers (`--init`, `--init-only`,
`--maintenance`), swarm/agent flags (`--team`, `--agents`, `--name`, ...),
worktree flags (`--worktree`, `--tmux`), and sampling controls.

### Subcommands

| Command | What it does |
|---|---|
| `fuxi` (or `fuxi tui`) | Launch the interactive TUI |
| `fuxi login` / `fuxi logout` | Sign in to your FuXi account (stdin flow) / sign out |
| `fuxi setup-token` | Sign in and print a token to export as `FUXI_OAUTH_TOKEN` (headless/CI) |
| `fuxi wizard` | TUI setup wizard: provider, base URL, key, model, connection test |
| `fuxi init [--force]` | Generate a `~/.fuxi/config.yaml` template (auto-detects provider from env) |
| `fuxi doctor` | Run diagnostic checks on your environment |
| `fuxi verify` | Verify provider connectivity |
| `fuxi info` | Show provider and model information |
| `fuxi agents` | List configured agents grouped by source |
| `fuxi auto-mode <sub>` | Inspect auto-mode classifier rules (`defaults` \| `config` \| `critique`) |
| `fuxi proxy` | Start the smart routing proxy (Anthropic ↔ OpenAI translation) |
| `fuxi launch [args]` | Launch a proxied binary via the proxy, using your FuXi config |
| `fuxi mcp` | Configure and manage MCP servers |
| `fuxi plugin` | Manage FuXi plugins |
| `fuxi workflow` | Manage workflow definitions |
| `fuxi relay-server` | Start the relay server (auth via `FUXI_RELAY_TOKEN`) |
| `fuxi remote-control` | Run as a cloud remote-control worker (alias for `--remote-control`) |
| `fuxi update [version]` | Download and install a release (checksum-verified, atomic) |

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

## Usage policy

**You must use FuXi in accordance with the laws applicable to you** — your
country/region's law, data-protection law, and any sectoral rules that apply to
your work. FuXi's technical capability is not permission: if a use is unlawful
where you are, you must not use FuXi for it.

In short, you must not use FuXi to commit or facilitate unlawful activity, harm
children, cause harm or destruction, gain unauthorised access, violate privacy,
deceive or defraud, create illegal content, circumvent the safety mechanisms to
cause those harms, misrepresent AI output as verified professional advice, or
abuse the service.

FuXi has a **minimum age of 13**; if you are under 18, a parent or guardian must
be involved and provide consent where required. The full requirements are in the
[Usage Policy](../security-privacy/policies/ACCEPTABLE_USE.md). If you are unsure
whether a use is lawful, take advice before proceeding.

---

## Advanced

- **Smart routing** — each request is scored by complexity and routed to the
  right model tier; cheap models handle simple tasks, powerful models are
  reserved for hard ones, with automatic failover.
- **Sub-agents** — parallel agents for larger tasks; `/fork` shows fork-agent
  stats.
- **Hooks, skills & plugins** — extensible and hot-reloadable, with first-party
  plugins.
- **Remote control** — run as a cloud worker with `fuxi remote-control` or
  `--remote-control`.
- **Proxy** — `fuxi proxy` starts the smart routing proxy (Anthropic ↔ OpenAI
  translation); `fuxi launch` runs a proxied binary through it.
- **Worktrees & swarm** — `--worktree` creates a git worktree for the session;
  `--team` joins swarm coordination with teammates.
- **Multi-window** — switch between concurrent sessions without interrupting
  current work.
- **Image & voice** — paste images from the clipboard, image captioning, and
  hold-to-talk voice capture (`Ctrl+V` to paste, `Alt+V` to talk).

See [CHANGELOG.md](../CHANGELOG.md) for release-by-release details and
[keybindings.md](keybindings.md) for the complete shortcut reference.