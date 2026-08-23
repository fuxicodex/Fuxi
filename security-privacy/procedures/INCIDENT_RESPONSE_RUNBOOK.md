# FuXi Incident Response Runbook

*Last updated: 2026-08-23 · Version 1.0 · Layer: L3 Procedure*

This runbook provides **step-by-step** incident response. Policy in
[Incident Response Policy](../../policies/INCIDENT_RESPONSE.md).

---

## 1. Preparation (ongoing)

- [ ] Maintain incident response team roster and contacts.
- [ ] Maintain affected-version list and release process.
- [ ] Confirm private reporting channel (GitHub Security Advisories) is working.
- [ ] Run periodic drills.

---

## 2. Detection & identification

1. Receive report (private advisories, internal monitoring, community).
2. Confirm the event is real (reproduce/verify).
3. Collect information: `fuxi --version`, OS, shell, reproduction steps.
4. Assign severity per policy (P0–P3).

---

## 3. Contain

| Severity | Containment action |
|---|---|
| P0 | Immediately assess impact; suspend affected distribution/update if needed; notify affected users |
| P1 | Provide temporary mitigation (disable feature, strengthen permission prompts) |
| P2/P3 | Record and schedule a fix |

---

## 4. Eradicate

1. Locate root cause (code, dependency, process).
2. Develop the fix and run regression tests.
3. Verify the update package (SHA-256) and release.

---

## 5. Recover

- Release the fixed version (reachable via `fuxi update`).
- Verify affected scenarios are restored.
- Lift temporary mitigations.

---

## 6. Learn

1. Record timeline, root cause, impact, response timeliness.
2. Propose improvements and fold into policy/standard/procedure revisions.
3. Run training or hardening as needed.

---

## 7. Notification template points

- Incident overview and impact scope;
- Actions affected users should take (e.g., rotate keys);
- Fixed version and mitigations;
- Contact and timeline.

---

*This runbook ensures incident response is executable, measurable, and
reviewable.*
