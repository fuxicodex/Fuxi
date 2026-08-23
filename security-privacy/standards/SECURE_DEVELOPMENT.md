# FuXi Secure Development Standard (SDLC / AI Safety)

*Last updated: 2026-08-23 · Version 1.0 · Layer: L2 Standard*

This standard defines FuXi's secure development lifecycle (SDLC) and
AI-specific security requirements.

---

## 1. Secure development lifecycle

Every change to FuXi follows:

1. **Requirements & threat modeling**: identify security needs and threats at
   design time.
2. **Secure design**: secure by default, least privilege, distrust external
   input.
3. **Secure implementation**: follow secure coding practices, avoid OWASP Top 10
   issues (injection, broken access control, sensitive data exposure, etc.).
4. **Testing**: unit, integration, and security tests; the command classifier and
   permission model are key test targets.
5. **Pre-release verification**: update-package SHA-256 check, regression tests.
6. **Post-release monitoring & response**: vulnerability disclosure, incident
   response, rapid fixes.

---

## 2. Command safety (special focus)

Command execution is FuXi's core capability and highest risk surface, requiring
dedicated safeguards:

- **AST safety classifier**: commands are parsed into an AST and classified by
  safety level before execution.
- **Rule set**: blocks dangerous patterns (privilege escalation, destructive
  operations).
- **Permission prompts**: sensitive commands prompt per the permission mode.
- **Circuit-breaker**: `--auto` approval includes a circuit-breaker that stops on
  anomaly.

---

## 3. AI-specific security

For FuXi as an AI agent:

| Focus | Requirement |
|---|---|
| Prompt injection defense | Distrust external content (files, web, MCP output) by default; do not blindly execute embedded instructions |
| Output verification | Model output is not fact; critical operations require user confirmation |
| Tool-call safety | Tool parameters are validated to avoid being induced into dangerous actions by malicious content |
| Permission consistency | Model-driven operations match the user's permission mode; no escalation |
| Data boundary | Send only the minimal context needed for the task to the model |

---

## 4. Dependencies and supply chain

- A single static binary with no runtime dependencies shrinks the attack surface.
- Dependency libraries (if any) are regularly scanned for known vulnerabilities
  and upgraded.

---

## 5. Testing and release gates

- Pre-release must pass security testing and checksum verification.
- High-severity vulnerabilities are fixed before disclosure (see Vulnerability
  Disclosure).

---

## 6. Responsibility

- **Engineering**: implement this standard throughout development.
- **Security team**: provide threat modeling, review, and testing support.

---

*This standard ensures security is built into FuXi from the start.*
