# FuXi Logging & Monitoring Standard

*Last updated: 2026-08-23 · Version 1.0 · Layer: L2 Standard*

This standard sets FuXi's logging, monitoring, and security-audit requirements.
Core principle: **provide traceability for users while never leaking sensitive
information in logs.**

---

## 1. Audit logs

- FuXi records the tool calls and command operations it executes, for user
  review.
- Logs are stored **locally** (under `~/.fuxi/`), not uploaded by default.
- Purpose: traceability, auditability, and post-incident review.

---

## 2. Log content rules

**Must record:**

- executed command / tool name;
- timestamp;
- outcome summary (success/failure);
- permission mode and whether user-approved.

**Must not record:**

- API keys, OAuth tokens, or other credentials in plaintext;
- sensitive user content not voluntarily provided (unless required for audit and
  already redacted);
- full source code (only necessary context).

---

## 3. Redaction requirements

- Keys, tokens, and passwords in logs are **masked/redacted** (e.g., `***`).
- Double-check before sharing logs; remove personal data and credentials.

---

## 4. Monitoring

- **Local self-check**: `fuxi doctor` checks config, API key, git, ripgrep, etc.
- **Connectivity**: `fuxi verify` confirms provider connection.
- **Status visibility**: `/status`, `/context`, `/cost` reflect runtime state in
  the TUI.
- **Update notification**: background version check (disable-able).

> Note: this monitoring targets the **user's own environment**; it is not
> server-side telemetry on user content. FuXi does not collect user code or
> conversation content.

---

## 5. Log retention and deletion

- Local log retention is user-controlled; removing `~/.fuxi/` clears them.
- Recommend periodic cleanup or archival of old logs.

---

## 6. Responsibility

- **Product**: ensure logs do not leak sensitive data and audit information is
  complete.
- **Users**: review logs, manage retention, and redact before sharing.

---

*This standard ensures the balance between traceability and privacy protection.*
