# FuXi Compliance & Responsibility Statement

*Last updated: 2026-09-12 · Version 1.0*

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

The universal principles above are our **floor**, applied worldwide. The table
below maps how they land in a few major jurisdictions; it is a non-exhaustive
illustration, not a jurisdiction-specific legal commitment or an endorsement of
any single country's law.

**Major-jurisdiction perspective (principles alignment, not certification)**

| Law / jurisdiction | Account-related obligations we map to | FuXi posture |
|---|---|---|
| EU — GDPR | Lawful basis, controller obligations, DSR (Art. 15–21), breach notification (Art. 33/34) | Account processing on a contractual basis; DSR handled via the documented procedure; zero content upload keeps breach scope minimal |
| China — PIPL | Consent / legal basis, DSR, cross-border transfer rules | Minimal account data; user rights honored; no content upload; cross-border only via user-chosen provider |
| USA — CCPA/CPRA | Right to know / delete / opt-out, "sale or share" restrictions | We do not sell or share personal data; zero content upload |
| Brazil — LGPD | Legal basis, DSR, ANPD interaction | Same universal baseline |
| Other jurisdictions | Similar minimization, rights, and security obligations | Same baseline; specific obligations follow the law applicable to us |

Because a FuXi account is **required**, account-data processing is subject to
the data-protection law applicable where the account is operated. We keep that
data minimal, honor your rights, and review this statement as laws evolve — this
is alignment with principles, not a claim of certification.

The full jurisdiction-by-jurisdiction analysis — scope triggers, the duties that
bind us, and a disclosed risk register — is in the
[Global Privacy & Legal Risk Map](compliance/GLOBAL_LAW_MAP.md).

---

## 4. Lawful use is a condition of use

**You must use FuXi in accordance with the laws applicable to you.** This is a
condition of using FuXi, not a suggestion:

- You are responsible for complying with the laws of your country/region,
  data-protection law, and any sectoral rules that apply to your work.
- Disallowed uses are listed in the
  [Usage Policy](policies/ACCEPTABLE_USE.md); among them are unlawful, harmful,
  deceptive, or privacy-violating uses.
- FuXi's technical capability is not permission: if a use is unlawful where you
  are, you must not use FuXi for it.
- If you are unsure whether a use is lawful, take advice before proceeding.

---

## 5. Responsibility boundaries

We draw clear lines to avoid misleading you:

- **We are responsible for**: the local security mechanisms of the FuXi binary
  itself, update integrity, documentation honesty, and the account
  authentication and account-data processing that are required to use FuXi.
- **You are responsible for**: your lawful use of FuXi (see §4), your machine's
  security, file-system permissions, and the choice and safeguarding of
  providers / MCP servers / plugins you configure.
- **Third parties are responsible for**: the privacy and data-processing
  behavior of the model providers, MCP servers, and plugins you connect to.

---

## 6. Disclaimers and honest disclosure

- FuXi may execute commands that affect local files; we reduce risk through the
  permission model and command safety classifier, but we cannot underwrite the
  consequences of fully autonomous / permission-skipping operation.
- Model output may be inaccurate; please review and verify critical operations
  yourself.
- We are not responsible for the behavior of third-party services you choose to
  connect.

---

## 7. Commitment checklist (honest, verifiable)

| # | Commitment | How to verify |
|---|---|---|
| 1 | No code/conversation collection | Content is never collected, stored, or retained; BYOK goes directly to your provider |
| 2 | Keys are not uploaded | Credentials stored only in local `~/.fuxi/` |
| 3 | Updates are verifiable | `fuxi update` SHA-256 check + atomic replacement |
| 4 | Command safety | Pre-execution AST classifier + permission prompts + audit logs |
| 5 | Transparency | Data flows and responsibility boundaries disclosed in this document set |
| 6 | Lawful use required | Users must comply with applicable law (see [Usage Policy](policies/ACCEPTABLE_USE.md)) |

---

## 8. Contact us

- Website: https://www.fuxicode.com
- Repository: https://github.com/fuxicodex/Fuxi
- Compliance / privacy matters: reach us via the repository issue tracker or
  the contact details published on the website.

---

*FuXi is secure by design, protecting its users — honest, transparent, and in
your control.*
*Entity: FUXI*
