# FuXi Governance, Standards & Trust

*Last updated: 2026-09-12 · Version 1.0*

This document sets out how FuXi's security and privacy program is governed, the
information-security policy it applies, the technical standards behind it, and
the trust commitments we publish to users.

> Related: [Security Whitepaper](SECURITY.md) ·
> [Compliance & Responsibility](COMPLIANCE.md) · [Operations](OPERATIONS.md) ·
> [Privacy Policy](PRIVACY_POLICY.md)

---

## 1. Governance

### 1.1 Objectives

1. **Protect users** — user privacy, data, and safety are the highest priority.
2. **Secure by default** — security is a design principle, not an afterthought.
3. **Respect global law** — honor widely applicable privacy principles.
4. **Honesty and transparency** — claim only verifiable capabilities; never
   fabricate certifications.
5. **Continuous improvement** — evolve through review, metrics, and incident
   learning.

### 1.2 Document hierarchy

```
Entry documents (user-facing)
  Privacy Policy · Security Whitepaper · Terms of Service
  Usage Policy · Data Protection · Compliance & Responsibility

Supporting documents
  Governance, Standards & Trust (this file)
  Operations (incident response, disclosure, third parties, continuity)
```

Where a lower-level statement conflicts with a higher one, the higher prevails.
Where this program conflicts with applicable law, the law prevails and the program
is updated.

### 1.3 Roles

| Domain | Responsible | Accountable |
|---|---|---|
| Security architecture & threat model | Security engineering | Security lead |
| Privacy & data processing | Privacy team | Privacy lead |
| Incident response | Incident response team | Security lead |
| Vulnerability disclosure | Security engineering | Security lead |
| Third-party / supply chain | Procurement & engineering | Compliance lead |
| Compliance mapping & audit | Compliance team | Compliance lead |
| Policy maintenance & versioning | Governance team | Governance lead |

### 1.4 Review cadence

| Object | Frequency | Triggers |
|---|---|---|
| Governance & policies | Annually | Major strategic, legal, or product change |
| Standards | Annually | Tech-stack change, new threats |
| Operational procedures | Semiannually | Drill findings, incident retrospectives |
| Compliance matrix & law map | Semiannually | New laws, new jurisdictions |
| Trust disclosures | Continuous | Any material change |

Every revision records the reason, updates the version and date, obtains approval
from the accountable lead, and is published.

### 1.5 Exceptions

Any deviation from a policy or standard must be submitted in writing with the
rationale, scope, duration, and risk; approved in writing by the accountable
lead; recorded with a review date; and it expires automatically if not reviewed by
that date. Exceptions must not be used to avoid legal obligations or harm user
rights.

### 1.6 Metrics

The program is measured by externally meaningful outcomes rather than
unverifiable internal percentages:

| Metric | Target |
|---|---|
| Vulnerability report first-response time | Within 3 business days |
| Critical vulnerability remediation | Fix before disclosure |
| Incident detection-to-response | Per the Operations targets |
| Data subject request turnaround | Strictest applicable deadline (15 days) |
| Document currency | Each document states its "last updated" date |

---

## 2. Information security policy

**Objective**: protect the confidentiality, integrity, and availability (CIA) of
user and FuXi information.

### 2.1 Core stance

FuXi's security comes from the architecture itself, not bolt-on defenses:

- **Local-first** — code, configuration, credentials, and sessions stay on your
  device.
- **Distrust by default** — commands, files, and external input are validated
  before use.
- **Explicit permissions** — sensitive operations require approval; no implicit
  escalation.
- **Least privilege** — only the minimum capability a task needs.
- **Verifiable** — updates are checksum-verified; behavior is auditable.

### 2.2 Control domains

| Domain | Key controls |
|---|---|
| Command safety | AST safety classifier + rule set + permission prompts + audit logs |
| Credential management | Local-only storage in `~/.fuxi/`, never uploaded; recommend file permissions + disk encryption |
| Update integrity | SHA-256 verification + atomic replacement |
| Session & data | Local storage; user-deletable at any time |
| Account & registration | Required account, minimal data, least-privilege tokens |
| Third-party integration | Only user-configured MCP servers and plugins are loaded |
| Vulnerability management | Private reporting + fix-before-disclosure |
| Logging | Local audit logs; no plaintext credentials in logs |

### 2.3 Violations

Violations are assessed by impact and trigger remediation, procedure revision, or
the incident response process.

---

## 3. Technical standards

### 3.1 Authentication

A FuXi account is **required**. Within that account there are two ways to connect
models:

| Path | Mechanism | Purpose |
|---|---|---|
| FuXi account (required) | OAuth sign-in (`fuxi login` / `fuxi setup-token`) | Operate the account; provision FuXi-managed models |
| Bring your own key (optional) | API key / env vars / local config | Authenticate to your chosen provider |

**Credential requirements**

1. **Local storage** — API keys live in `~/.fuxi/config.yaml` or environment
   variables, never uploaded.
2. **Minimal exposure** — credentials never written to logs, errors, screenshots,
   or issues/PRs.
3. **File permissions** — set `config.yaml` to owner-only (e.g. `chmod 600`).
4. **CI use** — `FUXI_API_KEY` and similar variables can replace the config file.

**OAuth tokens.** `fuxi login` signs in interactively (stdin flow); tokens are
used only for authentication and provisioning managed models, are issued with
least privilege, and can be revoked by signing out. `fuxi setup-token` prints a
token for CI use as `FUXI_OAUTH_TOKEN`.

**Provider authentication.** In BYOK mode FuXi presents your key to the provider
as a standard client. TLS and key rotation follow the provider's standards.

### 3.2 Cryptography

| Scenario | Requirement |
|---|---|
| Communication with model providers (BYOK) | The provider-required encrypted transport (typically TLS), negotiated between provider and user |
| Official install/update downloads | Over HTTPS (TLS) |
| Update integrity | SHA-256 verified against the published manifest before the running binary is atomically replaced |

> Transport encryption with model providers is implemented by **that provider**;
> FuXi follows its standard client behavior and does not invent encryption
> protocols.

**Storage.** Local credentials and data are protected by filesystem permissions.
Whether local files are additionally encrypted is subject to the product
implementation; we do not fabricate undisclosed encryption details and recommend
OS-provided encryption (FileVault, BitLocker, LUKS).

**Key material.** API keys and OAuth tokens are generated by you or your provider;
FuXi does not generate or escrow your provider keys. Keys are stored locally only
and are neither copied nor uploaded.

### 3.3 Logging and monitoring

**Principle**: provide traceability for users while never leaking sensitive
information in logs.

- FuXi records the tool calls and command operations it executes, stored
  **locally** (under `~/.fuxi/`; debug logs under `~/.fuxi/logs/`), not uploaded.
- **Must record**: executed command/tool name; timestamp; outcome summary; the
  permission mode and whether the user approved.
- **Must not record**: API keys or tokens in plaintext; sensitive user content
  that was not voluntarily provided; full source code.
- Keys, tokens, and passwords are **masked** (e.g. `***`). Review logs before
  sharing and redact personal data.
- **Monitoring is local**: `fuxi doctor` (environment), `fuxi verify` (provider
  connectivity), `/status` `/context` `/cost` (runtime state), and the
  disable-able background version check. This targets your own environment — it
  is not server-side telemetry on user content.
- **Retention** is user-controlled; removing `~/.fuxi/` clears logs.

### 3.4 Secure development

Every change follows a secure lifecycle: requirements and threat modeling →
secure design (secure by default, least privilege) → secure implementation
(avoiding OWASP Top 10 classes such as injection, broken access control, and
sensitive-data exposure) → testing (the command classifier and permission model
are key test targets) → pre-release verification (SHA-256 and regression tests) →
post-release monitoring and response.

**Command safety** is the highest-risk surface and gets dedicated safeguards: AST
classification before execution, a rule set that blocks dangerous patterns, the
permission prompt, and a circuit-breaker on `--auto`.

**AI-specific security**

| Focus | Requirement |
|---|---|
| Prompt-injection defense | Distrust external content (files, web, MCP output); do not blindly execute embedded instructions |
| Output verification | Model output is not fact; critical operations require user confirmation |
| Tool-call safety | Validate tool parameters so malicious content cannot induce dangerous actions |
| Permission consistency | Model-driven operations match the user's permission mode; no escalation |
| Data boundary | Send only the minimal context needed for the task to the model |

---

## 4. Trust commitments

**In one line**: FuXi is local-first, bring-your-own-key, credentials are never
uploaded, your code and conversations are never collected or retained, and we
respect global law — realized by architecture, not slogans.

| Dimension | Fact |
|---|---|
| Data residency | Code, config, credentials, and sessions stay on your device |
| Keys | Local-only, never uploaded or copied |
| Content collection | No code or conversation collection |
| Forced registration | Yes — a FuXi account is required |
| Content upload | None — zero content upload |
| Command safety | AST classifier + permission prompts + audit logs |
| Invisible protection | On by default, no configuration needed (see [Security Whitepaper §5](SECURITY.md)) |
| Updates | SHA-256 verification + atomic replacement |
| Telemetry | No hidden background upload; disclosed analytics are opt-out (see [Privacy Controls](DATA_PROTECTION.md)) |
| Certification claims | No fabricated third-party certifications |
| Global law | Aligned to major privacy/AI laws; risks disclosed in [Compliance & Responsibility](COMPLIANCE.md) |

**Commitments we stand behind**

1. Local by default, minimal collection, transparent disclosure.
2. Commands and permissions are auditable, controllable, and revocable.
3. Updates are verifiable.
4. No fabricated certifications and no overstated capabilities.
5. Aimed at developers; not directed at children under 14 — users aged 14–17
   require a parent or guardian; no behavioural ads or profiling.
6. Honest limits — FuXi is a tool, not an adviser; output may be wrong and must be
   reviewed before you rely on it.

---

## 5. Scope and reporting

This program applies to the official FuXi binary, website, repository, and
related services. Third parties you actively connect follow their own policies.

- **Vulnerability reports**: privately via
  [GitHub Security Advisories](https://github.com/fuxicodex/Fuxi/security/advisories/new)
  — see [Operations §2](OPERATIONS.md).
- **Data rights requests**: see [Data Protection §6](DATA_PROTECTION.md).
- **General support**: repository issues or the website contact.

---

*This document ensures FuXi's governance, standards, and trust claims are
coherent, reviewable, and honest.*
