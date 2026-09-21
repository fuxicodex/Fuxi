# FuXi Operations

*Last updated: 2026-09-12 · Version 1.0*

This document covers how FuXi runs its service responsibly: incident response,
vulnerability disclosure, third-party and supply-chain risk, business continuity
and backup, and the transparency disclosures we publish.

> Related: [Security Whitepaper](SECURITY.md) ·
> [Compliance & Responsibility](COMPLIANCE.md) ·
> [Usage Policy](USAGE_POLICY.md)

---

## 1. Incident response

### 1.1 Definitions and severity

A **security/privacy incident** is any actual or suspected event that compromises
the confidentiality, integrity, or availability of user data, the system, or the
product.

| Level | Definition | Example |
|---|---|---|
| **P0 Critical** | Credential leak, remote code execution, large-scale data breach | Tampered update, credential upload |
| **P1 High** | Permission-model bypass, command-classifier failure | Dangerous command bypasses guardrails |
| **P2 Medium** | Defect causing unintended access or data exposure | Logs leak non-sensitive information |
| **P3 Low** | Minor issue, no security impact | Documentation error |

### 1.2 Response targets (best-effort)

> The windows below are **best-effort targets, not contractual guarantees**;
> they are measured from the moment an incident is confirmed.

| Level | Detect → respond | Contain | Fix | Notify |
|---|---|---|---|---|
| P0 Critical | ≤ 2 hours | ≤ 1 business day | Issue fix before disclosure | Promptly notify affected users |
| P1 High | ≤ 1 business day | ≤ 2 business days | By priority, next release window | As impacted |
| P2 Medium | ≤ 3 business days | Per plan | Next release | As appropriate |
| P3 Low | Next iteration | — | With iteration | As appropriate |

Because breach-notification deadlines differ by jurisdiction (GDPR 72 hours,
Singapore 3 days, Australia "as soon as practicable"), we apply the **strictest**
target internally so that every regime is met.

### 1.3 Response phases

**Prepare → Detect → Contain → Eradicate → Recover → Learn.**

1. **Preparation (ongoing)** — maintain the response roster and contacts, the
   affected-version list, and the private reporting channel; run periodic drills.
2. **Detection** — receive the report (private advisories, internal monitoring of
   service-side infrastructure, community); confirm it is real; collect
   `fuxi --version`, OS, shell, and reproduction steps; assign a severity.
3. **Contain** — P0: assess impact immediately, suspend affected
   distribution/update if needed, and notify affected users, beginning within two
   hours. P1: provide temporary mitigation within one business day. P2/P3: record
   and schedule a fix.
4. **Eradicate** — locate the root cause; develop the fix and run regression
   tests; verify the update package (SHA-256).
5. **Recover** — release the fixed version (reachable via `fuxi update`); verify
   affected scenarios are restored; lift temporary mitigations. For a
   credential-leak incident, revoke and rotate the affected tokens.
6. **Learn** — record the timeline, root cause, impact, and response timeliness;
   fold improvements into policy, standard, and procedure revisions.

### 1.4 Notification and roles

- If an incident affects user data, we notify affected users and relevant parties
  promptly, per law and our commitment; on credential leaks we give remediation
  advice (key rotation); we publish necessary fixes and mitigations.
- **Roles**: the incident response team executes and contains; the security lead
  sets severity, decides, and coordinates externally; legal/PR handle compliant
  disclosure; engineering delivers the root-cause fix and regression verification.

> Note: internal monitoring covers only service-side account and distribution
> infrastructure. Because user content is never uploaded, we do not — and cannot
> — monitor user content.

---

## 2. Vulnerability disclosure

Security researchers' reports are welcome.

- **Reporting channel**: GitHub
  [Security Advisories](https://github.com/fuxicodex/Fuxi/security/advisories/new)
  (private). Do not discuss security issues in public issues.
- **What to include**: FuXi version (`fuxi --version`) and install method; OS and
  shell; a minimal reproduction or proof-of-concept; your assessed impact.
- **Flow**: Receive → Confirm (**initial reply within 3 business days**) → Triage
  → Fix → Coordinated disclosure → Publish. We aim to release a fix before
  details are made public; the disclosure window is generally up to **90 days**
  between acknowledgment and publication, shortened when a fix ships sooner.
- **Principles**: agree a reasonable public timeline with the reporter; do not
  leak details to unrelated parties before publication; credit the reporter with
  permission.
- **Bounty**: FuXi currently does **not** run a public bug-bounty program with
  published rewards. If one launches, its scope and rewards will be announced
  officially.
- **For reporters**: do not access or leak others' data without authorisation; do
  not perform denial-of-service, physical, or social-engineering attacks; follow
  local law.

---

## 3. Third-party and supply-chain risk

| Type | Introduced by | Risk |
|---|---|---|
| Model providers (BYOK) | User | Content transmission, data handling |
| MCP servers | User | Tool access, command execution |
| Plugins / skills | User | Arbitrary code execution |
| Vendors (hosting, distribution) | FuXi | Supply chain, service availability |

**Third parties you connect.** FuXi states honestly which data flows to third
parties and you choose. MCP servers and plugins are **off by default** and load
only when you explicitly configure them. Install only from trusted sources and
review each third party's privacy policy and data-processing terms.

**FuXi's own supply chain.** Installs and updates come only from
`https://downloads.fuxicode.com`. `fuxi update` verifies SHA-256 against the
published manifest and replaces the binary atomically. A single static binary with
no runtime dependencies shrinks the supply-chain attack surface. The product
source is not published, so third parties cannot target public code paths; we
provide verifiability instead through this documentation set, self-checks, and
the transparency disclosures in §5.

**Vendor assessment.** For third parties FuXi itself uses: transfer only the
minimum data necessary; assess their security and privacy practices; bind their
data handling by contract; and disclose them (§4). On a third-party security
incident, we assess user impact and notify per our commitment, and promptly
disable and clean up any third party no longer used or found risky.

---

## 4. Subprocessors

FuXi is local-first: apart from the account and distribution services below, we
do not engage third parties to process user data, and user content is never
processed by subprocessors.

| Processor | Purpose | Data handled | Location |
|---|---|---|---|
| Official distribution/update infrastructure | Distribute binary and updates | Version info, basic update-request info | Per official website |
| Account authentication service (required sign-in) | Identity authentication and account operation | Account identifier | Per official website |

The specific processor list and locations are disclosed on the official website
(https://www.fuxicode.com); this list is updated before material changes take
effect.

**Explicit exclusions.** The following are **not** FuXi subprocessors (chosen by
you, not engaged by FuXi): model providers you select via BYOK; MCP servers you
connect; plugins and skills you install. Their compliance is governed by their own
policies.

---

## 5. Transparency and business continuity

### 5.1 Transparency disclosures

| Item | Status |
|---|---|
| User code collection | **None by default** — not collected, stored, or retained; `send_conversations` is opt-in |
| Conversation content collection | **None by default** (opt-in via `send_conversations`) |
| Credential collection | **None** — local-only |
| Hidden telemetry | **None** — no undisclosed tracking; available analytics are disclosed and opt-out (see [Privacy Controls](DATA_PROTECTION.md)) |
| Forced registration | **Yes** — a FuXi account is required to use FuXi |

Government and legal requests: we disclose only what we **actually hold**. Because
we do not hold user code or conversations, there is generally nothing to disclose
for content requests; account-information requests are answered only as the law
requires, within the minimum we hold. We publish figures when a request actually
occurs; as of this issue, none has been reported.

| Item | Status |
|---|---|
| Reported vulnerabilities | Via repository security advisories (private; public after disclosure) |
| Confirmed data breaches | No public record |
| High-severity incidents | No public record |

### 5.2 Business continuity

FuXi's core functionality runs on your device, so an outage of our services does
not stop local work once you are signed in. Because an account is required, an
account-system outage can block sign-in and therefore block use — but local data
remains safe on your device throughout.

| Service | Target | Notes |
|---|---|---|
| Local usage | Independent of our services | Core local features work offline/during our outage |
| Install & update services | Best effort | No formal uptime SLA |
| Account authentication (required) | Best effort | Required to use FuXi |

| Scenario | User impact | Response |
|---|---|---|
| FuXi server outage (distribution/update) | Local task work unaffected once signed in | Continue locally; updates resume later |
| User device failure | Local data lost | Restore from your backup |
| Distribution channel down | Cannot install/update | Alternate official channel; prompt restore |
| Account system failure | Sign-in blocked → use blocked | Prompt restore; local data remains safe on device |

### 5.3 Backup and recovery

| Data | Location | Notes |
|---|---|---|
| Configuration & credentials | `~/.fuxi/config.yaml` (or `$FUXI_CONFIG_DIR/config.yaml`) | Provider, model, key |
| Session records | Under the config directory | History, checkpoints |
| Project memory | Memory files in project | Cross-session memory |
| Audit logs | Under the config directory | Operation records |
| Debug logs | `~/.fuxi/logs/` | Diagnostic logs |

```bash
# Back up the config directory
cp -a "$HOME/.fuxi" "$HOME/.fuxi.backup.$(date +%Y%m%d)"

# Restore it
rm -rf "$HOME/.fuxi"
cp -a "$HOME/.fuxi.backup.<backup-date>" "$HOME/.fuxi"
fuxi doctor    # verify after restoring
```

- **Backups may contain keys** — encrypt them and store them securely.
- To restore a single session, use `/history` or `/resume` in the TUI, or
  `fuxi -r <sessionId>` / `fuxi -c` on the command line.

---

## 6. Responsibility

- **FuXi**: maintain the response process, disclose honestly, manage its own
  supply chain, and keep official services available on a best-effort basis.
- **Users**: define and run your own backups (encrypted), and manage the choice
  and risk of the third parties you connect.

---

*This document ensures FuXi's operational commitments are executable, measurable,
reviewable, and honestly disclosed.*
