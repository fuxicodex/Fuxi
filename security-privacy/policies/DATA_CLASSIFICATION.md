# FuXi Data Classification Policy

*Last updated: 2026-08-23 · Version 1.0 · Layer: L1 Policy*

This policy defines the types of data FuXi processes, their sensitivity levels,
and corresponding handling requirements.

---

## 1. Classification levels

| Level | Definition | Examples | Handling |
|---|---|---|---|
| **Public** | Publicly shareable | Docs, README, version info | No special requirements |
| **Internal** | Operational, not for publication | Internal design, metrics | Least access |
| **Sensitive** | Disclosure creates risk | Credentials, API keys, OAuth tokens | Encrypt, least privilege, no plaintext in logs |
| **User Content** | User's code and conversations | Source code, prompts, sessions | Local by default, not through servers, user-controlled |

> **Key fact**: FuXi's architecture means **user content and credentials stay on
> the user's device by default** and never enter FuXi's servers. Therefore, for
> the "Sensitive" and "User Content" levels, FuXi **holds nothing server-side** —
> the strongest form of data protection.

---

## 2. Processing location by data type

| Data | Location | Can FuXi access? |
|---|---|---|
| Configuration & credentials (config.yaml) | User-local `~/.fuxi/` | No |
| Session records | User-local | No |
| Project memory file | User-local, in-project | No |
| Audit logs | User-local | No |
| Request content (BYOK mode) | User ↔ provider, direct | No |
| Sign-in account data (optional) | FuXi account system | Authentication-only |

---

## 3. Handling rules

1. **No plaintext credentials**: no logs, errors, or screenshots may contain
   plaintext keys.
2. **Least-privilege access**: local credential files should have user-only
   permissions.
3. **Encryption recommendation**: enable full-disk / filesystem encryption for
   local data.
4. **Local by default**: data does not leave the device unless the user actively
   configures (sign-in, third-party integration).
5. **Redaction**: redact keys and personal data before sharing logs, issues, or
   PRs.

---

## 4. Data lifecycle

```
Create → Use → Store → Archive/Delete
          ↑ user in full control throughout
```

- Retention and deletion of local data are user-controlled (remove `~/.fuxi/`).
- Sign-in account data can be deleted on request.

---

## 5. Responsibility

- **Security team**: maintain this classification and matching controls.
- **Engineering**: implement classification requirements in feature design.
- **Users**: manage local file permissions, disk encryption, and third-party
  choices.

---

*This policy ensures all data is protected according to its sensitivity.*
