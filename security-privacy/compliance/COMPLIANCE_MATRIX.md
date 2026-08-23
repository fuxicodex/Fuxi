# FuXi Global Compliance Matrix

*Last updated: 2026-08-23 · Version 1.0 · Layer: L4 Compliance*

This matrix maps FuXi's privacy and security practices to the **common
principles** of major global privacy/data/AI laws. **Honesty statement**: this
matrix shows *principle alignment*, not a claim of certification or a compliance
conclusion; specific obligations follow the applicable jurisdiction and the laws
actually applicable to FuXi.

---

## 1. Referenced laws and frameworks

| Abbr. | Full name | Jurisdiction |
|---|---|---|
| GDPR | General Data Protection Regulation | EU/EEA |
| UK GDPR | UK General Data Protection Regulation | UK |
| PIPL | Personal Information Protection Law | China |
| CCPA/CPRA | California Consumer Privacy Act / California Privacy Rights Act | California, USA |
| LGPD | Lei Geral de Proteção de Dados | Brazil |
| PIPEDA | Personal Information Protection and Electronic Documents Act | Canada |
| PDPA | Personal Data Protection Act | Singapore |
| APP | Australian Privacy Principles (Privacy Act) | Australia |
| EU AI Act | Artificial Intelligence Act | EU |

---

## 2. Common principles mapping

| Common principle | FuXi practice | Document |
|---|---|---|
| Data minimization | Process only necessary data; local-first | [Privacy Policy](../PRIVACY_POLICY.md), [Data Classification](DATA_CLASSIFICATION.md) |
| Purpose limitation | Use only for stated purposes | Privacy Policy |
| Transparency | Honest disclosure of data flows and responsibility | All documents |
| User rights (access/rectify/erase) | Exercise channels; local data user-controlled | [DSR Procedure](../procedures/DATA_SUBJECT_REQUEST.md) |
| Security obligation | Command classifier, permission model, update verification | [Security Whitepaper](../SECURITY.md) |
| Breach notification | Severity tiers and notification duty | [Incident Response Policy](INCIDENT_RESPONSE.md) |
| Cross-border transfer | None by default; BYOK is user's choice | [Transfer Assessment](TRANSFER_ASSESSMENT.md) |
| Children protection | Not child-directed; no knowing collection under 16 | Privacy Policy §8 |
| AI accountability (human-in-the-loop, transparent) | Think→Act→Verify, permission model, audit | [AI Governance Policy](AI_GOVERNANCE.md) |

---

## 3. Architectural advantage: meeting most requirements naturally

- **Local-first + bring your own key** = by default we **do not hold** user code
  or conversations → most "collect, store, share, delete" obligations dissolve
  (nothing collected, nothing to violate).
- **No forced registration** = no identity data processed by default.
- **Explicit permissions + audit** = satisfies "human-in-the-loop" and
  "accountability".

---

## 4. How we stay aligned

1. Review this matrix semiannually, adding new laws/jurisdictions.
2. Material legal changes trigger policy and procedure revisions.
3. Disclose via transparency report and trust center.

---

## 5. Boundary statement

- This matrix does **not** claim any certification or regulatory endorsement.
- Third parties users connect (model providers/MCP/plugins) are responsible for
  their own compliance; FuXi discloses them honestly and the user chooses.

---

*This matrix is FuXi's tool for respecting global law and continuous
improvement.*
