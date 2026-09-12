# FuXi Global Privacy & Legal Risk Map

*Last updated: 2026-09-12 · Version 1.0 · Layer: L4 Compliance*

This document maps FuXi's practices to the **major privacy, data-protection, and
AI laws worldwide**, explains the specific risks that arise from operating a
**registered account** service, and states how we manage each one. It is written
to be comprehensive and honest: it shows **principle alignment**, not
certification, and it is **not legal advice** (see §7).

> Companion documents: [Privacy Policy](../PRIVACY_POLICY.md) ·
> [Compliance Matrix](COMPLIANCE_MATRIX.md) ·
> [Data Protection Commitment](../DATA_PROTECTION.md) ·
> [Transfer Impact Assessment](TRANSFER_ASSESSMENT.md) ·
> [ROPA](ROPA.md) · [DPIA](DPIA.md)

---

## 1. The two-zone model: where the risk actually is

The single most important fact about FuXi's legal position is that **user
content never enters FuXi's systems**. Everything else follows from that.

| Zone | What it contains | Where it lives | Who controls it |
|---|---|---|---|
| **Zone A — user content** | Source code, prompts, conversations, files, project memory, credentials | On the user's device (`~/.fuxi/`), or in direct transit to the user's chosen provider | The user |
| **Zone B — account data** | Account identifier, authentication material, minimal operational metadata | FuXi account system / official distribution | FuXi (as data controller) |

**Legal consequence**: FuXi's regulated processing footprint is confined to
**Zone B**. Because Zone A holds essentially all of the sensitive data and never
leaves the device, obligations that normally attach to "collect, store, share,
delete, breach-notify" user content apply to a **much smaller** data set — but
they do still apply to Zone B, which is why registration requires the
obligations listed in §3–§5.

**Invisible protection**: this zoning is not a setting the user must enable. It
is the default architecture, and therefore protection users receive
automatically. See the [Security Whitepaper §5](../SECURITY.md).

---

## 2. Registration makes FuXi a data controller — what changes

Before registration, FuXi was local software and processed no personal data.
With **mandatory registration**, FuXi processes account data and is therefore
a **data controller / data fiduciary / business** (terminology varies) for that
data. This is the pivotal legal change, and it brings a defined set of
obligations:

| Obligation class | What it requires | How FuXi satisfies it |
|---|---|---|
| Lawful basis | A valid basis for processing account data | Performance of the service contract; consent only where required |
| Transparency | A clear notice of what is processed and why | This document set + [Privacy Policy](../PRIVACY_POLICY.md) |
| Data-subject rights | Access, rectification, erasure, portability, objection | [DSR Procedure](../procedures/DATA_SUBJECT_REQUEST.md) |
| Security | Appropriate technical and organizational measures | [Information Security Policy](../policies/INFORMATION_SECURITY_POLICY.md) |
| Breach notification | Notify authorities and/or users within legal deadlines | [Incident Response Policy](../policies/INCIDENT_RESPONSE.md) |
| Accountability | Records, assessments, reviews | [ROPA](ROPA.md) · [DPIA](DPIA.md) · [Governance](../governance/GOVERNANCE.md) |
| Representation | A local representative where required | Disclosed on the official website (see §5) |

---

## 3. Jurisdiction-by-jurisdiction map

The table gives each major law's **scope trigger**, its **core obligations that
touch FuXi**, and our **risk rating** for that jurisdiction (how much of the law
actually reaches us). Detail follows the table.

| Jurisdiction | Law | Scope trigger | Obligations that touch FuXi | Risk |
|---|---|---|---|---|
| EU/EEA | GDPR | Offering services to / monitoring people in the EU, even without an EU establishment | Controller duties, Art. 27 representative, DSR (1 month), breach notice (72h), transfers (Chapter V) | **Medium** |
| UK | UK GDPR + DPA 2018 | Same, for the UK | Mirrors GDPR; UK representative; ICO oversight | **Medium** |
| China | PIPL, DSL, CSL | Processing personal info of people in China, including from abroad | Separate consent for sensitive PI, cross-border transfer mechanism, breach notice, localization for CIIOs | **High** |
| USA — California | CCPA/CPRA | Doing business in CA + thresholds | Know/delete/correct/opt-out/limit, 45-day response, no sale of minors' data | **Medium** |
| USA — other states | VCDPA, CPA, CTDPA, UCPA, TDPSA, etc. | State-specific thresholds | Similar rights; consent for sensitive data; opt-out of targeted ads/profiling | **Medium** |
| USA — federal | FTC Act §5, COPPA | Unfair/deceptive practices; children under 13 | Truthful claims, security reasonableness, children's consent | **Low–Medium** |
| Brazil | LGPD | Processing data of people in Brazil | Legal bases, DSR (~15 days), ANPD, breach notice | **Medium** |
| Canada | PIPEDA + Quebec Law 25 | Commercial activity in Canada | Consent, 30-day DSR, breach reporting (real risk of significant harm); QC privacy-by-default | **Medium** |
| India | DPDP Act 2023 | Processing digital personal data of people in India | Consent, notice, data-principal rights, children's verifiable consent, SDF duties | **High** |
| Japan | APPI | Handling personal information of people in Japan | Consent + info for cross-border transfer, breach notice to PPC and individuals | **Medium** |
| South Korea | PIPA | Processing data of people in Korea | Strict consent, cross-border disclosure, breach notice, high fines | **Medium–High** |
| Australia | Privacy Act + APPs | Australian individuals | 13 APPs, Notifiable Data Breaches scheme, APP 8 cross-border accountability | **Medium** |
| Singapore | PDPA | Collecting/using data in Singapore | Consent, mandatory DPO, breach notice within 3 days | **Medium** |
| South Africa | POPIA | Processing data of people in South Africa | 8 conditions, Information Regulator, breach notice | **Low–Medium** |
| Switzerland | Revised FADP | Processing data of people in Switzerland | GDPR-like duties, FDPIC, breach notice | **Low–Medium** |
| Other | See §3.3 | Varies | Listed and monitored; principles-level alignment | **Monitored** |

### 3.1 Detail for the highest-touch jurisdictions

**EU/EEA — GDPR.** Because FuXi offers its service to users in the EU, GDPR can
apply even without an EU establishment (Art. 3(2)). The obligations that
realistically reach us: a lawful basis for account data (we use performance of
the contract), an **Art. 27 representative** where required, DSR responses
within one month, **breach notification to the supervisory authority within 72
hours**, a DPIA for high-risk processing, and Chapter V safeguards for any
transfer of account data. **Note**: PIPL/EU-style transfer mechanisms are the
main open item when account infrastructure is located outside a user's region;
this is disclosed and handled on the official website.

**China — PIPL (with CSL and DSL).** PIPL applies to processing the personal
information of people in China, including processing performed abroad. The
obligations that reach us: notice and consent (with **separate consent** for any
sensitive personal information), a lawful cross-border transfer mechanism
(security assessment, certification, or a filed standard contract), breach
notification to authorities and affected individuals, and — for critical
information infrastructure operators and volumes above regulatory thresholds —
**data localization**. Because FuXi's Zone B is minimal, our exposure is small,
but localization and transfer mechanisms must be chosen deliberately.

**India — DPDP Act 2023.** Consent-based, with a notice obligation, data-principal
rights, **verifiable parental consent for children** (under 18, with exemptions),
and enhanced duties for Significant Data Fiduciaries (DPO, audits, DPIAs). Our
minimal Zone B keeps obligations tractable.

**USA — California CCPA/CPRA and the state-law wave.** CCPA/CPRA gives consumers
the rights to know, delete, correct, opt out of sale/share, and limit use of
sensitive personal information, with a 45-day response window; we do not sell or
share personal data. A growing set of state laws (Virginia, Colorado,
Connecticut, Utah, Texas, and others) adds similar rights. At the federal level,
the FTC Act §5 requires that our public claims be truthful (we apply this
strictly — see §6) and COPPA governs children under 13.

### 3.2 Children and AI-tool rules

FuXi **may be used by children and young people**, so two bodies of law apply
together: children's privacy rules and AI-tool rules.

- **Age of digital consent varies** — GDPR 16 (or lower by member state), US
  COPPA 13, China 14, Korea 14, India 18. We apply the stricter rule where the
  jurisdiction is known, and require guardian consent below the threshold.
- **Children's design codes** (UK ICO AADC; California AADC; GDPR Art. 8
  expectations) call for the best interests of the child and high privacy by
  default. We meet this with privacy-by-default for all users, no behavioural
  advertising or profiling, and data minimization.
- **AI-tool rules** — the EU AI Act's transparency expectations, China's
  generative-AI measures, and FTC §5 truthfulness apply to how an AI agent is
  presented. The user is always told they are working with an AI agent, and we
  never overstate its reliability (see the
  [AI Governance Policy §6–§8](../policies/AI_GOVERNANCE.md)).

### 3.3 Additional jurisdictions monitored

We also track, at principles level: Russia (152-FZ, data localization), UAE and
Saudi Arabia (PDPL), Thailand and Malaysia (PDPA), Indonesia (PDP Law), Vietnam
(PDPD), the Philippines (DPA), Mexico (LFPDPPP), Argentina (PDPA), and New
Zealand (Privacy Act). New laws are added to the matrix on the semiannual review
cycle (see [Compliance Matrix §5](COMPLIANCE_MATRIX.md)).

---

## 4. Global legal risk register

This is the honest list of risks, with the mitigation we rely on. We disclose
risks rather than claim they do not exist.

| # | Risk | Where it bites | Mitigation |
|---|---|---|---|
| R1 | **Registration creates controller duties** | Worldwide | Minimal Zone B; documented lawful basis; DSR procedure; this map |
| R2 | **Cross-border transfer of account data** | EU/UK, China, India, Russia | Transfer mechanism chosen per region; localization where required; TIA documented |
| R3 | **Data-localization mandates** | China (CIIO/thresholds), Russia | Minimal data; regional deployment options; disclosed residency |
| R4 | **Divergent breach-notification deadlines** | GDPR 72h; Singapore 3 days; AU/ZA "ASAP" | Single strictest internal target (P0 → notify promptly) so we meet every regime |
| R5 | **Representative / DPO requirements** | EU (Art. 27), UK, Korea, India (SDF) | Appointed where required; published on the official website |
| R6 | **Children / age thresholds differ** | GDPR 16 (default), US 13, China 14, Korea 14, India 18 | Minors may use FuXi, so we apply age-appropriate safeguards: guardian consent where required, no behavioural ads/profiling, minimal data, and recommended adult supervision |
| R7 | **AI-specific obligations** | EU AI Act (transparency), China generative-AI rules | Human-in-the-loop (Think→Act→Verify), permission model, honest capability claims |
| R8 | **Government / lawful-access requests** | All jurisdictions | We can only disclose what we actually hold (Zone B); disclosed in the Transparency Report |
| R9 | **Marketing / consent hygiene** | EU ePrivacy, others | No unsolicited marketing; consent where required; easy withdrawal |
| R10 | **Over-claiming** (the compliance risk we fear most) | All jurisdictions | No fabricated certifications; every claim verifiable; §6 rules |

---

## 5. How we manage these risks

1. **Minimize Zone B relentlessly.** The smaller the account data, the smaller
   every obligation becomes. This is the primary control.
2. **Choose transfer mechanisms deliberately** and disclose residency; use
   localization where a jurisdiction requires it.
3. **Apply the strictest deadline globally internally**, so we satisfy the
   tightest regime everywhere.
4. **Appoint representatives/DPOs** where the law requires, and publish them.
5. **Review semiannually**, adding new laws and jurisdictions; material legal
   changes trigger policy and procedure revisions.
6. **Never claim a certification we do not hold.** See §6.

Where the law requires more than this document states, the law prevails, and we
update the program (see [Governance §2](../governance/GOVERNANCE.md)).

---

## 6. Honesty rules for legal claims

To avoid the most common compliance failure — **over-claiming** — we hold to
these rules:

- We describe **principle alignment**, never "certified compliant" unless a
  certification is actually held and published.
- We state where a risk exists rather than implying it does not.
- We do not claim an absolute ("fully compliant worldwide") that no single
  document can substantiate.
- Every claim here is traceable to a mechanism described in this document set.

---

## 7. Boundary statement

- This map is **not legal advice** and does not create rights beyond those the
  applicable law grants.
- Specific obligations follow the jurisdiction and the laws **actually
  applicable to FuXi**; where they differ from this summary, the law prevails.
- Third parties the user chooses (model providers, MCP servers, plugins) are
  responsible for their own compliance; we disclose them honestly (see
  [Third-Party Risk Policy](../policies/THIRD_PARTY_RISK.md)).

---

*This map is FuXi's tool for respecting global law, disclosing real risks, and
improving continuously.*
