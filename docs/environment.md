# Environment variables

FuXi resolves configuration from, in order of precedence: environment variables,
`~/.fuxi/config.yaml`, and built-in defaults. This page mirrors the full
`Environment` section of `fuxi --help`, so the knobs that matter most to a
security or deployment review — remote control, the bash sandbox, and MCP
resource limits — are visible and searchable here. Run `fuxi --help` on your
installed binary for the always-authoritative reference.

## Provider & credentials

| Variable | Purpose |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `ANTHROPIC_MODEL` | Model name for the Anthropic provider (default `claude-sonnet-4-6`) |
| `FUXI_BASE_URL` | OpenAPI-compatible base URL (e.g. `https://api.openai.com/v1`) |
| `FUXI_API_KEY` | API key for the OpenAPI-compatible provider |
| `FUXI_MODEL` | Model name for the OpenAPI-compatible provider |

## Reasoning

| Variable | Purpose |
|---|---|
| `FUXI_THINKING_MODE` | Thinking mode: `auto` / `enabled` / `disabled` |
| `FUXI_THINKING_EFFORT` | Thinking effort: `low` / `medium` / `high` / `max` |
| `FUXI_THINKING_STRATEGY` | Thinking strategy: `auto` / `native` / `prompt_inject` / `two_phase` |

## Config & diagnostics

| Variable | Purpose |
|---|---|
| `FUXI_CONFIG_DIR` | Override the config directory (default `~/.fuxi`) |
| `FUXI_DEBUG` | Set to `1` to enable debug logging |

## Bridge / remote control

| Variable | Purpose |
|---|---|
| `FUXI_ENV_PROFILE` | Backend profile selector: `test` / `prod` |
| `FUXI_ENVIRONMENT_ID` | Registered environment ID (auto-saved to `~/.fuxi/bridge.env`) |
| `FUXI_ENVIRONMENT_SECRET` | Environment secret for work polling |
| `FUXI_BRIDGE_TOKEN` | OAuth access token for bridge registration |
| `FUXI_MAX_SESSIONS` | Max concurrent remote sessions (default `32`) |
| `FUXI_DISABLE_BRIDGE` | Set to `1` to disable remote-control mode |

## Feature toggles

| Variable | Purpose |
|---|---|
| `FUXI_FORK_MAX_CONCURRENCY` | Max concurrent fork agents (int, default `4`) |
| `FUXI_DISABLE_TOOL_USAGE` | Set to `1` to disable persistent tool-usage tracking |
| `FUXI_DISABLE_AWAY_SUMMARY` | Set to `1` to disable session-end away-summary persistence |
| `FUXI_INLINE` | Set to `1` to force the inline dashboard as a fallback surface |
| `FUXI_INK` | No-op (`1`) — Ink is the default primary surface |

## Sampling controls

| Variable | Purpose |
|---|---|
| `FUXI_TEMPERATURE` | Sampling temperature (0.0–2.0) |
| `FUXI_TOP_P` | Top-p nucleus sampling (0.0–1.0) |
| `FUXI_SEED` | Reproducible sampling seed (positive int) |

## Bash sandbox (macOS)

| Variable | Purpose |
|---|---|
| `FUXI_BASH_ALLOW_NETWORK` | Set to `1` to allow network access from the bash tool |
| `FUXI_BASH_MEM_LIMIT_MB` | Bash process memory ceiling in MB |

## MCP resource limits

| Variable | Purpose |
|---|---|
| `FUXI_MCP_MEM_LIMIT_MB` | MCP server memory ceiling in MB |
| `FUXI_MCP_CPU_LIMIT_SEC` | MCP server CPU-time ceiling in seconds |

## Env variables documented under flags

These are documented alongside their flags and are honored the same way:

| Variable | Where it applies |
|---|---|
| `NO_UPDATE_NOTIFIER` | Suppress background update checks (`--no-update-notifier`) |
| `FUXI_TEAM_NAME` | Swarm team name (`--team`) |
| `FUXI_OAUTH_TOKEN` | Token printed by `fuxi setup-token` for headless/CI auth |
| `FUXI_RELAY_TOKEN` | Auth for `fuxi relay-server` |
