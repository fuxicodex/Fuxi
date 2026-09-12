# FuXi Global Compliance Matrix

*Last updated: 2026-09-12 · Version 1.0 · Layer: L4 Compliance*

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
| CSL / DSL | Cybersecurity Law / Data Security Law | China |
| CCPA/CPRA | California Consumer Privacy Act / California Privacy Rights Act | California, USA |
| VCDPA / CPA / CTDPA / UCPA / TDPSA | Virginia / Colorado / Connecticut / Utah / Texas consumer privacy acts | Other US states |
| FTC Act §5 / COPPA | Federal Trade Commission Act / Children's Online Privacy Protection Act | USA (federal) |
| LGPD | Lei Geral de Proteção de Dados | Brazil |
| PIPEDA / Law 25 | Personal Information Protection and Electronic Documents Act / Quebec Law 25 | Canada |
| DPDP Act | Digital Personal Data Protection Act 2023 | India |
| APPI | Act on the Protection of Personal Information | Japan |
| PIPA | Personal Information Protection Act | South Korea |
| Singapore PDPA / Thailand PDPA | Personal Data Protection Act | Singapore (3 days) / Thailand (72 hours) |
| Privacy Act + APPs | Privacy Act and Australian Privacy Principles | Australia |
| POPIA | Protection of Personal Information Act | South Africa |
| FADP | Federal Act on Data Protection | Switzerland |
| 152-FZ | Federal Law on Personal Data | Russia |
| EU AI Act | Artificial Intelligence Act | EU |
| Generative AI Measures | Interim Measures for Generative AI Services | China |

---

## 2. Common principles mapping

| Common principle | FuXi practice | Document |
|---|---|---|
| Data minimization | Process only necessary data; local-first | [Privacy Policy](../PRIVACY_POLICY.md), [Data Classification](../policies/DATA_CLASSIFICATION.md) |
| Purpose limitation | Use only for stated purposes | Privacy Policy |
| Transparency | Honest disclosure of data flows and responsibility | All documents |
| User rights (access/rectify/erase) | Exercise channels; local data user-controlled | [DSR Procedure](../procedures/DATA_SUBJECT_REQUEST.md) |
| Security obligation | Command classifier, permission model, update verification | [Security Whitepaper](../SECURITY.md) |
| Breach notification | Severity tiers and notification duty | [Incident Response Policy](../policies/INCIDENT_RESPONSE.md) |
| Cross-border transfer | User content not transferred by FuXi; account data may transfer to the account-service region | [Transfer Assessment](TRANSFER_ASSESSMENT.md) |
| Children protection | Not directed at children under 14; 14–17 require a parent/guardian; no behavioural ads/profiling | [Privacy Policy §8](../PRIVACY_POLICY.md) |
| AI accountability (human-in-the-loop, transparent) | Think→Act→Verify, permission model, audit | [AI Governance Policy](../policies/AI_GOVERNANCE.md) |

---

## 3. Obligation-level mapping (the duties that actually bind us)

Because an account is required, FuXi is a **controller** for account data. The
table maps the concrete obligations that follow, and how each is met. For the
jurisdiction-by-jurisdiction view and the risk register, see the
[Global Law Map](GLOBAL_LAW_MAP.md).

| Obligation | Typical source | FuXi's implementation |
|---|---|---|
| Lawful basis | GDPR Art. 6; PIPL Art. 13; LGPD Art. 7 | Performance of the service contract for account data; consent where required |
| Notice / transparency | GDPR Art. 13–14; PIPL Art. 17; CCPA §1798.100 | [Privacy Policy](../PRIVACY_POLICY.md) + this document set |
| Access / portability | GDPR Art. 15, 20; CCPA; DPDP | [DSR Procedure](../procedures/DATA_SUBJECT_REQUEST.md) |
| Rectification | GDPR Art. 16; LGPD Art. 18 | Account settings / DSR channel |
| Erasure | GDPR Art. 17; CCPA; PIPL Art. 47 | Local data: `rm -rf ~/.fuxi`; account data: on request |
| Object / restrict | GDPR Art. 18, 21; LGPD | DSR channel |
| Breach notification | GDPR Art. 33/34 (72h); Singapore PDPA (3 days); Thailand PDPA (72h); AU NDB | [Incident Response Policy](../policies/INCIDENT_RESPONSE.md), strictest target applied |
| Security of processing | GDPR Art. 32; PIPL Art. 51 | [Information Security Policy](../policies/INFORMATION_SECURITY_POLICY.md) |
| Records & assessments | GDPR Art. 30, 35; DPDP (SDF) | [ROPA](ROPA.md) · [DPIA](DPIA.md) |
| Cross-border transfer | GDPR Ch. V; PIPL Ch. 3; 152-FZ | [Transfer Assessment](TRANSFER_ASSESSMENT.md); mechanism per region |
| Local representation | GDPR Art. 27; UK; PIPA (KR) | Appointed where required; published on the official website |
| Children | GDPR Art. 8; COPPA; PIPL Art. 31; DPDP | Not directed at under-14s; 14–17 require a parent/guardian; no ads/profiling; minimal data |
| AI transparency | EU AI Act; China generative-AI rules | Human-in-the-loop, permission model, honest capability claims ([AI Governance](../policies/AI_GOVERNANCE.md)) |

---

## 4. Architectural advantage: meeting most requirements naturally

- **Content not held** = FuXi does not collect, store, or retain user code or
  conversations, so the "collect, store, share, delete" obligations attach to a
  far smaller data set (account data only) — not to zero obligations.
- **Required account, minimal data** = registration processes only the minimum
  account data needed to operate the account; no content is uploaded.
- **Explicit permissions + audit** = satisfies "human-in-the-loop" and
  "accountability".

---

## 5. How we stay aligned

1. Review this matrix semiannually, adding new laws/jurisdictions.
2. Material legal changes trigger policy and procedure revisions.
3. Disclose via transparency report and trust center.
4. Maintain the [Global Law Map](GLOBAL_LAW_MAP.md) risk register alongside this
   matrix, so risks are disclosed rather than assumed away.

---

## 6. Boundary statement

- This matrix does **not** claim any certification or regulatory endorsement.
- Third parties users connect (model providers/MCP/plugins) are responsible for
  their own compliance; FuXi discloses them honestly and the user chooses.

---

*This matrix is FuXi's tool for respecting global law and continuous
improvement.*
