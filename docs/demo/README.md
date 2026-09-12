# Demo recording

`fuxi-demo.gif` (used in the main README) is recorded with
[VHS](https://github.com/charmbracelet/vhs) from a real FuXi session.

## Regenerate

```bash
# Prerequisites: vhs, ffmpeg, and an installed `fuxi` with a configured model
brew install vhs ffmpeg

# 1. Create the demo project (a failing test to fix)
mkdir -p ~/dev/calc-demo && cd ~/dev/calc-demo
cat > calculator.py <<'PY'
def add(a, b):
    return a + b


def multiply(a, b):
    return a + b  # BUG: should multiply


def divide(a, b):
    return a / b
PY
cat > test_calculator.py <<'PY'
from calculator import add, multiply, divide

assert add(2, 3) == 5
assert multiply(4, 5) == 20
assert divide(10, 2) == 5
print("All tests passed!")
PY

# 2. Record
vhs docs/demo/fuxi-demo.tape          # -> docs/demo/final-raw.gif

# 3. Post-process (1.4x speed; GIF for README, MP4 for the website)
ffmpeg -i docs/demo/final-raw.gif -vf "setpts=PTS/1.4,fps=16,scale=1100:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" docs/fuxi-demo.gif
ffmpeg -i docs/demo/final-raw.gif -vf "setpts=PTS/1.4,fps=24,scale=1280:-1:flags=lanczos" -c:v libx264 -pix_fmt yuv420p -crf 20 -movflags +faststart docs/fuxi-demo.mp4
```

The tape runs a real session: FuXi explores the project, finds the bug, shows a
real diff, and runs the test suite. Permission prompts are approved with `Enter`
during recording, so the demo reflects the default (safe) permission mode.
