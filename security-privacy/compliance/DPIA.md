# FuXi Data Protection Impact Assessment (DPIA)

*Last updated: 2026-08-23 · Version 1.0 · Layer: L4 Compliance*

This document is a **methodology framework** for systematically assessing and
reducing privacy risk before introducing features/processing that may pose a
high risk to user privacy.

---

## 1. When to trigger a DPIA

A DPIA should be performed for:

- introduction of a new processing activity;
- a material change in the nature of processing;
- adoption of new technology (e.g., new AI capability, new data flows);
- high-risk automated decision-making (if applicable).

---

## 2. DPIA steps

1. **Describe the processing**: what data, why, how, who can access, how long
   retained.
2. **Assess necessity & proportionality**: can less be collected? Is the purpose
   clear and legitimate?
3. **Identify risks**: risks to users' rights and freedoms (confidentiality,
   integrity, availability, autonomy).
4. **Design mitigations**: technical + organizational measures to reduce risk.
5. **Record & approve**: produce a DPIA report, approved by the privacy lead.
6. **Monitor**: review periodically, update on change.

---

## 3. Risk and mitigation mapping

| Risk | FuXi's mitigation |
|---|---|
| User code/conversations collected | Local-first + BYOK: not held, not routed through servers by default |
| Credential leak | Local-only storage, never uploaded, disk encryption recommended |
| Malicious command execution | AST classifier + permission prompts + audit |
| Biased/inaccurate model output | Think→Act→Verify, human-in-the-loop |
| Improper third-party handling | Off by default, user's choice, honest disclosure |

---

## 4. Conclusion template

```
Processing activity: ________
Necessity: ________ (minimization confirmed)
Main risks: ________
Mitigations: ________
Residual risk level: low / medium / high
Approver: ________  Date: ________
Review date: ________
```

---

## 5. Record keeping

- DPIA reports are kept in the compliance log and updated with product changes.
- High-residual-risk processing requires privacy-lead approval before
  deployment.

---

*This document ensures FuXi proactively identifies and reduces privacy risk
before introducing new processing.*
