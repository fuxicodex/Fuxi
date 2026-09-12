# FuXi Record of Processing Activities (ROPA)

*Last updated: 2026-09-12 · Version 1.0 · Layer: L4 Compliance*

This record truthfully registers FuXi's data processing activities. **Core
fact**: due to the local-first architecture, FuXi does **not** process user code
or conversations by default; this record reflects that minimization reality.

---

## 1. Processing activity list

**Controller**: FuXi ("FUXI"); contact via the website contact details. Where
required by law, a local representative is appointed and published on the
official website.

| # | Activity | Data categories | Purpose | Location | Basis | Retention |
|---|---|---|---|---|---|---|
| 1 | Local configuration storage | Provider config, model, key | Remember settings | User-local `~/.fuxi/` | Performance of contract | Until the user deletes it |
| 2 | Sessions & memory | Conversation history, project memory | Resume/continue | User-local | Performance of contract | Until the user deletes it |
| 3 | Audit logs | Command/tool-call records | Traceability | User-local | Legitimate interest | Until the user deletes it |
| 4 | Request sending (BYOK, user-initiated) | Prompt + code context | Enable model work | Direct user ↔ provider | User's choice (outside our scope) | Not retained by FuXi |
| 5 | Account authentication (required) | Account identifier | Operate account; provision managed models | FuXi account system | Performance of contract | Account lifetime + 30 days |
| 6 | Update downloads | Version info | Update | Official distribution | Legitimate interest | Not retained |

---

## 2. Key notes

- **Data we (FuXi server-side) actually hold** is limited to: the minimal
  account data of item 5, and basic update-request information of item
  6. **Everything else stays on the user's device.**
- Item 4 is a **user-initiated direct transfer** between the user and their
  chosen provider; FuXi relays no content, so it is listed here for completeness
  and counts as **outside our processing scope**.
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
| Account data | During account lifetime; user can request deletion |

---

## 5. Maintenance

- This record is updated with processing changes and reviewed semiannually.
- Used alongside [DPIA](DPIA.md) and
  [Transfer Assessment](TRANSFER_ASSESSMENT.md).

---

*This record truthfully reflects FuXi's minimal, local-first data processing
reality.*
