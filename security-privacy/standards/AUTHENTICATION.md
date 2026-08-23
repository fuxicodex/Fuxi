# FuXi Authentication Standard

*Last updated: 2026-08-23 · Version 1.0 · Layer: L2 Standard*

This standard defines how FuXi authenticates users, protects credentials, and
authenticates to model providers.

---

## 1. Authentication paths

FuXi supports two paths:

| Path | Mechanism | Purpose |
|---|---|---|
| Bring your own key (BYOK) | API key / env vars / local config | Authenticate to the user's chosen provider |
| FuXi account (optional) | OAuth sign-in (`fuxi login` / `setup-token`) | Provision FuXi-managed models |

---

## 2. Credential management requirements

1. **Local storage**: API keys live in `~/.fuxi/config.yaml` or env vars, never
   uploaded.
2. **Minimal exposure**: credentials never written to logs, errors, screenshots,
   or issues/PRs.
3. **File permissions**: set `config.yaml` to owner-only (e.g., `chmod 600`).
4. **Environment variables**: `FUXI_API_KEY` etc. can replace the config file for
   CI scenarios.

---

## 3. OAuth tokens (optional sign-in)

- `fuxi login`: browser authorization; the token is used only for authentication
  and provisioning managed models.
- `fuxi setup-token`: prints a token for `FUXI_OAUTH_TOKEN` in headless/CI use.
- Tokens are issued with least privilege; users can sign out/revoke anytime.

---

## 4. Authentication to providers

- In BYOK mode, FuXi presents the user's key to the provider as a standard
  client, completing authentication.
- Authentication security (TLS, key rotation) follows provider standards.

---

## 5. Sessions and local identity

- Local session data is bound to the user's device account / file permissions;
  no additional network identity is required.
- Core functionality works without an account; no forced registration.

---

## 6. Responsibility

- **FuXi**: implement secure credential reading and OAuth flows; never leak or
  upload credentials.
- **Users**: safeguard keys, set local permissions, and rotate leaked keys
  promptly.

---

*This standard ensures authentication and credential handling are secure and
transparent.*
