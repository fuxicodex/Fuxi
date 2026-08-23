# FuXi Compliance & Responsibility Statement

*Last updated: 2026-08-23 · Version 1.0*

This statement explains, for users worldwide, FuXi's legal-framework
alignment, responsibility boundaries, and honest commitments. **We are honest:
we do not fabricate certifications, overstate capabilities, or claim what we
have not done.**

---

## 1. Our stance

FuXi is a local-first terminal AI coding agent. Our compliance and privacy
stance rests on three unchanging principles:

1. **Honesty** — we claim only what we actually do, and never mislead users
   under the guise of "certification" or "compliance".
2. **Transparency** — data flows, capability boundaries, and responsibility
   scopes are described truthfully.
3. **User-centricity** — privacy and safety are the design starting point, not
   a compliance floor.

---

## 2. Honest note on "certifications"

We do **not** claim any third-party security or privacy certification (e.g.,
ISO 27001, SOC 2, GDPR certification) unless we have actually obtained it and
published it on the website and in documentation.

Our security claims come from the **architecture itself** (local-first, command
safety classifier, checksum-verified updates, explicit permissions). These are
verifiable through use, audit logs, and self-checks such as `fuxi doctor` —
rather than relying on a certificate.

---

## 3. Legal-framework alignment

FuXi serves users worldwide, and we strive to honor widely applicable data
protection principles — data minimization, purpose limitation, transparency,
user rights, and security obligations — which are common to mainstream privacy
laws (e.g., GDPR and various personal-information protection laws). Specific
obligations follow the jurisdiction you are in and the laws actually applicable
to us.

**No jurisdiction-specific special commitments beyond the universal principles**
— this is a global, principles-based statement and does not endorse any single
country's law.

---

## 4. Responsibility boundaries

We draw clear lines to avoid misleading you:

- **We are responsible for**: the local security mechanisms of the FuXi binary
  itself, update integrity, documentation honesty, and (when you use the
  sign-in feature) account-authentication processing.
- **You are responsible for**: your machine's security, file-system permissions,
  and the choice and safeguarding of providers / MCP servers / plugins you
  configure.
- **Third parties are responsible for**: the privacy and data-processing
  behavior of the model providers, MCP servers, and plugins you connect to.

---

## 5. Disclaimers and honest disclosure

- FuXi may execute commands that affect local files; we reduce risk through the
  permission model and command safety classifier, but we cannot underwrite the
  consequences of fully autonomous / permission-skipping operation.
- Model output may be inaccurate; please review and verify critical operations
  yourself.
- We are not responsible for the behavior of third-party services you choose to
  connect.

---

## 6. Commitment checklist (honest, verifiable)

| # | Commitment | How to verify |
|---|---|---|
| 1 | No code/conversation collection by default | BYOK mode content goes directly to your provider; local data stays on device |
| 2 | Keys are not uploaded | Credentials stored only in local `~/.fuxi/` |
| 3 | Updates are verifiable | `fuxi update` SHA-256 check + atomic replacement |
| 4 | Command safety | Pre-execution AST classifier + permission prompts + audit logs |
| 5 | Transparency | Data flows and responsibility boundaries disclosed in this document set |

---

## 7. Contact us

- Website: https://www.fuxicode.com
- Repository: https://github.com/fuxicodex/Fuxi
- Compliance / privacy matters: reach us via the repository issue tracker or
  the contact details published on the website.

---

*FuXi is secure by design, protecting its users — honest, transparent, and in
your control.*
*Entity: FUXI*
