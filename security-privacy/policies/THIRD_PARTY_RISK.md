# FuXi Third-Party & Supply Chain Risk Policy

*Last updated: 2026-08-23 · Version 1.0 · Layer: L1 Policy*

This policy manages risks from third parties FuXi depends on or that users
connect (model providers, MCP servers, plugins, vendors).

---

## 1. Third-party types

| Type | Introduced by | Risk |
|---|---|---|
| Model providers (BYOK) | User | Content transmission, data handling |
| MCP servers | User | Tool access, command execution |
| Plugins / skills | User | Arbitrary code execution |
| Vendors (hosting, distribution) | FuXi | Supply chain, service availability |

---

## 2. User-connected third parties (BYOK / MCP / plugins)

- **Transparent**: FuXi honestly states which data flows to third parties; the
  user chooses.
- **Off by default**: MCP and plugins are not loaded unless the user explicitly
  enables them.
- **User responsibility**: users should install only from trusted sources and
  review third-party behavior.
- **Recommendation**: review each third party's privacy policy and data
  processing terms.

---

## 3. FuXi's own supply chain controls

- **Official distribution**: installs and updates only via
  `https://releases.fuxicode.com`.
- **Update integrity**: `fuxi update` verifies SHA-256 against the manifest and
  replaces atomically.
- **Minimal dependencies**: a single static binary with no runtime dependencies
  shrinks the supply-chain attack surface.
- **Closed source**: product source is not published, reducing targeted attacks
  on public code (while we provide verifiability via transparency reports and
  security documentation).

---

## 4. Vendor assessment (third parties FuXi uses)

For third parties FuXi itself uses (hosting, monitoring, payment, etc.):

1. collect/transfer only the minimum data necessary for the service;
2. assess their security and privacy practices;
3. bind their data handling through contracts;
4. record them in the [Subprocessors List](../../trust/SUBPROCESSORS.md) and
   disclose to users.

---

## 5. Incidents and offboarding

- On a third-party security incident, assess user impact and notify per our
  commitment.
- Promptly disable and clean up third parties no longer used or found risky.

---

## 6. Responsibility

- **FuXi**: manage its own supply chain and third-party disclosures.
- **Users**: manage the choice and risk of third parties they connect
  (BYOK/MCP/plugins).

---

*This policy brings third-party risk under unified management while respecting
user choice.*
