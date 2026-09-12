# FuXi Privacy Policy

*Last updated: 2026-09-12 · Version 1.0*
*Entity: FUXI*

This policy applies to users worldwide and explains how and why FuXi processes
data. We write it in plain, honest language: **FuXi is designed not to collect
your code or conversation content by default.**

---

## 1. Overview: Our privacy stance

FuXi is a **terminal AI coding agent** that runs on *your own machine*. It is not
a web service hosted on our servers. That architecture sets the privacy baseline:

- **A FuXi account is required to use FuXi** — you register and sign in via
  `fuxi login` (`fuxi setup-token` in headless/CI). Registration processes only
  the minimal account data needed to operate your account and provision access
  to FuXi-managed models.
- **Zero content upload** — you never upload your code or conversations to FuXi,
  and FuXi **never collects, stores, or retains** them. Precisely:
  - *Bring your own key:* content travels **directly between your device and the
    provider you choose**; FuXi is not in the path.
  - *FuXi-managed models:* the request is transmitted to the model endpoint
    **solely to serve that request**; it is not retained by FuXi and not used to
    train models.
  - In both cases, FuXi never asks you to upload your project or files to a FuXi
    service.
- Your code, conversations, configuration, and credentials stay on **your own
  device** under `~/.fuxi/`.

This policy describes honestly: which data stays local, which data leaves your
device and under what circumstances, and why.

---

## 2. What data we process

### 2.1 Data that stays on your device (we cannot access it)

The following data is produced by FuXi and stored locally under `~/.fuxi/`
(overridable with `FUXI_CONFIG_DIR`), and is **not uploaded to any FuXi server
by default**:

| Data | Purpose | Location |
|---|---|---|
| Configuration (incl. API key) | Remember your provider and model settings | Local `~/.fuxi/config.yaml` |
| Session / conversation history | Enable `/resume`, checkpoints, context | Local disk |
| Project memory file | Consolidate memory across sessions | Local, in-project |
| Operation audit log | Let you review what FuXi did | Local |

**We do not read, copy, or upload this data.** It belongs to you and lives on
your own device.

### 2.2 Data that leaves your device

Only the following leaves your device — and in **no case** does FuXi collect,
store, or retain your code or conversations:

- **Account registration & sign-in (required)**: `fuxi login` (or
  `fuxi setup-token` in CI) authenticates you with your FuXi account. Minimal
  account data (identifier and authentication material) is processed by the
  FuXi account system to operate your account and provision FuXi-managed models.
- **Requests to a model** — the prompt and the code context needed for that
  request are transmitted so the model can do its work:
  - *Bring your own key:* direct between your device and the provider you chose
    (OpenAI-compatible, Gemini, Bedrock/Vertex, etc.); that provider's privacy
    policy applies.
  - *FuXi-managed models:* transmitted to the model endpoint solely to serve the
    request. FuXi does **not** retain the content and does **not** use it to
    train models.

### 2.3 Data we do not collect

- We do **not** collect or store your source code or project contents.
- We do **not** collect or retain your conversation content, and we do **not**
  use it for training or any other purpose.
- We do **not** sell, rent, or trade any of your personal data.
- We do **not** silently upload telemetry in the background.

---

## 3. Purposes and legal basis

We process data only to the **strictly necessary** extent:

| Purpose | Description | Basis |
|---|---|---|
| Provide product functionality | Let the agent read code, run commands, drive tools | Performance of the usage relationship |
| Account registration & authentication (required) | `fuxi login` / `fuxi setup-token` | Performance of the usage relationship (contract) |
| Updates and security | Checksum verification, vulnerability fixes | Legitimate interest (user safety) |
| Compliance and legal duty | Comply with applicable law | Legal obligation |

We adhere to **data minimization**: only the minimum data necessary for the
above purposes is processed.

---

## 4. Data sharing and third parties

- We do **not** sell your data to any third party.
- Data is shared only when: you connect a model provider / MCP server / plugin
  yourself (whose behavior you choose and whose own policies apply), or when
  legally required (see §5).

---

## 5. Disclosures required by law

We respect applicable law. Only when the law **clearly requires** it (e.g., a
valid court order or a lawful request in a judicial or administrative
proceeding) will we disclose data we **actually hold**. Because our architecture
does not hold your code or conversations by default, in most such cases we have
**no** corresponding data to disclose.

---

## 6. Data retention and deletion

- Local data (configuration, sessions, audit logs) is retained **at your
  discretion** and can be deleted at any time: removing `~/.fuxi/` (or the
  directory pointed to by `FUXI_CONFIG_DIR`) removes the related local data.
- Uninstalling (`rm -rf "$HOME/.fuxi"`) clears local data.
- For your FuXi account data, contact us to request deletion; the account
  terms applicable when it was created govern the account model used.---

## 7. Your rights

Wherever you are, we honor these universal rights:

- **Access & transparency**: learn what data about you we process;
- **Rectification**: correct inaccurate information;
- **Erasure**: request deletion of related data;
- **Withdraw consent**: withdraw consent-based processing (e.g., optional
  cross-session memory or third-party integrations) at any time;
- **Object & restrict**: object to or restrict particular processing.

To exercise these rights, contact us via the details below.

---

## 8. Children and young users

FuXi **may be used by children and young people** — learning to code is a
legitimate and valuable use. Because FuXi is an AI coding tool that can run
commands, we apply **age-appropriate safeguards** rather than excluding young
users:

- **Consent from a parent or guardian where the law requires it.** Where a user
  is below the applicable age of digital consent — generally **16 or lower**
  under GDPR (13 for COPPA in the US, **14 in China**, **18 in India**, 14 in
  Korea) — registration requires verifiable consent from a parent or guardian.
  The age of consent varies by jurisdiction and we apply the stricter rule
  where it is known.
- **Data minimization for children.** We process the same minimal account data
  as for any user — never more — and we do **not** use children's data for
  behavioural advertising or profiling.
- **No behavioural advertising.** FuXi does not serve behavioural advertising to
  any user, and never to children.
- **Safety by default.** The protections in the
  [Security Whitepaper §5](SECURITY.md) (deny-by-default permissions, command
  classification, local-only data) apply to every user, including children.
- **Adult oversight recommended.** Because AI output can be wrong and FuXi can
  execute commands, we recommend that a parent, guardian, or teacher supervises
  a child's use — especially when FuXi is permitted to act autonomously.
- **Guardian requests.** A parent or guardian may contact us to review, correct,
  or delete a child's account data (see §7).

---

## 9. AI output and user reliance

We want users — including young users and their guardians — to trust FuXi
**accurately**, not blindly:

- FuXi is a **tool**, not a professional adviser. Its output may be inaccurate,
  incomplete, or biased, and must not be relied on as legal, medical, financial,
  or safety advice.
- FuXi does not make decisions on its own: sensitive actions require approval
  and can be interrupted (see the [AI Governance Policy](policies/AI_GOVERNANCE.md)).
- You are responsible for reviewing output and for the final decision on
  critical operations (edits, commands, commits, releases).

---

## 10. Changes to this policy

For material changes, we will announce on the website
(https://www.fuxicode.com) and in this repository, and update the "last
updated" date.

---

## 11. Contact us

- Website: https://www.fuxicode.com
- Repository: https://github.com/fuxicodex/Fuxi
- Privacy matters: reach us via the repository issue tracker or the contact
  details published on the website.

---

*FuXi is secure by design, protecting its users — that is our starting point and
our commitment to you.*
