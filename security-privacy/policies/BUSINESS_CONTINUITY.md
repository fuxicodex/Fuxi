# FuXi Business Continuity & Disaster Recovery Policy

*Last updated: 2026-08-23 · Version 1.0 · Layer: L1 Policy*

This policy describes how FuXi maintains service availability and how users can
recover their own data in disaster scenarios. Operational detail is in
[Backup & Recovery](../../procedures/BACKUP_RECOVERY.md).

---

## 1. Key fact: resilience from being local-first

- FuXi's core functionality **runs on the user's device** and does not depend on
  FuXi servers (in BYOK mode, users connect directly to their own provider).
- Therefore, the availability of user data is **largely in the user's own hands**,
  with minimal exposure to server outages.

---

## 2. Availability targets

| Service | Target | Notes |
|---|---|---|
| Local usage | Independent of our services | Core local features work offline/during our outage |
| Install & update services | High availability | Official distribution stays available |
| Account authentication (optional) | High availability | Affects sign-in only |

---

## 3. User data backup

- Local data (config, sessions, memory, audit) is backed up by the user.
- **Recommendation**: periodically back up `~/.fuxi/` and project directories, or
  use version control / sync tools.
- Recovery steps in [Backup & Recovery](../../procedures/BACKUP_RECOVERY.md).

---

## 4. Disaster scenarios and responses

| Scenario | User impact | Response |
|---|---|---|
| FuXi server outage | Local features unaffected (BYOK) | Users continue locally |
| User device failure | Local data lost | User restores from backup |
| Distribution channel down | Cannot install/update | Alternate official channel + prompt restore |
| Account system failure | Sign-in affected | Prompt restore; local mode unaffected |

---

## 5. Recovery objectives

- Distribution and account services: restore promptly, targeting high
  availability.
- User data: recovery point (RPO) and recovery time (RTO) determined by the
  user's backup strategy.

---

## 6. Responsibility

- **FuXi**: ensure availability and recovery of official services.
- **Users**: define and execute local data backup strategy.

---

*This policy ensures FuXi and user data are resilient, minimizing disaster
impact.*
