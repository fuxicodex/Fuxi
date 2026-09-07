# Changelog

All notable changes to FuXi are documented in this file. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Each entry mirrors the
corresponding GitHub Release.

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

[0.1.6]: https://github.com/fuxicodex/Fuxi/releases/tag/0.1.6
[0.1.2]: https://github.com/fuxicodex/Fuxi/releases/tag/v0.1.2
[0.1.1]: https://github.com/fuxicodex/Fuxi/releases/tag/v0.1.1
