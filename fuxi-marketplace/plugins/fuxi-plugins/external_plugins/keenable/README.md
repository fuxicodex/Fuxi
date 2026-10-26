# Keenable

[Keenable](https://keenable.ai) is a web search engine built for AI agents. It gives FuXi current results from the web and reads web pages as clean markdown.

This plugin connects FuXi to Keenable's hosted remote MCP server (`https://api.keenable.ai/mcp`), no local Node.js, npm, or npx required.

## Available Tools

- **`search_web_pages`**: searches the web and returns results with title, URL, and a text snippet. Optional filters: `site` (one domain), `published_after` / `published_before` (`YYYY-MM-DD`), and `max_results`.
- **`fetch_page_content`**: fetches a URL and returns the page as markdown. An optional `prompt` returns only the part of the page you ask for.

## API Key (optional)

Without an API key the plugin connects anonymously on Keenable's shared public tier. Every request carries an `X-Keenable-Title: fuxi` header that names the client; no account is needed. For higher rate limits, create an API key in the [Keenable console](https://app.keenable.ai/console) and export it as an environment variable before launching FuXi:

```bash
# e.g. in ~/.zshrc or ~/.bashrc
export KEENABLE_API_KEY="your-api-key"
```

The plugin's MCP server configuration sends `KEENABLE_API_KEY` as the `X-API-Key` header automatically. Restart FuXi after setting it.

## Usage

The plugin works automatically when a task needs the web:

- "What changed in the latest Node.js LTS release?"
- "Find recent reports of this error message and how people fixed it"
- "Read https://fastapi.tiangolo.com/advanced/events/ and summarize the lifespan setup"

To narrow a search, ask for a site or a date range (e.g. "only results from github.com published after 2026-01-01").

---

Maintained by [Keenable](https://keenable.ai). Docs: [docs.keenable.ai/mcp-server](https://docs.keenable.ai/mcp-server). GitHub: [keenableai/keenable-mcp](https://github.com/keenableai/keenable-mcp).
