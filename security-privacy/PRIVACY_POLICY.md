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
- You **never have to upload your code or conversations to us** — this is our
  **zero content upload** commitment. Your code, prompts, and conversation
  content are not stored on, and not routed through, FuXi's servers.
- By default, your code, conversations, configuration, and credentials stay on
  **your own device**, or travel directly between you and the model provider you
  choose.

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

### 2.2 Data that leaves your device (only after you configure it)

Only the following data leaves your device, and only in the described scope — in
no case is your code or conversation content uploaded to FuXi:

- **Account registration & sign-in (required)**: `fuxi login` (or
  `fuxi setup-token` in CI) authenticates you with your FuXi account. Minimal
  account data (identifier and authentication material) is processed by the
  FuXi account system to operate your account and provision FuXi-managed models.
- **Communication with a model provider**: when you make a request, the prompt
  and the relevant code context needed for that request are sent to the model
  provider you configured (OpenAI-compatible, Gemini, Bedrock/Vertex, etc.).
  This is required for the model to do its work; content travels directly
  between you and that provider and is not relayed or stored by FuXi. That
  provider's privacy policy applies to this transmission.

### 2.3 Data we do not collect

- We do **not** collect your source code or project contents.
- We do **not** collect your conversation content for training or any other
  purpose (in "bring your own key" mode, content flows directly between you and
  your provider).
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
  terms applicable when it was created govern the account model used.

---

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

## 8. Children's privacy

FuXi is intended for developers and professional users, is not directed at
children, and does not knowingly collect data from individuals under 16. If we
learn of any such collection, we will delete it promptly.

---

## 9. Changes to this policy

For material changes, we will announce on the website
(https://www.fuxicode.com) and in this repository, and update the "last
updated" date.

---

## 10. Contact us

- Website: https://www.fuxicode.com
- Repository: https://github.com/fuxicodex/Fuxi
- Privacy matters: reach us via the repository issue tracker or the contact
  details published on the website.

---

*FuXi is secure by design, protecting its users — that is our starting point and
our commitment to you.*
