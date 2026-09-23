---
name: example-skill
description: This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating FuXi plugin skills.
version: 1.0.0
---

# Example Skill

This skill demonstrates the structure and format for FuXi plugin skills.

## Overview

Skills are model-invoked capabilities that FuXi autonomously uses based on task context. Unlike commands (user-invoked) or agents (spawned by FuXi), skills provide contextual guidance that FuXi incorporates into its responses.

## When This Skill Applies

This skill activates when the user's request involves:
- Creating or understanding plugin skills
- Skill template or reference needs
- Skill development patterns

## Skill Structure

### Required Files

```
skills/
└── skill-name/
    └── SKILL.md          # Main skill definition (required)
```

### Optional Supporting Files

```
skills/
└── skill-name/
    ├── SKILL.md          # Main skill definition
    ├── README.md         # Additional documentation
    ├── references/       # Reference materials
    │   └── patterns.md
    ├── examples/         # Example files
    │   └── sample.md
    └── scripts/          # Helper scripts
        └── helper.sh
```

## Frontmatter Options

Skills support these frontmatter fields:

- **name** (required): Skill identifier
- **description** (required): Trigger conditions - describe when FuXi should use this skill
- **version** (optional): Semantic version number
- **license** (optional): License information or reference

## Writing Effective Descriptions

The description field is crucial - it tells FuXi when to invoke the skill.

**Good description patterns:**
```yaml
description: This skill should be used when the user asks to "specific phrase", "another phrase", mentions "keyword", or discusses topic-area.
```

**Include:**
- Specific trigger phrases users might say
- Keywords that indicate relevance
- Topic areas the skill covers

## Skill Content Guidelines

1. **Clear purpose**: State what the skill helps with
2. **When to use**: Define activation conditions
3. **Structured guidance**: Organize information logically
4. **Actionable instructions**: Provide concrete steps
5. **Examples**: Include practical examples when helpful

## Best Practices

- Keep skills focused on a single domain
- Write descriptions that clearly indicate when to activate
- Include reference materials in subdirectories for complex skills
- Test that the skill activates for expected queries
- Avoid overlap with other skills' trigger conditions
