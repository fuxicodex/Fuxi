# FuXi Access Control Policy

*Last updated: 2026-08-23 · Version 1.0 · Layer: L1 Policy*

This policy defines FuXi's permission model and access control principles,
ensuring autonomous execution stays under the user's control.

---

## 1. Principles

1. **Least privilege**: grant only the minimum permission needed for a task.
2. **Explicit approval**: sensitive or irreversible operations require explicit
   user approval.
3. **Separation of duties**: requesting, executing, and auditing are separated.
4. **Revocable**: the user can adjust permission modes or revoke authorization at
   any time.

---

## 2. Permission modes

FuXi offers user-selectable permission modes:

| Mode | Behavior | Use case |
|---|---|---|
| `default` | Sensitive operations prompt for approval one by one | Daily use (recommended) |
| `plan` | Planning mode: read-only analysis, no changes | Review the plan first |
| `bypassPermissions` | Auto-approve (skip prompts) | Trusted, automatable environments |
| `--auto` | Auto-approve only operations the **classifier deems safe**, with circuit-breaker | Balance speed and safety |
| `--dangerously-skip-permissions` | Skip **all** permission checks | Fully trusted, isolated environments only |

> ⚠️ `--dangerously-skip-permissions` disables all safeguards; use at your own
> risk.

---

## 3. Command execution control

Every shell command (`bash` / PowerShell), before execution:

1. is parsed into an abstract syntax tree (AST);
2. is classified by the **safety classifier**;
3. is filtered by the **rule set** for dangerous patterns;
4. is gated on the current permission mode (prompt or not);
5. is written to the **audit log** after execution.

---

## 4. Tool and MCP access

- **Built-in tools**: restrict via `--tools` (`""` none, `default` all, or by
  name).
- **MCP servers**: only user-configured servers are loaded; `--strict-mcp-config`
  uses only `--mcp-config` servers.
- **Plugins/skills**: install only from trusted sources; users are responsible for
  their behavior (see Third-Party Risk Policy).

---

## 5. Local data access

- Configuration and credentials live in `~/.fuxi/`, protected by the user's
  filesystem permissions.
- Recommendation: set `~/.fuxi/config.yaml` to owner-only (e.g., `chmod 600`).
- FuXi does not read or upload local credentials.

---

## 6. Audit and traceability

- All tool calls and command executions are recorded in local audit logs.
- Users can review what FuXi did and revoke authorization at any time.

---

## 7. Responsibility

- **Product**: implement and maintain the permission model and classifier.
- **Users**: choose the right permission mode and manage local file permissions.

---

*This policy ensures autonomous execution is always auditable, controllable, and
revocable.*
