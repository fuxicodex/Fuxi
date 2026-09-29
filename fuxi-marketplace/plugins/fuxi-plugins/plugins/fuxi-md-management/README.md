# FUXI.md Management Plugin

Tools to maintain and improve FUXI.md files - audit quality, capture session learnings, and keep project memory current.

## What It Does

Two complementary tools for different purposes:

| | fuxi-md-improver (skill) | /revise-fuxi-md (command) |
|---|---|---|
| **Purpose** | Keep FUXI.md aligned with codebase | Capture session learnings |
| **Triggered by** | Codebase changes | End of session |
| **Use when** | Periodic maintenance | Session revealed missing context |

## Usage

### Skill: fuxi-md-improver

Audits FUXI.md files against current codebase state:

```
"audit my FUXI.md files"
"check if my FUXI.md is up to date"
```

<img src="fuxi-md-improver-example.png" alt="FUXI.md improver showing quality scores and recommended updates" width="600">

### Command: /revise-fuxi-md

Captures learnings from the current session:

```
/revise-fuxi-md
```

<img src="revise-fuxi-md-example.png" alt="Revise command capturing session learnings into FUXI.md" width="600">

## Author

Isabella He (support@fuxicode.com)
