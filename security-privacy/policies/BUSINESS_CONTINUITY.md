# FuXi Business Continuity & Disaster Recovery Policy

*Last updated: 2026-09-12 · Version 1.0 · Layer: L1 Policy*

This policy describes how FuXi maintains service availability and how users can
recover their own data in disaster scenarios. Operational detail is in
[Backup & Recovery](../procedures/BACKUP_RECOVERY.md).

---

## 1. Key fact: resilience from being local-first

- FuXi's core functionality **runs on the user's device** and does not depend on
  FuXi servers to process a task (in BYOK mode, users connect directly to their
  own provider).
- Because an account is **required** to use FuXi, an account-system outage can
  block sign-in and therefore block use — but local data remains safe on the
  user's device and is unaffected by any outage.
- Therefore, the availability of user data is **largely in the user's own hands**,
  with minimal exposure to server outages.

---

## 2. Availability targets

| Service | Target | Notes |
|---|---|---|
| Local usage | Independent of our services | Core local features work offline/during our outage |
| Install & update services | Best effort | No formal uptime SLA; official distribution maintained |
| Account authentication (required) | Best effort | Required to use FuXi |

---

## 3. User data backup

- Local data (config, sessions, memory, audit) is backed up by the user.
- **Recommendation**: periodically back up `~/.fuxi/` and project directories, or
  use version control / sync tools.
- Recovery steps in [Backup & Recovery](../procedures/BACKUP_RECOVERY.md).

---

## 4. Disaster scenarios and responses

| Scenario | User impact | Response |
|---|---|---|
| FuXi server outage (distribution/update) | Local task work unaffected once signed in | Users continue locally; updates resume later |
| User device failure | Local data lost | User restores from backup |
| Distribution channel down | Cannot install/update | Alternate official channel + prompt restore |
| Account system failure | Sign-in blocked → use blocked | Prompt restore; local data remains safe on device |

---

## 5. Recovery objectives

- Distribution and account services: restore on a best-effort basis; no formal
  uptime SLA is published.
- User data: recovery point (RPO) and recovery time (RTO) determined by the
  user's backup strategy.

---

## 6. Responsibility

- **FuXi**: ensure availability and recovery of official services.
- **Users**: define and execute local data backup strategy.

---

*This policy ensures FuXi and user data are resilient, minimizing disaster
impact.*
