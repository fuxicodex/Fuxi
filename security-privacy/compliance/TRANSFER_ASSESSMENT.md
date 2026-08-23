# FuXi Transfer Impact Assessment (TIA)

*Last updated: 2026-08-23 · Version 1.0 · Layer: L4 Compliance*

This assessment explains cross-border data transfer involving FuXi, to support
data-export reviews across jurisdictions.

---

## 1. Bottom line

- **No cross-border transfer by default**: local data does not leave your
  device.
- **After active configuration**: transfer to a model provider is determined by
  **your choice**; providers may be in different countries/regions.
- FuXi's servers do **not** hold or relay user code or conversations.

---

## 2. Transfer scenario analysis

| Scenario | Cross-border? | Data | Decided by | Safeguards |
|---|---|---|---|---|
| Local use | No | Config/sessions/memory/audit | — | Local device security |
| BYOK request | Depends on provider | Prompt + code context | User | Provider TLS + its policy |
| Sign-in (optional) | Depends on deployment | Account identifier | User | OAuth + least privilege |
| Updates | Yes (official channel) | Version info | User | HTTPS + SHA-256 |

---

## 3. Safeguards

- **Encrypted transport**: updates and provider communication over HTTPS/TLS.
- **Minimal transfer**: only the minimal context needed is sent to the model.
- **User choice**: whether and where to transfer is determined by the provider
  the user selects.
- **Transparent**: flows are disclosed honestly; review providers' residency
  policies.

---

## 4. User action recommendations

1. Choose providers that meet your jurisdiction's data-residency requirements.
2. Review the provider's privacy policy and cross-border terms.
3. For sensitive projects, prefer local/compliant deployment options.

---

## 5. Boundary statement

- This assessment is not legal advice; specific export obligations follow
  applicable law and your jurisdiction.
- FuXi does not assume substitute liability for transfers to third parties the
  user actively chooses (see Third-Party Risk Policy).

---

*This assessment ensures cross-border transfers are transparent, minimal, and
user-controlled.*
