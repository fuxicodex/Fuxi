# Changelog

All notable changes to FuXi are documented in this file. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Each entry mirrors a **published GitHub Release**
([releases](https://github.com/fuxicodex/Fuxi/releases)). Development builds can
be newer than the latest release listed here; run `fuxi --version` to check the
build you have and `fuxi update` to move to the latest release.


## [0.1.8] - 2026-09-22

## New Features

- **Rate-limit banners**: unified rate-limit data now feeds subscription banners; usage beyond the limit is silently rolled into additional usage with clear notification.
- **Official plugin marketplace mirror**: the plugin marketplace is now served from an official GCS mirror, making plugin installs more stable and reliable.

## Performance

- **Smoother long-session interactions**: estimated scroll offsets and zero render-time filesystem syscalls reduce a cold first frame from ~1.6s (1000 lines) to ~160ms; scrolling performance is now independent of line count.
- **Faster resume & reads**: a resume reads the transcript only once (34MB: 4.6s → 0.8s); sessions larger than 5MiB are read through a precompacted fast path in 1MB sequential chunks (~4.9× on a 30MB transcript); write-side 100ms batching keeps the disk format unchanged.
- **Streaming render fix**: the `linkify` O(n²) full-render issue is resolved (20KB single line: 278ms → 2.9ms); streaming output no longer appears non-streaming.

## Sessions & Messages

- **Session storage-chain optimization**: a precompact read fast path, write-side batching, and live-cache re-append are introduced (metadata such as titles and tags flush synchronously, and external SDK writes are absorbed via a 64KB tail window).
- **Message-chain integrity**: parentUuid chains now fully link every participant, with automatic re-linking after forks; switching sessions no longer loses in-flight messages; a unified session UUID registry fixes the `/clear` cache invalidation issue.

## Permissions & Security

- **Dialog & rules**: the permission dialog now uses a numbered Select list; "Always Allow" clearly displays the exact rule to be persisted; low-risk file commands (mkdir/cp/mv/touch/rmdir) are relaxed to command-name prefix rules.
- **Stability & Bash safety**: the whole-UI freeze caused by permission dialogs is resolved (approval sends are now non-blocking); the Bash read-only gate is hardened (backticks and newlines can no longer bypass auto-approval); permission suggestions are built once per request and differentiated by reason.

## Windows Compatibility

- **Startup & rendering**: when Git for Windows is missing, startup now provides installation guidance directly (no longer stuck behind the login flow); CJK console glyphs and borders adapt to terminal capabilities, resolving mojibake, tofu, and input-box jitter; subprocess output is decoded strictly as UTF-8.

## Engine & Tools

- **Non-streaming fallback**: on empty or interrupted streams, the current turn is automatically retried via a non-streaming request.
- **Tool-execution dedup**: a tool state machine and tracker form a dedup closed loop, eliminating duplicate tool cards.
- **Tool behavior unification**: Read, Write, Edit, Notebook, and PDF tools now share consistent behavior and error messages; non-standard error prefixes are removed.

## UI / MCP / Misc

- **UI**: the task list is deduplicated (the right sidebar is the single task surface); the plan-approval dialog fits exactly, with buttons remaining visible on long plans.
- **MCP**: the command allowlist is re-seeded after configuration reloads (servers added at runtime are no longer blocked); `~/.fuxi.json` global configuration is unified.


## [0.1.6] - 2026-09-07

Unified session and message handling, hardened login flow, and cross-platform stability improvements.

### Added

- Unified session & message handling: chat messages are consolidated into a single message model, removing inconsistencies between handling paths; message parent-child chains are preserved more completely, and partially-compacted history survives session resume.
- Hardened login flow: cross-process token refresh is serialized to prevent token-chain failures; tokens are refreshed proactively before expiry to avoid forced re-login; login no longer times out — it waits until the user cancels.
- Model selection validation: the `/model` command now validates that the selected model is supported by the current endpoint, with clear feedback on invalid model names.

### Changed

- Engine: empty responses are automatically retried via non-streaming requests; repeated injection of external file changes and conditional memory is fixed; the coordinator queue is drained before every request; gateway length errors are correctly recognized as context-window overflows.
- Bash / Windows: unified command-line parsing reduces misclassification; strict UTF-8 subprocess output on Windows avoids garbled text; nested-heredoc crash fixed; startup git-bash check and working-directory exclusion added.
- UI & rendering: improved markdown rendering with box-drawing tables; sidebar shows reasoning state and session cost; chat lag on huge content fixed; CJK character-width handling now applies only to legacy Windows consoles.
- Tasks / agents: standardized task IDs and output paths; notification queue priorities (immediate / later / next); stricter stop-task conditions; `agent_busy` claim check.
- Files & search: more accurate search timeouts; staged protection for very large file reads; Grep content checks and UNC path handling fixed.
- MCP: `/mcp` toggle persisted per project; improved port allocation and lock-backoff; staged truncation for tool output.
- Permission & sandbox: static directory rules support subtree matching; sandbox configuration now takes effect with settings; unified session grant logic.
- Context compaction: staged decision for file restore after compaction; improved shared-cache partial compaction.
- Image recognition: recognition configuration is endpoint-scoped and no longer affects the main model's vision judgment; recognition-model refusals are never cached.

## [0.1.2] - 2026-08-06

Multi-window coordination, image capabilities, and plugin ecosystem improvements.

### Added

- Multi-window coordination: switch seamlessly between concurrent sessions without interrupting your current work.
- Image captioning: non-vision models can now generate image descriptions automatically, enabled by default.
- Automatic vision-capability detection from known provider capabilities, no manual configuration required.
- Task-adaptive thinking mode for smarter responses.
- Voice capture and browser tools integrated through the native extension bridge.

### Changed

- Tool-level thinking refined; status blink for collapsed groups in the TUI restored.
- Unified MCP plugin lifecycle: manifest, channel, session, and other plugin sources load under one consistent contract.
- Memory extraction now runs asynchronously with an optimized `memory_saved` card.
- Model cache isolation stays stable across sessions; compacted context remains consistent across TUI turns.
- Each model gets a stable user identity; long prompts are preserved intact across the OpenAPI boundary.
- Plugin LSP lifecycle options supported; usable LSP plugins recommended after real file edits.

### Fixed

- Multiple security hardening items: plaintext MCP tokens removed, OAuth credentials scoped to their trust domains, plugin secrets kept out of prompts, plugin reloads no longer expose stale state.
- Path traversal blocked before normalization, preventing path-escape risks.
- Empty tool results no longer lost before transcript replay.

## [0.1.1] - 2026-08-05

Remote control, image preprocessing, and built-in search tooling.

### Added

- Remote Control: CCR v2 sessions with secure worker credential exchange and real-time event streaming, synchronized with the local TUI.
- Remote input integrated with the local session; slash commands and prompts processed under unified security policies.
- Image preprocessing: automatic resizing and compression before upload using the Lanczos3 scaling kernel.
- Built-in file search tools (`bfs`/`ugrep`) with no additional dependencies, available on Windows, macOS, and Linux.
- Chrome integration dialog, enabled by default.
- `@mention` content delivered directly to the model.
- Bash cards expanded by default.
- Exit-word routing and automatic detection of long-running task keywords.

### Changed

- Optimized context compaction and tool-result budgeting for more stable long-conversation streaming.
- Token refresh interval extended to 6 hours.
- WebSocket 401 auto-recovery improved.

### Fixed

- Windows path conversion, snapshot, hooks, and permission rule issues.
- `deepseek-v4` output limits and API request parameters (`top_p`).
- Attachment ordering, message boundaries, and hook completion order.

[0.1.6]: https://github.com/fuxicodex/Fuxi/releases/tag/v0.1.6
[0.1.2]: https://github.com/fuxicodex/Fuxi/releases/tag/v0.1.2
[0.1.1]: https://github.com/fuxicodex/Fuxi/releases/tag/v0.1.1
