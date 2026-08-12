# Changelog

All notable changes to FuXi are documented in this file. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Each entry mirrors the
corresponding GitHub Release.

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

[0.1.2]: https://github.com/fuxicodex/Fuxi/releases/tag/v0.1.2
[0.1.1]: https://github.com/fuxicodex/Fuxi/releases/tag/v0.1.1
