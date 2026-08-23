# FuXi Data Protection Commitment

*Last updated: 2026-08-23 · Version 1.0*

This commitment explains, for users worldwide, how FuXi protects data in
practice: data flows, storage locations, your rights, and cross-border
transfers. **Our commitment: by default we do not collect your code or
conversations, and data processing follows minimization principles.**

---

## 1. Data minimization and purpose limitation

We process only the data **necessary to provide product functionality**, for
clearly stated purposes, and not for any unstated use. Specifically:

- No account is required for core functionality → no identity data collected.
- Content flows directly to the provider you choose by default → not routed
  through or stored by FuXi.
- Local data is retained only to support session resume, memory, and audit.

---

## 2. Data flow map

```
Your machine (local — we cannot access it)
├── ~/.fuxi/config.yaml      — configuration & credentials (local)
├── ~/.fuxi/ session records — conversation history (local)
├── Project memory file       — cross-session memory (local)
└── Audit logs                — operation records (local)

Leaves the device only after you actively configure it:
  Request prompt + code context ──▶  the model provider you choose
                                       (its policy applies)
  fuxi login (optional)        ──▶  FuXi authentication (sign-in only)
```

**Key point:** in "bring your own key" mode, your content travels directly
between **you and your provider**; FuXi does not hold, relay, or store it.

---

## 3. Storage location and isolation

- All local data is stored under `~/.fuxi/` (overridable with `FUXI_CONFIG_DIR`).
- We do not store your code, conversations, or keys on our servers.
- Minimal sign-in account data (if you choose to sign in) is handled by the
  FuXi account system, solely for authentication and provisioning managed
  models.

---

## 4. Cross-border data transfers

- **No cross-border transfer by default**: local data does not leave your
  device.
- **When you actively configure it**: transfer to a model provider is determined
  by your choice; providers may be located in different countries/regions, and
  their own privacy policies apply.
- We disclose this honestly and recommend reviewing your chosen provider's
  privacy and data-residency policies.

---

## 5. Security safeguards

See the [Security Whitepaper](SECURITY.md). Highlights: AST command safety
classifier, explicit permission model, audit logs, checksum-verified updates,
and local-only credential storage.

---

## 6. Your rights (universal)

- **Access**: learn what data about you we process;
- **Rectification**: correct inaccurate information;
- **Erasure**: delete local data (remove `~/.fuxi/`) or request account data
  deletion;
- **Withdraw consent**: stop the sign-in / account feature at any time;
- **Complain**: raise concerns with us or your local data protection authority.

---

## 7. Incident response

If a data security incident affects users, we will:

1. investigate and contain the impact promptly;
2. notify affected users and relevant parties as required by law and our
   commitment;
3. publish necessary fixes and mitigations.

---

## 8. Updates to this commitment

For material changes, we will announce on the website
(https://www.fuxicode.com) and in this repository, and update the date.

---

*FuXi is secure by design, protecting its users — our long-term, honest
commitment to you.*
*Entity: FUXI*
