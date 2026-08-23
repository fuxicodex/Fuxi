# FuXi Data Subject Request (DSR) Handling

*Last updated: 2026-08-23 · Version 1.0 · Layer: L3 Procedure*

This procedure defines how privacy rights requests (access, rectification,
erasure, withdraw consent, object) are received and handled.

---

## 1. Right types

| Request | Description | Handling |
|---|---|---|
| Access | Learn what data about you we process | Explain data scope and flows |
| Rectification | Correct inaccurate information | Update account info (if applicable) |
| Erasure | Delete related data | See deletion guidance below |
| Withdraw consent | Stop consent-based processing (sign-in) | Sign out / disable account |
| Object / restrict | Object to particular processing | Assess and respond |

---

## 2. Intake channel

- Submit via the repository issue tracker or the contact details on the website.
- Requests should include: verifiable identity (if needed), request type, scope.

---

## 3. Turnaround time

- Per applicable law (usually within **30 days**, extendable as permitted).
- When identity verification is required, the clock starts after verification.

---

## 4. Key fact: local data is user-controlled

- FuXi's core data (config, sessions, memory, audit) is **stored on the user's
  device**; we **do not hold it**.
- Therefore, for local data, "erasure" can be done by the user **immediately**:
  remove the `~/.fuxi/` directory.

---

## 5. Deletion guidance

| Data | User action |
|---|---|
| Local config/sessions/memory/audit | `rm -rf "$HOME/.fuxi"` (or remove the `FUXI_CONFIG_DIR` directory) |
| Sign-in account data (if used) | Contact us, or use the account deletion option |

---

## 6. Cases that cannot be fulfilled

- Data the law requires us to retain;
- Data we do not actually hold (e.g., local data) — we will state this honestly
  and guide the user to delete it themselves.

---

## 7. Responsibility

- **Privacy team**: receive, verify, execute, and respond.
- **Users**: manage local data themselves; cooperate with identity verification
  if needed.

---

*This procedure ensures user rights receive timely, honest responses.*
