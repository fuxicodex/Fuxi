# FuXi Privacy Controls

*Last updated: 2026-09-12 · Version 1.0*
*Layer: L1 Policy*

This page lists the privacy and network controls FuXi gives you, and how to use
them. FuXi runs locally and does not collect, store, or retain your code or
conversations — but a few functions do talk to the network, and this page shows
you exactly what and how to change it.

> Related: [Privacy Policy](PRIVACY_POLICY.md) ·
> [Security Whitepaper](SECURITY.md) ·
> [Environment variables](../docs/environment.md)

---

## 1. What always stays local

| Data | Location | Uploaded to FuXi? |
|---|---|---|
| Code, prompts, conversations | Your device | **No** — never collected, stored, or retained |
| Provider credentials (API key, OAuth token) | `~/.fuxi/` | **No** |
| Sessions, checkpoints, project memory | `~/.fuxi/`, project dir | **No** |
| Audit logs | `~/.fuxi/` | **No** |

With **your own key**, requests go directly to the provider you choose; with
**FuXi-managed models**, requests are transmitted only to serve that request and
are not retained or used to train models.

---

## 2. Privacy settings

Manage privacy preferences inside the TUI:

```
/privacy-settings
```

(also available as `/privacy`). These preferences are read and written through
FuXi's privacy settings handler.

---

## 3. Privacy levels

FuXi resolves network behaviour into one of three levels:

| Level | Meaning |
|---|---|
| **default** | Telemetry enabled — anonymous product-usage signals may be sent to improve the product (no code, prompts, file paths, or command output) |
| **no-telemetry** | Analytics/telemetry disabled |
| **essential-traffic** | All nonessential network traffic disabled |

---

## 4. Toggles

| Setting | Default | What it does |
|---|---|---|
| `telemetry` | on by default at the **default** level | Anonymous usage/diagnostics signals. Turning it off stops the corresponding events from being sent. |
| `crash_reports` | off | Sends crash/error summaries to help fix defects. |
| `send_conversations` | **off** | Sends conversation content for support, quality, or security investigation. **Must be explicitly enabled by you.** |

**FuXi never sends your conversation content to third-party or first-party model
training** unless you explicitly enable `send_conversations` (or give separate
written consent).

---

## 5. Environment / deployment controls

For CI, enterprise, or hardened deployments, these are honored:

| Variable | Effect |
|---|---|
| `FUXI_DISABLE_TELEMETRY` | Disable analytics/telemetry |
| `FUXI_DISABLE_NONESSENTIAL_TRAFFIC` | Disable all nonessential network traffic |
| `FUXI_ANALYTICS_MAX_EVENTS` | Cap the number of analytics events |
| `--no-update-notifier` / `NO_UPDATE_NOTIFIER=1` | Suppress the background update check |

---

## 6. Other network requests

- **Update check** — retrieves version metadata only; no user content. Suppress
  with `--no-update-notifier` or `NO_UPDATE_NOTIFIER=1`.
- **Managed-model requests** — only when you use FuXi-managed models.
- **Account authentication** — required to use FuXi; see the
  [Authentication Standard](standards/AUTHENTICATION.md).

---

## 7. Your controls in one place

1. Keep secrets local: credentials stay in `~/.fuxi/`; never paste them into
   issues or logs.
2. Review your settings: run `/privacy-settings` to view and change them.
3. Reduce traffic: set the level to `essential-traffic`, or set the environment
   variables in §5.
4. Delete local data: remove the config directory
   (`rm -rf "${FUXI_CONFIG_DIR:-$HOME/.fuxi}"`).
5. Exercise your rights: see
   [Data Subject Request Handling](procedures/DATA_SUBJECT_REQUEST.md).

---

*This page ensures the controls that protect your privacy are visible and
usable.*
