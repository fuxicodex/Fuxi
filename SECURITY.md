# Security Policy

FuXi runs shell commands, stores provider credentials under `~/.fuxi/`, and
self-updates over the network — security reports are welcome and appreciated.

## Supported versions

Only the latest release is actively maintained. FuXi updates itself in place,
so please keep it current and verify the affected version with `fuxi --version`
before reporting.

## Reporting a vulnerability

Please report suspected vulnerabilities **privately** through GitHub's
[security advisories](https://github.com/fuxicodex/Fuxi/security/advisories/new)
("Report a vulnerability") on this repository. Do not open a public issue for
security concerns.

Include:

- FuXi version (`fuxi --version`) and how it was installed,
- operating system and shell,
- a minimal reproduction or proof-of-concept,
- the impact you believe it has.

## What to expect

Reports are reviewed on a best-effort basis; you will receive an initial
response within a few days and follow-up updates as the report progresses. If a
report is accepted, we aim to release a fix before details are made public, and
we will coordinate with you on disclosure timing. As a general guideline, we
ask for a window of up to 90 days between acknowledgment and public disclosure,
and we will work with you to shorten it whenever a fix ships sooner.

Thank you for helping keep FuXi users safe.
