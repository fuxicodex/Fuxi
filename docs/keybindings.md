# Keyboard Shortcuts

A quick reference for the FuXi terminal UI. Type `/` at the start of an empty
prompt to open the command palette, which lists many of the same actions.

> macOS notes: `Alt` means the **Option** key. If your terminal treats Option as
> "compose" (macOS Terminal / iTerm with "Option as Meta" off), some `Alt+`
> shortcuts may not reach FuXi — use the `Ctrl+X` chord equivalents instead.

## Prompt editor

| Keys | Action |
|---|---|
| `Enter` | Send the message |
| `Ctrl+J` / `Shift+Enter` | Insert a newline |
| `↑` / `↓` | Previous / next prompt history |
| `Ctrl+R` | Reverse-search prompt history |
| `Ctrl+V` (macOS/Linux) · `Alt+V` (Windows) | Paste an image from the clipboard as an attachment |
| `/` | Open the command palette (at the start of an empty prompt) |
| `Esc` | Cancel / close the current popup |

## Chat / transcript

| Keys | Action |
|---|---|
| `Esc` | Cancel the current operation or close a popup |
| `↓` / `j` · `↑` / `k` | Scroll down / up |
| `Shift+↑` / `Shift+↓` | Jump to the previous / next user message |
| `Ctrl+U` / `PgUp` | Scroll up half a page |
| `Ctrl+D` / `PgDn` | Scroll down half a page |
| `Space` / `Ctrl+F` | Scroll down one page |
| `b` / `Ctrl+B` | Scroll up one page |
| `g` / `Home` | Jump to the top of the conversation |
| `G` / `End` | Jump to the bottom |
| `Ctrl+T` | Cycle inline task / teammate panels |
| `Tab` | Toggle the sidebar |
| `Shift+Tab` | Cycle permission mode (default → acceptEdits → plan) |
| `c` | Copy the selected card |
| `p` | Copy the input of the selected card |

## Global

| Keys | Action |
|---|---|
| `Ctrl+C` | Interrupt or quit |
| `Ctrl+L` / `Alt+P` | Open the model picker |
| `Ctrl+G` | Open the prompt in your `$EDITOR` |
| `Ctrl+Shift+P` | Quick open — fuzzy file finder |
| `Ctrl+Shift+F` | Workspace-wide search |
| `Ctrl+S` | Stash the current prompt aside |
| `Ctrl+W` | Open workflows |
| `Ctrl+Y` | Yank — insert the last killed text |
| `Alt+Y` | Yank pop — cycle through the kill-ring |
| `Ctrl+Z` | Suspend FuXi to the background |
| `Alt+O` | Toggle fast mode |
| `Alt+T` | Toggle the model's thinking generation |
| `Alt+M` | Collapse / expand the sidebar MCP section |
| `Alt+V` | Hold-to-talk voice capture |
| `Ctrl+_` / `Ctrl+Shift+-` | Undo the last prompt-editor edit |
| `Esc` `Esc` (double-tap) | Rewind the conversation to a previous point |

## `Ctrl+X` chords

`Ctrl+X` arms a chord prefix; the next key completes the action.

| Chord | Action |
|---|---|
| `Ctrl+X` `Ctrl+L` | Redraw the screen (recovery after external clear) |
| `Ctrl+X` `Ctrl+O` | Toggle fast mode |
| `Ctrl+X` `Ctrl+T` | Toggle thinking |
| `Ctrl+X` `Ctrl+P` | Quick open |
| `Ctrl+X` `Ctrl+F` | Workspace search |
| `Ctrl+X` `Ctrl+V` | Voice capture |
| `Ctrl+X` `Ctrl+W` | Workflows |
| `Ctrl+X` `Ctrl+E` | External editor |
| `Ctrl+X` `Ctrl+K` | Kill running agents |

## Dialogs

| Keys | Action |
|---|---|
| `Tab` / `Shift+Tab` | Move focus between items |
| `↑` / `↓` | Choose an item |
| `Enter` | Confirm |
| `Esc` | Cancel |
| `y` / `n` | Yes / no in confirmation prompts |
