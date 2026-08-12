# Contributing to FuXi

FuXi's source is proprietary, but this repository — the documentation, release
installers, and issue tracker — is open to contributions.

## Ways to contribute

- **Report a bug** — open an issue using the **Bug report** template.
- **Suggest a feature** — open an issue using the **Feature request** template.
- **Improve the documentation** — fix typos, clarify wording, or add sections to
  the README (English and 简体中文).
- **Answer questions** — help other users in issues and discussions.

## Bug reports

Open an issue using the **Bug report** template. The most useful reports include:

- `fuxi --version` output,
- operating system, shell, and terminal emulator,
- the provider in use (OpenAI-compatible / Bedrock / Vertex / Gemini / other),
- expected vs. actual behavior,
- a minimal reproduction.

## Feature requests

Open an issue using the **Feature request** template. Describe the problem you
are trying to solve, the proposed behavior, and why it matters. Concrete use
cases help more than abstract ideas.

## Documentation fixes and improvements

Pull requests for the README (English and 简体中文), typo fixes, clarifications,
and new documentation sections are welcome. Please keep the two languages in
lockstep: if you change a section, update both `README.md` and
`README.zh-CN.md`.

A few documentation conventions:

- Keep wording accurate and verifiable — do not claim features that are not
  shipped.
- Prefer concise, scannable sections over long prose.
- When a section changes, update the table of contents if it lists section
  anchors.

## Pull requests

- Keep PRs scoped to one change.
- Describe what changed and why in the PR description.
- A maintainer will review; response times are best-effort.

## Community guidelines

- Be respectful and constructive in all interactions.
- Do not include API keys, credentials, or personal data in issues, PRs, or
  attachments. Redact secrets before pasting config snippets or logs.

Thank you for helping keep FuXi useful for everyone!
