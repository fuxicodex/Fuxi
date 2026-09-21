# FuXi Compliance & Responsibility

*Last updated: 2026-09-12 · Version 1.0*

This document explains FuXi's legal-framework alignment, its records and
assessments, the risks we have identified, and where responsibility lies. We
state plainly what we do and what we do not claim.

> Related: [Privacy Policy](PRIVACY_POLICY.md) ·
> [Data Protection](DATA_PROTECTION.md) · [Usage Policy](USAGE_POLICY.md) ·
> [Terms of Service](TERMS_OF_SERVICE.md)

---

## 1. Our stance

1. **Honesty** — we claim only what we actually do, and never mislead under the
   guise of "certification" or "compliance".
2. **Transparency** — data flows, capability boundaries, and responsibility
   scopes are described truthfully.
3. **User-centricity** — privacy and safety are the design starting point, not a
   compliance floor.

---

## 2. Honest note on "certifications"

We do **not** claim any third-party security or privacy certification (e.g.
ISO 27001, SOC 2, a "GDPR certification") unless we have actually obtained it and
published it on the website and in the documentation.

Our security claims come from the architecture itself (local-first, command
safety classifier, checksum-verified updates, explicit permissions). These are
verifiable through use, audit logs, and self-checks such as `fuxi doctor` — rather
than relying on a certificate.

---

## 3. Lawful use is a condition of use

**You must use FuXi in accordance with the laws applicable to you.** This is a
condition of using FuXi, not a suggestion:

- You are responsible for complying with the laws of your country and region,
  data-protection law, and any sectoral rules that apply to your work.
- Disallowed uses are listed in the [Usage Policy](USAGE_POLICY.md); among them
  are unlawful, harmful, deceptive, and privacy-violating uses.
- FuXi's technical capability is not permission: if a use is unlawful where you
  are, you must not use FuXi for it.
- If you are unsure whether a use is lawful, take advice before proceeding.

---

## 4. Legal-framework alignment

FuXi serves users worldwide, and we strive to honor widely applicable data
protection principles — data minimization, purpose limitation, transparency, user
rights, and security obligations — common to mainstream privacy laws.

The universal principles are our **floor**, applied everywhere. The table below
maps how they land in major jurisdictions; it is a non-exhaustive illustration,
not a jurisdiction-specific legal commitment or an endorsement of any single
country's law.

| Jurisdiction | Law | Scope trigger | Obligations that touch FuXi | Risk |
|---|---|---|---|---|
| EU/EEA | GDPR | Offering services to / monitoring people in the EU, even without an EU establishment | Controller duties, Art. 27 representative, DSR (1 month), breach notice (72h), transfers (Chapter V) | **Medium** |
| UK | UK GDPR + DPA 2018 | Same, for the UK | Mirrors GDPR; UK representative; ICO oversight | **Medium** |
| China | PIPL, CSL, DSL | Processing personal information of people in China, including from abroad | Notice and consent (separate consent for sensitive PI), cross-border transfer mechanism, breach notice, localization for CIIOs | **High** |
| USA — California | CCPA/CPRA | Doing business in CA + thresholds | Know/delete/correct/opt-out/limit, 45-day response, no sale of minors' data | **Medium** |
| USA — other states | VCDPA, CPA, CTDPA, UCPA, TDPSA, etc. | State-specific thresholds | Similar rights; consent for sensitive data; opt-out of targeted ads/profiling | **Medium** |
| USA — federal | FTC Act §5, COPPA | Unfair or deceptive practices; children under 13 | Truthful claims, security reasonableness, children's consent | **Low–Medium** |
| Brazil | LGPD | Processing data of people in Brazil | Legal bases, DSR (about 15 days), ANPD, breach notice | **Medium** |
| Canada | PIPEDA + Quebec Law 25 | Commercial activity in Canada | Consent, 30-day DSR, breach reporting (real risk of significant harm) | **Medium** |
| India | DPDP Act 2023 | Processing digital personal data of people in India | Consent, notice, data-principal rights, verifiable parental consent for children, SDF duties | **High** |
| Japan | APPI | Handling personal information of people in Japan | Consent and information for cross-border transfer, breach notice to PPC and individuals | **Medium** |
| South Korea | PIPA | Processing data of people in Korea | Strict consent, cross-border disclosure, breach notice, high fines | **Medium–High** |
| Australia | Privacy Act + APPs | Australian individuals | 13 APPs, Notifiable Data Breaches scheme, APP 8 cross-border accountability | **Medium** |
| Singapore / Thailand | PDPA | Collecting or using data in those jurisdictions | Consent, mandatory DPO, breach notice (Singapore 3 days; Thailand 72 hours) | **Medium** |
| South Africa | POPIA | Processing data of people in South Africa | Eight conditions, Information Regulator, breach notice | **Low–Medium** |
| Switzerland | Revised FADP | Processing data of people in Switzerland | GDPR-like duties, FDPIC, breach notice | **Low–Medium** |
| Russia | 152-FZ | Processing data of people in Russia | Data localization; cross-border restrictions | **Medium** |
| Other | — | Varies | Listed and monitored; principles-level alignment | **Monitored** |

**AI-tool rules.** Two bodies of law apply together: children's privacy rules and
AI-tool rules.

- **Age of digital consent varies** — GDPR 16 (or lower by member state), US
  COPPA 13, China 14. FuXi is aimed at developers and is not directed at children
  under 14; users aged 14–17 require a parent or guardian.
- **Children's design codes** (UK ICO AADC; California AADC; GDPR Art. 8
  expectations) call for the best interests of the child and high privacy by
  default — met through privacy-by-default for all users, no behavioural
  advertising or profiling, and data minimization.
- **AI rules** — the EU AI Act's transparency expectations, China's generative-AI
  measures, and FTC §5 truthfulness apply to how an AI agent is presented. You are
  always told you are working with an AI agent, and we never overstate its
  reliability (see [Usage Policy §5](USAGE_POLICY.md)).

---

## 5. Obligation-level mapping

Because an account is required, FuXi is a **controller** for account data. The
obligations that follow, and how each is met:

| Obligation | Typical source | FuXi's implementation |
|---|---|---|
| Lawful basis | GDPR Art. 6; PIPL Art. 13; LGPD Art. 7 | Performance of the contract for account data; consent where required |
| Notice / transparency | GDPR Art. 13–14; PIPL Art. 17; CCPA §1798.100 | [Privacy Policy](PRIVACY_POLICY.md) and this document set |
| Access / portability | GDPR Art. 15, 20; CCPA; DPDP | [Data Protection §6](DATA_PROTECTION.md) |
| Rectification | GDPR Art. 16; LGPD Art. 18 | Account settings / request channel |
| Erasure | GDPR Art. 17; CCPA; PIPL Art. 47 | Local data: delete the config directory; account data on request |
| Object / restrict | GDPR Art. 18, 21; LGPD | Request channel |
| Breach notification | GDPR Art. 33/34 (72h); Singapore PDPA (3 days); Thailand PDPA (72h); AU NDB | [Operations §1](OPERATIONS.md), strictest target applied |
| Security of processing | GDPR Art. 32; PIPL Art. 51 | [Governance §2](GOVERNANCE.md) |
| Records & assessments | GDPR Art. 30, 35; DPDP (SDF) | §6 and §7 below |
| Cross-border transfer | GDPR Ch. V; PIPL Ch. 3; 152-FZ | §8 below |
| Local representation | GDPR Art. 27; UK; PIPA (KR) | Appointed where required; published on the official website |
| Children | GDPR Art. 8; COPPA; PIPL Art. 31; DPDP | Not directed at under-14s; 14–17 require a parent or guardian |
| AI transparency | EU AI Act; China's generative-AI measures | Human-in-the-loop, permission model, honest capability claims |

**Architectural advantage.** FuXi does not collect, store, or retain user code or
conversations, so the "collect, store, share, delete" obligations attach to a far
smaller data set (account data only) — not to zero obligations. Required
registration with minimal data, plus explicit permissions and audit, keeps the
regulated footprint small and the human-in-the-loop requirement satisfied.

---

## 6. Records of processing (ROPA)

**Controller**: FuXi ("FUXI"); contact via the website. Where required by law, a
local representative is appointed and published on the official website.

| # | Activity | Data categories | Purpose | Location | Basis | Retention |
|---|---|---|---|---|---|---|
| 1 | Local configuration storage | Provider config, model, key | Remember settings | User-local `~/.fuxi/` | Performance of contract | Until the user deletes it |
| 2 | Sessions & memory | Conversation history, project memory | Resume / continue | User-local | Performance of contract | Until the user deletes it |
| 3 | Audit logs | Command/tool-call records | Traceability | User-local | Legitimate interest | Until the user deletes it |
| 4 | Request sending (BYOK, user-initiated) | Prompt + code context | Enable model work | Direct user ↔ provider | User's choice (outside our scope) | Not retained by FuXi |
| 5 | Account authentication (required) | Account identifier | Operate the account; provision managed models | FuXi account system | Performance of contract | Account lifetime + 30 days |
| 6 | Update downloads | Version info | Update | Official distribution | Legitimate interest | Not retained |

**What we actually hold** is limited to the minimal account data of item 5 and the
basic update-request information of item 6. Everything else stays on your device.
Item 4 is a user-initiated direct transfer between you and your chosen provider;
FuXi relays no content, so it is listed for completeness and is outside our
processing scope.

**Recipients**: model providers and MCP servers/plugins you configure (your
choice; their policies apply), and official distribution infrastructure (minimum
necessary). This record is reviewed semiannually and updated with processing
changes.

---

## 7. Privacy impact assessment (DPIA)

**When to run one**: introduction of a new processing activity; a material change
in the nature of processing; adoption of new technology; or high-risk automated
decision-making.

**Steps**: describe the processing (what data, why, how, who can access, how long)
→ assess necessity and proportionality → identify risks to users' rights and
freedoms → design technical and organizational mitigations → record and approve →
monitor and review on change. High-residual-risk processing requires privacy-lead
approval before deployment.

**Risk and mitigation mapping**

| Risk | Mitigation |
|---|---|
| User code/conversations collected | Not collected, stored, or retained by default; conversation upload only if `send_conversations` is explicitly enabled |
| Credential leak | Local-only storage, never uploaded; disk encryption recommended |
| Malicious command execution | AST classifier + permission prompts + audit |
| Biased or inaccurate model output | Think → Act → Verify; human-in-the-loop |
| Children using an AI coding tool | Not directed at under-14s; 14–17 require a parent or guardian; no ads or profiling |
| Improper third-party handling | Off by default; your choice; honest disclosure |

**Completed example — current default state (illustrative)**

```
Processing activity: default local operation (config, sessions, memory, audit;
                     direct BYOK requests to user-chosen providers)
Necessity: yes — minimal and purpose-bound; minimization confirmed
Main risks: local device compromise; unintended command execution; transfer to a
            user-chosen third-party provider
Mitigations: permission model + AST command classifier + local audit logs;
             local-only credential storage; disk encryption recommended
Residual risk level: low (default); rises only if the user disables permission
                     checks
Approver: privacy lead   Date: 2026-09-12
Review date: 2027-03-12 (semiannual)
```

---

## 8. Cross-border transfers (TIA)

- **User content is not collected by default** — it is not collected, stored, or
  retained by FuXi unless you explicitly enable `send_conversations`. In BYOK
  mode model requests go directly to the provider you choose; with managed
  models they are transmitted only to serve that request.
- **Account data may be transferred** to the region where the FuXi account service
  is deployed (registration is required).

| Scenario | Cross-border? | Data | Driven by | Safeguards |
|---|---|---|---|---|
| Local use | No | Config/sessions/memory/audit | Local only | Local device security |
| BYOK request | Depends on provider | Prompt + code context | Your provider choice | Provider TLS + its policy |
| Account registration & sign-in | Depends on account-service region | Account identifier | Required to use FuXi | OAuth + least privilege; regional deployment where required |
| Updates | Yes (official channel) | Version info (metadata only) | Version check | HTTPS + SHA-256 |

Where we transfer account data across borders, we rely on appropriate safeguards
(for example standard contractual clauses, or separate consent where a
jurisdiction requires it). This assessment is not legal advice; specific export
obligations follow the applicable law and your jurisdiction.

---

## 9. Global legal risk register

We disclose the risks rather than assuming they do not exist.

| # | Risk | Where it bites | Mitigation |
|---|---|---|---|
| R1 | Registration creates controller duties | Worldwide | Minimal account data; documented lawful basis; request procedure |
| R2 | Cross-border transfer of account data | EU/UK, China, India | Transfer mechanism chosen per region; localization where required |
| R3 | Data-localization mandates | China (CIIO/thresholds), Russia | Minimal data; regional deployment options; disclosed residency |
| R4 | Divergent breach-notification deadlines | GDPR 72h; Singapore 3 days; Thailand 72h | Single strictest internal target |
| R5 | Representative / DPO requirements | EU (Art. 27), UK, Korea, India (SDF) | Appointed where required; published on the website |
| R6 | Children / age thresholds differ | GDPR 16, US 13, China 14 | Not directed at under-14s; 14–17 require a guardian; no ads or profiling |
| R7 | AI-specific obligations | EU AI Act; China's generative-AI measures | Human-in-the-loop; permission model; honest claims |
| R8 | Government / lawful-access requests | All jurisdictions | We can only disclose what we actually hold |
| R9 | Marketing / consent hygiene | EU ePrivacy, others | No unsolicited marketing; easy withdrawal |
| R10 | **Over-claiming** (the risk we guard against most) | All jurisdictions | No fabricated certifications; every claim verifiable |

---

## 10. Responsibility boundaries

- **We are responsible for**: the local security mechanisms of the FuXi binary,
  update integrity, documentation honesty, and the account authentication and
  account-data processing required to use FuXi.
- **You are responsible for**: your lawful use of FuXi (§3), your machine's
  security, file-system permissions, and the choice and safeguarding of the
  providers, MCP servers, and plugins you configure.
- **Third parties are responsible for**: the privacy and data-processing behavior
  of the model providers, MCP servers, and plugins you connect.

**Disclaimers.** FuXi may execute commands that affect local files; we reduce risk
through the permission model and command classifier but cannot underwrite the
consequences of fully autonomous or permission-skipping operation. Model output
may be inaccurate — review and verify critical operations yourself.

---

## 11. Commitments and contact

| # | Commitment | How to verify |
|---|---|---|
| 1 | No code/conversation collection by default | Not collected/retained unless `send_conversations` is enabled; BYOK goes directly to your provider |
| 2 | Keys are not uploaded | Credentials stored only in local `~/.fuxi/` |
| 3 | Updates are verifiable | `fuxi update` SHA-256 check + atomic replacement |
| 4 | Command safety | Pre-execution AST classifier + permission prompts + audit logs |
| 5 | Transparency | Data flows and responsibility boundaries disclosed in this document set |
| 6 | Lawful use required | Users must comply with applicable law (see [Usage Policy](USAGE_POLICY.md)) |

- Website: https://www.fuxicode.com
- Repository: https://github.com/fuxicodex/Fuxi
- Compliance and privacy matters: the contact details published on the website.

---

*This document is FuXi's tool for respecting global law, disclosing real risks,
and improving continuously.*
