# FuXi Information Security Policy

*Last updated: 2026-08-23 · Version 1.0 · Layer: L1 Policy*

This policy is the **umbrella** of the FuXi information security program,
providing the normative basis for all standards, procedures, and operations.
Other policies refine it.

---

## 1. Objective

Protect the **confidentiality, integrity, and availability (CIA)** of user and
FuXi information.

---

## 2. Core security stance

FuXi's security comes from **the architecture itself**, not bolt-on defenses:

- **Local-first**: code, configuration, credentials, and sessions stay on the
  user's device by default, minimizing server-side attack surface.
- **Distrust by default**: commands, files, and external input are validated
  before execution.
- **Explicit permissions**: sensitive operations require user approval; no
  implicit escalation.
- **Least privilege**: only the minimum capability needed for a task is used.
- **Verifiable**: updates are checksum-verified; behavior is auditable.

---

## 3. Security control domains

| Domain | Key controls |
|---|---|
| Command safety | AST safety classifier + rule set + permission prompts + audit logs |
| Credential management | Local-only storage in `~/.fuxi/`, never uploaded; recommend file permissions + disk encryption |
| Update integrity | SHA-256 verification + atomic replacement |
| Session & data | Local storage; user-deletable at any time |
| Third-party integration | Only user-configured MCP/plugins are loaded |
| Vulnerability management | Private reporting + fix-before-disclosure (see SECURITY) |

---

## 4. Access control principles

- **Least privilege**: minimum by default, granted on demand.
- **Separation of duties**: authorization, execution, and audit are separated.
- **Explicit approval**: sensitive operations (bypass permissions, skip safety
  checks) require explicit, informed consent.
- See [Access Control Policy](ACCESS_CONTROL.md).

---

## 5. Data protection principles

- **Minimization**: process only necessary data.
- **Purpose limitation**: use only for stated purposes.
- **Local-first**: local storage by default.
- See [Privacy Policy](../PRIVACY_POLICY.md) and
  [Data Classification Policy](DATA_CLASSIFICATION.md).

---

## 6. Compliance and responsibility

- Comply with applicable law and globally accepted data protection principles.
- No fabricated certifications or overstated capabilities.
- Responsibility boundaries in
  [Compliance & Responsibility](../COMPLIANCE.md).

---

## 7. Violations and remediation

Violations are assessed by impact and trigger remediation, procedure revision,
or the incident response process. Incidents involving user data follow the
[Incident Response Policy](INCIDENT_RESPONSE.md).

---

## 8. Policy management

Reviewed annually, or on material changes in law, product, or threat landscape.
Version and change records live in the Governance Charter.

---

*This policy is the normative umbrella of the FuXi security program.*
