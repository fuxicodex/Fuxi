# FuXi Architecture

*Last updated: 2026-09-12 · Version 1.0*

This page describes how FuXi is built: the execution base that lets the model act,
the persistence engine that keeps long work alive, the routing layer that chooses
models, and the multi-window and extensibility systems. It covers the product
dimensions that the [README](../README.md) summarizes.

> Related: [Usage guide](usage.md) · [Security Whitepaper](../security-privacy/SECURITY.md)
> · [Privacy Controls](../security-privacy/PRIVACY_CONTROLS.md)

---

## 1. Execution base: the model acts on your real environment

FuXi turns a model from something that *answers* into something that *works* — in
your actual codebase, shell, and browser.

| Capability | Detail |
|---|---|
| **Read and modify real files** | Read/write/edit code, config, and docs directly on disk — the model sees and changes your real files |
| **Run real shell commands** | Executes `Bash` / `PowerShell` and observes output, filtered by an **AST safety classifier** and a **rule set**; high-risk commands require confirmation |
| **Search the whole codebase** | Fast pattern search (`Glob` for paths, `Grep` for content) across any repository size |
| **Fetch live web content** | Fetches URLs, with **SSRF protection** — private address ranges are blocked |
| **Live LSP diagnostics** | Queries language servers for errors, warnings, hover info, and definitions |
| **Parallel sub-agents** | Splits large tasks across parallel sub-agents that run independently and coordinate |

### Tool set

FuXi ships roughly fifty built-in tools. They are grouped below by purpose; the
names are the identifiers FuXi exposes to the model and to permission rules.

| Group | Tools |
|---|---|
| Files & code | `Read`, `Write`, `Edit`, `Glob`, `Grep`, `NotebookEdit`, `LSP` |
| Shell | `Bash` (AST-guarded), `PowerShell` |
| Web | `WebFetch` (SSRF-guarded), `WebSearch`, `WebBrowser` |
| Agents & teams | `Agent`, `Skill`, `SendMessage`, `TeamCreate`, `TeamDelete`, `ListPeers` |
| Tasks | `TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate`, `TaskStop`, `TaskOutput`, `TodoWrite` |
| Interaction & control | `AskUserQuestion`, `EnterPlanMode`, `ExitPlanMode`, `EnterWorktree`, `ExitWorktree`, `Sleep`, `VerifyPlan`, `StructuredOutput` |
| MCP | `MCP`, `ListMcpResources`, `ReadMcpResource` |
| Automation | `CronCreate`, `CronDelete`, `CronList`, `Monitor`, `RemoteTrigger`, `Workflow`, `ToolSearch`, `subscribePR`, `SuggestBackgroundPR` |
| Session | `Brief`, `ctxInspect`, `pushNotification`, `sendUserFile`, `terminalCapture` |

A subset is sent to the model at any moment and the rest are discovered on demand
via `ToolSearch`; `--tools`, `--allowed-tools`, and `--disallowed-tools` control
which are available.

### Sandbox

Command execution is constrained by filesystem rules with allow/deny lists on both
read and write paths (`allowWrite`, `denyWrite`, `denyRead`, `allowRead`). See the
[Environment variables](environment.md) for the sandbox limits.

---

## 2. Persistence engine: long work survives

FuXi is built so that a task lasting hours does not fall over:

- **Persistent transcripts** — every conversation is written to disk; after a
  restart the session resumes with no message lost.
- **Checkpoints, resume, and rewind** — checkpoint at any moment, resume or roll
  back, and **fork** to explore a different direction from the same checkpoint.
- **"Dreaming" memory consolidation** — while idle, FuXi consolidates memory and
  learning across sessions, so the agent improves over time.
- **Automatic context compaction** — long conversations compact automatically,
  preserving key information and reducing token cost.

---

## 3. Routing: cost-aware, with failover

FuXi scores each request by complexity and routes it to the right model tier,
so a simple task does not pay for a frontier model:

| Tier | Example use |
|---|---|
| Free / local | Local or cached models |
| Cheap | Small, fast hosted models |
| Standard | Balanced general-purpose models |
| Premium | Strong models for hard problems |

Automatic failover with exponential backoff keeps work going when a provider is
rate-limited or down, and a race mode runs primary and backup models in parallel,
using whichever answers first.

---

## 4. Multi-window and cross-machine coordination

Several FuXi windows on the same project are aware of each other:

- **Local awareness** — windows broadcast file changes over a Unix domain socket,
  so a save in one window makes the others re-read the changed file.
- **Timestamp gate** — a modification-time check refuses conflicting writes, so a
  stale write cannot clobber a newer one.
- **Cross-machine relay** — a self-hosted `fuxi relay-server` lets machines in
  different locations exchange messages, authenticated with a bearer token; no
  third-party cloud is required.
- **Shared task list** — windows share a project-scoped task list (isolated by git
  root), and an atomic file lock means only one window claims a given task.

---

## 5. Extensibility

Four orthogonal extension mechanisms, all hot-reloadable:

| Mechanism | What it does |
|---|---|
| **MCP servers** | Connect any MCP server (stdio, HTTP, WebSocket; OAuth supported) and its tools become available |
| **Hooks** | Attach custom logic to lifecycle events — among them `SessionStart`, `SessionEnd`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`, `PostCompact`, `Notification`, `Stop`, and `SubagentStop` |
| **Skills & slash commands** | Package a workflow as a skill or custom slash command, stored in the repository and shared with the team |
| **Plugins** | Install and manage plugins (`fuxi plugin`), with marketplace support |

---

## 6. How the loop fits together

- **Think → Act → Verify** — the agent reasons, decides which tool to use, acts,
  observes the result, and reflects — looping until the work is verified (a test
  passes, a build is green).
- **Human in the loop** — sensitive operations require approval and can be
  interrupted; every action is recorded in local audit logs.

See the [Usage guide](usage.md) for how to drive these features, and
[Privacy Controls](../security-privacy/PRIVACY_CONTROLS.md) for the privacy
settings that apply to them.
