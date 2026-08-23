# FuXi Security & Privacy Governance Charter

*Last updated: 2026-08-23 · Version 1.0 · Entity: FUXI*

This document is the **top-level governance document** of the FuXi Security &
Privacy Program ("the Program"). It defines the governance framework, policy
hierarchy, roles and responsibilities, review cadence, exception handling, and
metrics. All policies, standards, procedures, and compliance documents sit
under this Charter.

---

## 1. Governance objectives

1. **Protect users** — user privacy, data, and safety are the highest priority.
2. **Secure by default** — security is a design principle, not an afterthought.
3. **Global compliance** — respect privacy principles widely applicable across
   jurisdictions.
4. **Honesty and transparency** — claim only verifiable capabilities; never
   fabricate certifications.
5. **Continuous improvement** — evolve through review, metrics, and incident
   learning.

---

## 2. Policy hierarchy

The Program uses a layered structure, from principle to execution:

```
L0  Governance Charter (this file) — top-level objectives & governance
├── L1  Policies          — "what must be done" (normative)
│     ├── Information Security Policy
│     ├── Privacy Policy
│     ├── Data Classification Policy
│     ├── Access Control Policy
│     ├── AI Governance Policy
│     ├── Incident Response Policy
│     ├── Third-Party Risk Policy
│     └── Business Continuity Policy
├── L2  Standards         — "how it is done" (technical norms)
│     ├── Cryptography Standard
│     ├── Authentication Standard
│     ├── Logging & Monitoring Standard
│     └── Secure Development Standard (SDLC / AI safety)
├── L3  Procedures        — "step by step" (runbooks)
│     ├── Incident Response Runbook
│     ├── Vulnerability Disclosure (CVD / bounty)
│     ├── Data Subject Request Handling
│     └── Backup & Recovery
├── L4  Compliance        — mapping to global law
│     ├── Global Compliance Matrix
│     ├── Privacy Impact Assessment (DPIA)
│     ├── Records of Processing (ROPA)
│     └── Transfer Impact Assessment (TIA)
└── L5  Trust             — user-facing trust disclosures
      ├── Trust Center
      ├── Subprocessors List
      └── Transparency Report
```

**Conflict resolution**: where a lower-level document conflicts with a higher
one, the higher prevails. Where the Program conflicts with applicable law, the
law prevails and the Program is updated accordingly.

---

## 3. Roles and responsibilities (RACI)

> R = Responsible · A = Accountable · C = Consulted · I = Informed

| Domain | R | A | C | I |
|---|---|---|---|---|
| Security architecture & threat model | Security engineering | Security lead | Eng, Product | All |
| Privacy & data processing | Privacy team | Privacy lead (DPO or equivalent) | Legal, Security | Users, regulators |
| Incident response | Incident response team | Security lead | Legal, PR | Affected users |
| Vulnerability disclosure | Security engineering | Security lead | Legal | Reporter, community |
| Third-party / supply chain | Procurement & Eng | Compliance lead | Security, Legal | — |
| Compliance mapping & audit | Compliance team | Compliance lead | Legal | Management |
| Policy maintenance & versioning | Governance team | Governance lead | All | All |

---

## 4. Review and maintenance cadence

| Object | Frequency | Triggers |
|---|---|---|
| Governance Charter | Annually | Major strategic change |
| Policies | Annually | Law changes, major product change, security incident |
| Standards | Annually | Tech-stack change, new threats |
| Procedures | Semiannually | Drill findings, incident retrospectives |
| Compliance matrix | Semiannually | New laws, new jurisdictions |
| Trust Center | Continuous | Any material change |

Every revision must: record the reason, bump version and date, obtain approval
from the accountable lead, and be published.

---

## 5. Exception handling

Any request to deviate from a policy/standard must:

1. be submitted in writing with rationale, scope, duration, and risk;
2. be assessed and approved in writing by the accountable lead;
3. be recorded in an exception log with a review date;
4. expire automatically if not reviewed by that date.

Exceptions must not be used to avoid legal obligations or harm user rights.

---

## 6. Metrics

The Program is measured by:

| Metric | Target |
|---|---|
| Vulnerability report first-response time | within a few working days |
| Critical vulnerability remediation time | promptly; fix before disclosure |
| Incident detection-to-response time | per runbook SLA |
| Data subject request turnaround | per applicable law (e.g., 30 days) |
| On-time policy review completion | 100% |
| Staff/contributor security training coverage | 100% |

---

## 7. Scope

This Program applies to FuXi's official binary, website, repository, and related
services. Third parties users actively connect (model providers, MCP servers,
plugins) follow their own policies; see the related documents.

---

*This Charter is FuXi's governance commitment to being secure by design,
protecting its users, and respecting global law.*
