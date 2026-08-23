# FuXi Record of Processing Activities (ROPA)

*Last updated: 2026-08-23 · Version 1.0 · Layer: L4 Compliance*

This record truthfully registers FuXi's data processing activities. **Core
fact**: due to the local-first architecture, FuXi does **not** process user code
or conversations by default; this record reflects that minimization reality.

---

## 1. Processing activity list

| # | Activity | Data categories | Purpose | Location | Basis |
|---|---|---|---|---|---|
| 1 | Local configuration storage | Provider config, model, key | Remember settings | User-local `~/.fuxi/` | Performance of usage relationship |
| 2 | Sessions & memory | Conversation history, project memory | Resume/continue | User-local | Performance of usage relationship |
| 3 | Audit logs | Command/tool-call records | Traceability | User-local | Legitimate interest |
| 4 | Request sending (BYOK) | Prompt + code context | Enable model work | Direct to user's provider | User's choice |
| 5 | Sign-in auth (optional) | Account identifier | Provision managed models | FuXi account system | Consent + service |
| 6 | Update downloads | Version info | Update | Official distribution | Legitimate interest |

---

## 2. Key notes

- **Data we (FuXi server-side) actually hold** is limited to: the minimal
  sign-in account data of item 5, and basic update-request information of item
  6. **Everything else stays on the user's device.**
- Therefore, user code, conversations, and credentials are **outside** our
  processing scope.

---

## 3. Data recipients

| Recipient | Scenario | Basis |
|---|---|---|
| Model providers | User actively configures BYOK | User's choice; their policy applies |
| MCP servers / plugins | User actively connects | User's choice; their policy applies |
| Official distribution infrastructure | Install/update | Minimum necessary |

---

## 4. Retention periods

| Data | Retention |
|---|---|
| Local data | User-controlled (removing `~/.fuxi/` clears it) |
| Sign-in account data | During account lifetime; user can request deletion |

---

## 5. Maintenance

- This record is updated with processing changes and reviewed semiannually.
- Used alongside [DPIA](DPIA.md) and
  [Transfer Assessment](TRANSFER_ASSESSMENT.md).

---

*This record truthfully reflects FuXi's minimal, local-first data processing
reality.*
