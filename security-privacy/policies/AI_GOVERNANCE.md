# FuXi AI Governance Policy

*Last updated: 2026-09-12 · Version 1.0 · Layer: L1 Policy*

This policy describes how FuXi, as an AI coding agent, operates under principles
of **responsibility, safety, and control**. FuXi itself is the "vehicle"; the
model is the "engine". This policy governs their combination.

---

## 1. Positioning: the model is the engine, FuXi is the vehicle

- FuXi does **not train or host** the underlying general-purpose models; it turns
  the model the user chooses into a "worker" that reasons, acts, and verifies.
- Model output may be inaccurate or biased; FuXi reduces risk through the
  **think → act → verify** loop, but final judgment and responsibility rest with
  the user.

---

## 2. AI safety principles

| Principle | Implementation |
|---|---|
| **Human in the loop** | Sensitive operations require approval; user can interrupt or revoke anytime |
| **Explainable & traceable** | Every action is traceable via audit logs |
| **Safety guardrails** | Commands filtered by AST classifier + rule set |
| **No implicit escalation** | Permission model defaults to least privilege |
| **Refuse misuse** | No assistance with destructive, offensive, or unlawful use; see the [Usage Policy](ACCEPTABLE_USE.md) |

---

## 3. Model routing and transparency

- **Intelligent routing**: requests are scored by complexity and routed to the
  right model tier, balancing cost and quality.
- **Observable**: `/model`, `/status`, `/context`, `/cost` keep the user informed
  of which model is used, at what cost, and context usage.
- **Bring your own key**: the user controls which provider and model are used;
  data flows are transparent.

---

## 4. Output safety and verification

- Model output is **not treated as fact**; users should review critical
  operations (file edits, commands, commits, releases) before confirming.
- Tests, builds, and checks are driven by FuXi, but the final "green light"
  should be confirmed by the user.

---

## 5. Fairness and non-discrimination

- FuXi does not unreasonably differentiate based on identity, region, or
  language.
- For potentially biased model output, transparent routing and verifiable
  processes let users detect and correct it.

---

## 6. Children and young users of an AI tool

FuXi is aimed at developers and professional users and is **not directed at
children under 14**; users aged 14–17 require the involvement of a parent or
guardian (see [Privacy Policy §8](../PRIVACY_POLICY.md)):

- Consent from a parent/guardian where the law requires it.
- No behavioural advertising or profiling, minimal data, and the same
  deny-by-default safety as every user.
- We recommend adult supervision, because AI output can be wrong and FuXi can
  run commands.

---

## 7. AI-tool usage law

FuXi is used across jurisdictions with AI-specific rules, and we align to their
common expectations:

| Regime | Expectation | FuXi posture |
|---|---|---|
| EU AI Act | Transparency about AI involvement; risk management for higher-risk uses | The user is always told they are working with an AI agent; human-in-the-loop and audit logs; honest capability claims |
| China — Generative AI Measures | Content safety, lawful data use, clear service identity | Service identity is explicit; safety guardrails; no content upload |
| US FTC §5 | Truthful claims; no deceptive AI behaviour | No fabricated certifications or overstated capabilities |
| Children's codes (e.g., UK ICO Age-Appropriate Design Code; California AADC) | Best interests of the child; high privacy by default | Privacy-by-default for all users; no profiling or behavioural ads; data minimization |

Because a FuXi account is required, the applicable AI rules are those of the
jurisdiction where the account is offered and operated; where they differ, the
stricter expectation is our internal standard.

---

## 8. User reliance and honest limits

Trust must be accurate, so we state our limits plainly:

- FuXi is a **tool**, not a professional adviser. Output must not be relied on as
  legal, medical, financial, or safety advice.
- Automated output can be wrong; users (and, for minors, their guardians) should
  review before acting, and confirm critical operations themselves.
- FuXi does not make autonomous decisions about a user's rights or obligations:
  sensitive actions require approval, and every action is auditable.
- We never represent that FuXi guarantees correct or complete results.

---

## 9. Responsibility boundaries

- **We are responsible for**: FuXi's own security mechanisms, permission model,
  routing, and update integrity.
- **Model providers are responsible for**: underlying model behavior, data, and
  compliance (their own policies apply).
- **Users are responsible for**: task selection, output review, and final
  decisions on critical operations.

---

## 10. Compliance alignment

- Honor widely applicable AI and data protection principles (transparency,
  fairness, accountability, human-in-the-loop).
- No fabricated "AI safety certifications"; capability boundaries are disclosed
  honestly.

---

*This policy ensures FuXi, as an AI product, serves users responsibly, safely,
and under control.*
