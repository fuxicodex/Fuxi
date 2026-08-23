# FuXi Security Whitepaper

*Last updated: 2026-08-23 · Version 1.0*

This whitepaper describes FuXi's security architecture and threat model, for
users and security researchers worldwide. FuXi runs shell commands, stores
provider credentials under `~/.fuxi/`, and self-updates over the network — so
security reports are welcome and appreciated. **FuXi is secure by design,
protecting its users** — this goal is realized through the technical design
below, not slogans.

---

## 1. Core security design principles

FuXi ensures safety across five layers:

1. **Local-first** — code, configuration, credentials, and sessions stay on
   your device by default, reducing attack surface.
2. **Distrust of external input by default** — commands, files, and MCP content
   are validated before execution.
3. **Explicit permissions** — sensitive operations require your approval; no
   implicit escalation.
4. **Verifiability** — updates are checksum-verified; behavior is traceable
   through audit logs.
5. **Least privilege** — only the minimum capability needed to complete a task
   is exercised.

---

## 2. Threat model

We explicitly identify and address the following threats:

| Threat | FuXi's mitigation |
|---|---|
| Malicious / dangerous shell commands | Commands pass an **AST safety classifier** + rule set before execution |
| Unauthorized access to local credentials | API keys live only in local `~/.fuxi/`, never uploaded; protected by file-system permissions |
| Supply-chain attack (tampered binary) | `fuxi update` performs SHA-256 checksum verification and atomic replacement |
| Provider-side leakage | You bring your own key; content flows directly to the provider you choose; without an account, nothing passes through FuXi |
| Malicious MCP / plugin | Only servers you explicitly configure are loaded; none enabled by default |

---

## 3. Command safety

FuXi can execute shell commands (`bash` / PowerShell). To keep this capability
from being abused:

- **AST safety classifier**: before execution, a command is parsed into an
  abstract syntax tree and classified by safety level.
- **Rule set**: additional policy rules block dangerous patterns.
- **Permission modes**: `default` / `plan` / `bypassPermissions` are yours to
  choose; `--auto` only auto-approves operations the classifier deems safe, with
  a circuit-breaker.
- **Audit logs**: every executed action is traceable and reviewable.

> ⚠️ `--dangerously-skip-permissions` skips all permission checks. Use it only in
> fully trusted, isolated environments, at your own risk.

---

## 4. Credential and key handling

- **Storage location**: API keys, OAuth tokens, and other credentials are stored
  locally in `~/.fuxi/config.yaml` or environment variables.
- **Not uploaded**: FuXi does not copy or upload your keys to any FuXi server.
- **Bring your own key (BYOK)**: keys are used only to make requests to the
  provider you configure, traveling directly between you and that provider.
- **Recommendations**: set appropriate file-system permissions on the
  credential file; redact secrets before sharing screenshots or logs. Do not
  paste keys into issues, PRs, or attachments.

---

## 5. Update security

- FuXi checks for new versions in the background (disable with
  `--no-update-notifier` or `NO_UPDATE_NOTIFIER=1`).
- `fuxi update` downloads the target version and **verifies its SHA-256 against
  the published manifest** before **atomically** replacing the running binary —
  preventing tampered or partially-installed states.
- Installers come from `https://releases.fuxicode.com`; install only from
  official channels.

---

## 6. Supported versions

Only the latest release is actively maintained. Keep it current and verify the
affected version with `fuxi --version` before reporting.

---

## 7. Reporting a vulnerability

Please report suspected vulnerabilities **privately** through GitHub's
[Security Advisories](https://github.com/fuxicodex/Fuxi/security/advisories/new).
Do **not** open a public issue for security concerns.

Include:

- FuXi version (`fuxi --version`) and how it was installed;
- operating system and shell;
- a minimal reproduction or proof-of-concept;
- the impact you believe it has.

**What to expect**: reports are reviewed on a best-effort basis; you will receive
an initial response within a few days and follow-ups as the report progresses.
If accepted, we aim to release a fix before details are made public and will
coordinate disclosure timing with you; as a general guideline, we ask for a
window of up to 90 days between acknowledgment and public disclosure, shortened
whenever a fix ships sooner.

Thank you for helping keep FuXi users safe.

---

*Last updated: 2026-08-23 · Version 1.0 · Entity: FUXI*
