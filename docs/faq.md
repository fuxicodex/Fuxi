# FAQ

Frequently asked questions about FuXi. For installation, usage, and
configuration details, see the [README](../README.md).

## Installation

**How do I install FuXi?**

macOS / Linux:

```bash
curl -fsSL https://releases.fuxicode.com/bootstrap.sh | bash
```

Windows (PowerShell):

```powershell
irm https://releases.fuxicode.com/bootstrap.ps1 | iex
```

All installers place FuXi in `~/.local/bin` (`%USERPROFILE%\.local\bin` on
Windows) and add it to your user `PATH`.

**How do I verify the install?**

```bash
fuxi --version
fuxi doctor      # environment sanity checks (config, API key, git, ripgrep, ...)
```

**How do I upgrade?**

Rerun the same installer command — it is the same command for install and
upgrade. Or run `fuxi update` from inside a session; it verifies the SHA-256
against the published manifest before replacing the binary.

**How do I uninstall?**

Remove `~/.local/bin/fuxi` and, optionally, `~/.fuxi` for config and state.

## Getting started

**What do I need on first run?**

A model to talk to, via one of two paths:

1. **Sign in** — `fuxi login` authenticates with your FuXi account and
   provisions models automatically. No API key needed.
2. **Bring your own key** — set a provider API key via environment variable or
   write `~/.fuxi/config.yaml` (`fuxi init` generates a starter template). Or
   run `fuxi wizard` for an interactive setup flow.

**Which model providers are supported?**

OpenAI-compatible endpoints, Gemini, Bedrock, Vertex, and other
OpenAI-compatible providers — or sign in with FuXi OAuth. Use any provider API
key of your choice.

**How do I switch models?**

Inside the TUI, press `Ctrl+L` or run `/model`. Manage the rest of your
settings with `/config`; everything (permissions, hooks, skills, plugins) is
driven from inside the TUI via slash commands.

## Usage

**What can FuXi do?**

FuXi works in a Think → Act → Verify loop: it reasons about a task, acts with
50+ built-in tools (file editing, shell, search, web fetch, and more), inspects
the result, and iterates until the work is verified.

**What are the permission modes?**

- `default` — prompts for approval of sensitive actions
- `plan` — plans before acting
- `bypassPermissions` — auto-approves everything

Cycle through them with `Shift+Tab` inside the TUI, or set one at launch with
`--permission-mode`. `--auto` auto-approves safe tool calls behind a
classifier-gated check with a circuit breaker.

**How do I resume a past conversation?**

- `fuxi -r <sessionId>` resumes a specific session
- `fuxi -c` continues the most recent conversation in the current directory
- Inside the TUI, `/history` or `/resume` browse past sessions/checkpoints

**Where is the full list of slash commands?**

Type `/` at the start of an empty prompt to open the command palette, or see
the slash-command table in the README's usage guide.

**Are my sessions saved?**

Yes. Transcripts persist to disk; checkpoints let you resume, roll back, or
fork. Long conversations auto-compact to save tokens, and an idle "dreaming"
pass consolidates memory across sessions.

## Troubleshooting

**A command or tool is blocked — why?**

Shell commands pass an AST safety classifier and a rule set before execution.
If something is blocked unexpectedly, review the permission rules with
`/permissions` and adjust them in the TUI.

**I think I found a bug. Where do I report it?**

Open an issue using the **Bug report** template, and include `fuxi --version`,
your OS and shell, and a minimal reproduction. For security issues, report
privately via [GitHub security advisories](https://github.com/fuxicodex/Fuxi/security/advisories/new).
