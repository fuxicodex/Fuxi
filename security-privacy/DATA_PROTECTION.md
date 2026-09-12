# FuXi Data Protection Commitment

*Last updated: 2026-09-12 · Version 1.0*

This document explains, for users worldwide, how FuXi protects data in practice:
what it classifies as sensitive, where data lives, the controls you have, your
rights, and how transfers and deletion work.

> Related: [Privacy Policy](PRIVACY_POLICY.md) ·
> [Security Whitepaper](SECURITY.md) · [Compliance & Responsibility](COMPLIANCE.md)

---

## 1. Minimization and accountability

We process only the data **necessary to provide the product**, for clearly stated
purposes.

- **A FuXi account is required to use FuXi** — minimal account data (identifier,
  authentication) is processed to operate your account; no unnecessary identity
  data is collected.
- **Zero content upload** — FuXi never collects, stores, or retains your code or
  conversations, and never asks you to upload them. In BYOK mode content travels
  directly to your chosen provider; with FuXi-managed models the request is
  transmitted only to serve it, and is not retained or used for training.
- Local data is retained only to support session resume, memory, and audit.

---

## 2. Data classification

| Level | Definition | Examples | Handling |
|---|---|---|---|
| **Public** | Publicly shareable | Docs, README, version info | No special requirements |
| **Internal** | Operational, not for publication | Internal design, metrics | Least access |
| **Sensitive** | Disclosure creates risk | Credentials, API keys, OAuth tokens | Encrypt, least privilege, no plaintext in logs |
| **User Content** | Your code and conversations | Source code, prompts, sessions | Local; transmitted only to serve a request; user-controlled |

> **Key fact**: FuXi does **not** collect, store, or retain user content. With
> BYOK, requests go directly to the provider you choose; with FuXi-managed models
> they are transmitted only to serve them. This keeps FuXi's server-side
> data-handling obligations to a minimum — it is not a claim of absolute security
> against every local threat.

---

## 3. Where data lives

| Data | Location | Can FuXi access? |
|---|---|---|
| Configuration & credentials (config.yaml) | User-local `~/.fuxi/` | No |
| Session records | User-local | No |
| Project memory file | User-local, in-project | No |
| Audit logs | User-local | No |
| Request content (BYOK) | User ↔ provider, direct | No |
| Request content (FuXi-managed models) | User → model endpoint (to serve the request only) | Not retained |
| Account data (required) | FuXi account system | Authentication-only |

```
Your machine (local — we cannot access it)
├── ~/.fuxi/config.yaml      — configuration & credentials
├── ~/.fuxi/ session records — conversation history
├── Project memory file       — cross-session memory
└── Audit logs                — operation records

Required account flow:
  fuxi login / setup-token   ──▶  FuXi account authentication (minimal data)

Leaves the device only for the model to work:
  BYOK:    prompt + code context ──▶  the provider you choose
  Managed: prompt + code context ──▶  the model endpoint (to serve the request
                                       only; not retained, not used for training)
```

**Handling rules**

1. **No plaintext credentials** — no logs, errors, or screenshots may contain
   plaintext keys.
2. **Least-privilege access** — local credential files should be owner-only.
3. **Encryption recommendation** — enable full-disk/filesystem encryption for
   local data.
4. **Minimized by default** — data leaves the device only as needed to operate the
   account or to serve a request.
5. **Redaction** — redact keys and personal data before sharing logs, issues, or
   PRs.

---

## 4. Privacy controls

FuXi runs locally, but a few functions use the network. Manage this in the TUI:

```
/privacy-settings
```

**Privacy levels**

| Level | Meaning |
|---|---|
| **default** | Telemetry enabled — anonymous product-usage signals may be sent to improve the product (no code, prompts, file paths, or command output) |
| **no-telemetry** | Analytics/telemetry disabled |
| **essential-traffic** | All nonessential network traffic disabled |

**Toggles**

| Setting | Default | What it does |
|---|---|---|
| `telemetry` | on at the **default** level | Anonymous usage/diagnostics signals |
| `crash_reports` | off | Sends crash/error summaries to help fix defects |
| `send_conversations` | **off** | Sends conversation content for support, quality, or security investigation — must be enabled explicitly by you |

FuXi never sends your conversation content for model training unless you
explicitly enable `send_conversations` (or give separate written consent).

**Environment and deployment controls**

| Variable | Effect |
|---|---|
| `FUXI_DISABLE_TELEMETRY` | Disable analytics/telemetry |
| `FUXI_DISABLE_NONESSENTIAL_TRAFFIC` | Disable all nonessential network traffic |
| `FUXI_ANALYTICS_MAX_EVENTS` | Cap the number of analytics events |
| `--no-update-notifier` / `NO_UPDATE_NOTIFIER=1` | Suppress the background update check |

**Other network requests**: the update check retrieves version metadata only;
managed-model requests occur only when you use FuXi-managed models; and account
authentication is required to use FuXi.

---

## 5. Cross-border transfers

- **User content is not transferred by FuXi**: your code and conversations are not
  collected, stored, or retained. In BYOK mode they go directly to the provider
  you choose, whose own policy and residency terms apply.
- **Account data may be transferred** to the region where the FuXi account service
  is deployed (registration is required), under the safeguards described below.
- We disclose this honestly and recommend reviewing your chosen provider's privacy
  and data-residency policies.

Safeguards: encrypted transport over HTTPS/TLS; minimal transfer (only the context
needed for the request); your choice of provider and region in BYOK mode; and
honest disclosure of flows.

---

## 6. Your rights and how to exercise them

Wherever you are, we honor these universal rights:

- **Access & transparency** — learn what data about you we process;
- **Rectification** — correct inaccurate information;
- **Erasure** — request deletion of related data;
- **Withdraw consent** — withdraw consent-based processing at any time;
- **Object & restrict** — object to or restrict particular processing.

**Local data is yours to control.** Because FuXi's core data lives on your device,
you can delete it immediately — no request needed:

| Data | Action |
|---|---|
| Local config/sessions/memory/audit | `rm -rf "${FUXI_CONFIG_DIR:-$HOME/.fuxi}"` |
| Account data (required) | Contact us to request deletion |

**Turnaround.** We apply the **strictest** applicable deadline: LGPD confirms
access within 15 days, GDPR within one month, CCPA within 45 days. We target
**15 days or sooner**. Where identity verification is needed, the clock starts
after verification. If the law allows an extension, we tell you why and when to
expect an answer.

**Intake.** Use the contact details published on the website, or the repository
issue tracker for non-sensitive requests. **Do not post identity documents or
other personal data in a public issue** — for anything requiring identity
verification, use the private contact on the website.

**Cases we cannot fulfil.** Data the law requires us to retain; and data we do not
actually hold (such as local data) — we will say so honestly and guide you to
delete it yourself.

**Escalation.** If we cannot fulfil a request, we explain why in writing and
suggest the closest alternative. If you are not satisfied, you may escalate
through the same channel, or complain to the supervisory authority in your
jurisdiction where one hears data-protection complaints.

---

## 7. Security safeguards

See the [Security Whitepaper](SECURITY.md). Highlights: an AST command-safety
classifier, an explicit permission model, local audit logs, checksum-verified
updates, and local-only credential storage. The privacy and network settings you
control are in §4 above.

---

## 8. Contact

- Website: https://www.fuxicode.com
- Repository: https://github.com/fuxicodex/Fuxi
- Privacy and data-protection matters: the contact details published on the
  website.

---

*This commitment ensures data is minimized, classified, protected, and under your
control.*
