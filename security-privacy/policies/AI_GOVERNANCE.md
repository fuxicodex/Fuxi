# FuXi AI Governance Policy

*Last updated: 2026-08-23 · Version 1.0 · Layer: L1 Policy*

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
| **Refuse misuse** | No assistance with destructive, offensive, or unlawful use |

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

## 6. Responsibility boundaries

- **We are responsible for**: FuXi's own security mechanisms, permission model,
  routing, and update integrity.
- **Model providers are responsible for**: underlying model behavior, data, and
  compliance (their own policies apply).
- **Users are responsible for**: task selection, output review, and final
  decisions on critical operations.

---

## 7. Compliance alignment

- Honor widely applicable AI and data protection principles (transparency,
  fairness, accountability, human-in-the-loop).
- No fabricated "AI safety certifications"; capability boundaries are disclosed
  honestly.

---

*This policy ensures FuXi, as an AI product, serves users responsibly, safely,
and under control.*
