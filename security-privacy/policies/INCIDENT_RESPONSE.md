# FuXi Incident Response Policy

*Last updated: 2026-08-23 · Version 1.0 · Layer: L1 Policy*

This policy defines the classification, severity, response targets, and
responsibilities for security and privacy incidents. Operational detail is in
the [Incident Response Runbook](../../procedures/INCIDENT_RESPONSE_RUNBOOK.md).

---

## 1. Definition

**Security/privacy incident**: any actual or suspected event that compromises
the confidentiality, integrity, or availability of user data, the system, or the
product.

---

## 2. Severity levels

| Level | Definition | Example |
|---|---|---|
| **P0 Critical** | Credential leak, remote code execution, large-scale data breach | Tampered update, credential upload |
| **P1 High** | Permission-model bypass, command-classifier failure | Dangerous command bypasses guardrails |
| **P2 Medium** | Defect causing unintended access/data exposure | Logs leak non-sensitive info |
| **P3 Low** | Minor issue, no security impact | Documentation error |

---

## 3. Response targets (SLA)

| Level | Detect→respond | Contain | Fix | Notify |
|---|---|---|---|---|
| P0 | Within hours | ASAP | Fix before disclosure | Promptly notify affected users |
| P1 | 1 business day | ASAP | By priority | As impacted |
| P2 | Within days | Per plan | Next release | As appropriate |
| P3 | Per plan | — | With iteration | As appropriate |

---

## 4. Response phases

**Prepare → Detect → Contain → Eradicate → Recover → Learn**, detailed in the
runbook.

---

## 5. Notification obligations

- If an incident affects user data, notify affected users and relevant parties
  promptly, per law and commitment.
- On credential leaks, provide remediation advice (key rotation, etc.).
- Publish necessary fixes and mitigations.

---

## 6. Roles and responsibilities

- **Incident response team**: execute response, contain impact.
- **Security lead**: severity, decisions, external coordination.
- **Legal/PR**: compliant disclosure and external communication.
- **Engineering**: root-cause fix and regression verification.

---

## 7. Retrospective and improvement

After every incident: review root cause, impact, response timeliness, and
improvements; fold them into process/standard revisions and training.

---

*This policy ensures incidents are responded to and learned from promptly and
properly.*
