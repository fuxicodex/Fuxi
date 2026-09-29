---
description: "Cancel active Ralph Loop"
allowed-tools: ["Bash(test -f .fuxi/ralph-loop.local.md:*)", "Bash(rm .fuxi/ralph-loop.local.md)", "Read(.fuxi/ralph-loop.local.md)"]
hide-from-slash-command-tool: "true"
---

# Cancel Ralph

To cancel the Ralph loop:

1. Check if `.fuxi/ralph-loop.local.md` exists using Bash: `test -f .fuxi/ralph-loop.local.md && echo "EXISTS" || echo "NOT_FOUND"`

2. **If NOT_FOUND**: Say "No active Ralph loop found."

3. **If EXISTS**:
   - Read `.fuxi/ralph-loop.local.md` to get the current iteration number from the `iteration:` field
   - Remove the file using Bash: `rm .fuxi/ralph-loop.local.md`
   - Report: "Cancelled Ralph loop (was at iteration N)" where N is the iteration value
