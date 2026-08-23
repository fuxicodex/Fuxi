# FuXi Backup & Recovery Procedure

*Last updated: 2026-08-23 · Version 1.0 · Layer: L3 Procedure*

This procedure explains how users back up and restore local data, and how FuXi
ensures service-side recovery. Policy in
[Business Continuity Policy](../../policies/BUSINESS_CONTINUITY.md).

---

## 1. Data to back up

| Data | Location | Notes |
|---|---|---|
| Configuration & credentials | `~/.fuxi/config.yaml` | Provider, model, key |
| Session records | `~/.fuxi/` related locations | History, checkpoints |
| Project memory | Memory files in project | Cross-session memory |
| Audit logs | `~/.fuxi/` related locations | Operation records |

> Also back up your **project code directories** (usually already in version
> control).

---

## 2. Backup methods

```bash
# Back up the whole config directory
cp -a "$HOME/.fuxi" "$HOME/.fuxi.backup.$(date +%Y%m%d)"

# Or archive it
tar -czf fuxi-backup.tar.gz "$HOME/.fuxi"
```

- You may also use version control (excluding sensitive content) or cloud sync
  tools.
- **Note**: backups may contain keys; encrypt them and store securely.

---

## 3. Restore methods

```bash
# Restore the whole config directory
rm -rf "$HOME/.fuxi"
cp -a "$HOME/.fuxi.backup.20260823" "$HOME/.fuxi"
```

- After restoring, run `fuxi doctor` to verify environment integrity.

---

## 4. Single-session restore

- In the TUI, `/history` and `/resume` restore past sessions/checkpoints.
- On the command line, `fuxi -r <sessionId>` or `-c` continues the latest
  session.

---

## 5. Service-side recovery (FuXi's responsibility)

- Official install/update distribution stays highly available.
- Account authentication (optional) is restored promptly on failure; local mode
  is unaffected.

---

## 6. Responsibility

- **Users**: define and run local backups; store backups encrypted.
- **FuXi**: ensure official service availability and recovery.

---

*This procedure ensures data is back-up-able, restorable, and risk-managed.*
