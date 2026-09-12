# FuXi Usage Policy

*Last updated: 2026-09-12 · Version 1.0*

This policy covers what you may and may not do with FuXi, how the permission
model keeps autonomous execution under your control, and how FuXi behaves as an
AI product. It applies to everyone who installs or uses FuXi. By using FuXi you
agree to follow it.

> Related: [Terms of Service](TERMS_OF_SERVICE.md) ·
> [Privacy Policy](PRIVACY_POLICY.md) · [Security Whitepaper](SECURITY.md) ·
> [Compliance & Responsibility](COMPLIANCE.md)

---

## 1. Use FuXi lawfully

**You must comply with all laws and regulations that apply to you**, including
the laws of the country and region where you are located and where you use FuXi,
data-protection law applicable to the data you handle, and the intellectual
property and licence terms of any code you work on.

Where your use would be unlawful in your jurisdiction, you must not use FuXi for
it — regardless of what FuXi is technically capable of. FuXi's technical
capability is not permission.

---

## 2. Disallowed uses

You must not use FuXi to:

1. **Commit or facilitate unlawful activity** — including crimes, infringement
   of others' rights, or evasion of a lawful obligation.
2. **Harm children** — including any sexual content involving minors, or
   exploitation or abuse of minors.
3. **Cause harm or destruction** — including attacks, denial-of-service, or
   damage to systems or data you do not own or are not authorised to test.
4. **Gain unauthorised access** — including unauthorised access to systems,
   networks, or accounts, or the creation and distribution of malware or
   exploits.
5. **Violate privacy** — including processing others' personal data without a
   lawful basis, or sharing others' private information without consent.
6. **Deceive or defraud** — including creating deceptive content, impersonation,
   fraud, or spam.
7. **Create illegal content** — including content unlawful in your jurisdiction.
8. **Circumvent safety** — including disabling or defeating FuXi's permission
   model or command safety classifier in order to carry out any of the above.
9. **Misrepresent AI output** — including presenting AI-generated output as
   verified professional advice.
10. **Abuse the service** — including probing, scanning, or testing our systems
    outside the authorised channel in §7.

---

## 3. Age requirements

- FuXi is aimed at developers and professional users and is **not directed at
  children under 14**, consistent with the [Privacy Policy §8](PRIVACY_POLICY.md).
- Users **aged 14–17** may use FuXi only with the involvement of a parent or
  guardian, who must consent where the law requires it and is responsible for
  the minor's use.
- We do not knowingly allow use by children under 14; if we learn of such use,
  we will take appropriate action.

---

## 4. Permission model and access control

FuXi can edit files and run commands, so autonomous execution is governed by an
explicit permission model.

**Principles**

1. **Least privilege** — grant only the minimum permission a task needs.
2. **Explicit approval** — sensitive or irreversible operations require explicit
   user approval.
3. **Separation of duties** — requesting, executing, and auditing are separated.
4. **Revocable** — you can change permission modes or revoke authorisation at any
   time.

**Permission modes**

| Mode | Behavior | Use case |
|---|---|---|
| `default` | Sensitive operations prompt for approval one by one | Daily use (recommended) |
| `plan` | Planning mode: read-only analysis, no changes | Review the plan first |
| `bypassPermissions` | Auto-approves prompts (the classifier and audit logging still run) | Trusted, automatable environments |
| `--auto` | Auto-approve only operations the classifier deems safe, with a circuit breaker | Balance speed and safety |
| `--dangerously-skip-permissions` | Skip all permission checks (DANGEROUS) | Fully trusted, isolated environments only |

> Deny-by-default means **no action is approved implicitly** — approving
> everything requires an explicit mode change. `bypassPermissions` skips the
> prompt layer but the command-safety classifier and audit logging still apply;
> `--dangerously-skip-permissions` skips all permission checks. Use at your own
> risk.

**Command execution control**

Every shell command (`Bash` / `PowerShell`) is, before execution: parsed into an
abstract syntax tree (AST); classified by the safety classifier; filtered by the
rule set for dangerous patterns; gated on the current permission mode; and
written to the local audit log afterwards.

**Tool and MCP access**

- **Built-in tools**: restrict with `--tools` (`""` none, `default` all, or by
  name), `--allowed-tools`, and `--disallowed-tools`.
- **MCP servers**: only user-configured servers are loaded;
  `--strict-mcp-config` uses only `--mcp-config` servers.
- **Plugins and skills**: install only from trusted sources; you are responsible
  for their behavior.

**Local data access**

- Configuration and credentials live in `~/.fuxi/`, protected by your filesystem
  permissions. We recommend `chmod 600` on `~/.fuxi/config.yaml`.
- FuXi does not read or upload local credentials.

**Minors**: because FuXi can run commands, a minor account (14–17) must not use
`bypassPermissions` or `--dangerously-skip-permissions`.

---

## 5. FuXi as an AI product

**The model is the engine; FuXi is the vehicle.** FuXi does not train or host the
underlying general-purpose models; it turns the model you choose into a worker
that reasons, acts, and verifies.

| Principle | Implementation |
|---|---|
| **Human in the loop** | Sensitive operations require approval; you can interrupt or revoke at any time |
| **Explainable & traceable** | Every action is traceable in the local audit logs |
| **Safety guardrails** | Commands filtered by the AST classifier and rule set before execution |
| **No implicit escalation** | The permission model defaults to least privilege |
| **Refuse misuse** | No assistance with destructive, offensive, or unlawful use |

**Routing and transparency.** Requests are scored by complexity and routed to the
appropriate model tier. `/model`, `/status`, `/context`, and `/cost` keep you
informed of which model is used, at what cost, and how much context is consumed.
With your own key you control which provider and model are used.

**Output safety.** Model output is **not treated as fact**. Review critical
operations — file edits, commands, commits, releases — before confirming. FuXi
drives tests and builds, but the final green light should be yours.

**Fairness.** FuXi does not unreasonably differentiate by identity, region, or
language. Transparent routing and verifiable processes let you detect and correct
biased output.

**AI-tool usage law.** FuXi is used across jurisdictions with AI-specific rules,
and we align to their common expectations:

| Regime | Expectation | FuXi posture |
|---|---|---|
| EU AI Act | Transparency about AI involvement; risk management for higher-risk uses | You are always told you are working with an AI agent; human-in-the-loop and audit logs; honest capability claims |
| China — Generative AI Measures | Content safety, lawful data use, clear service identity | Service identity is explicit; safety guardrails; no content upload |
| US FTC §5 | Truthful claims; no deceptive AI behaviour | No fabricated certifications or overstated capabilities |
| Children's design codes (e.g. UK ICO AADC, California AADC) | Best interests of the child; high privacy by default | Privacy-by-default for all users; no profiling or behavioural ads; data minimization |

Because an account is required, the applicable AI rules are those of the
jurisdiction where the account is offered and operated; where they differ, the
stricter expectation is our internal standard.

**Honest limits.** FuXi is a **tool**, not a professional adviser: its output must
not be relied on as legal, medical, financial, or safety advice. Automated output
can be wrong; review before acting. FuXi does not make autonomous decisions about
your rights or obligations — sensitive actions require approval and every action
is auditable. We never represent that FuXi guarantees correct or complete results.

---

## 6. Your responsibilities

You are responsible for:

- your task choices and their lawfulness;
- reviewing FuXi's output before acting on it;
- the consequences of actions you approve, especially when you disable
  permission prompts or allow autonomous operation;
- keeping your credentials and device secure, and keeping backups of your data.

We are responsible for FuXi's own security mechanisms, documentation honesty, and
the account processing required to operate the service. Model providers are
responsible for the underlying models; third parties you connect (MCP servers,
plugins) are responsible for their own behavior.

---

## 7. Reporting

- **Security issues**: report privately via
  [GitHub Security Advisories](https://github.com/fuxicodex/Fuxi/security/advisories/new).
  Do not open a public issue. There is currently no public bug-bounty program.
- **Abuse or policy violations**: contact us through the repository or the
  website; we may restrict or terminate access for serious or repeated
  violations.

---

## 8. If you are unsure

If it is unclear whether a use is lawful or permitted, **do not proceed until you
have taken advice** — this policy is not legal advice.

---

*This policy ensures FuXi is used lawfully, responsibly, and safely wherever it
is used, and that autonomous execution stays under your control.*
