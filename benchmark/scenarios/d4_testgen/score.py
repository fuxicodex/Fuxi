#!/usr/bin/env python3
"""Score d4_testgen: measure coverage of tests written by the model."""
import subprocess, sys, os, re

repo = os.path.dirname(os.path.abspath(__file__))

# Run pytest with coverage on the src module, using whatever tests the model wrote.
r = subprocess.run(
    [sys.executable, "-m", "pytest", "-q", "--tb=no", f"--cov=src.stringops", "--cov-report=term-missing"],
    cwd=repo, capture_output=True, text=True
)
out = r.stdout + r.stderr
print(out)

# Extract coverage %
m = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", out)
if m:
    cov = int(m.group(1))
    print(f"COVERAGE={cov}")
else:
    # fallback: any 'passing' count
    mp = re.search(r"(\d+) passed", out)
    print(f"COVERAGE=UNKNOWN passed={mp.group(1) if mp else '?'}")

# Also check tests collected / passed
mp = re.search(r"(\d+) passed", out)
mf = re.search(r"(\d+) failed", out)
print(f"PASSED={mp.group(1) if mp else 0}")
print(f"FAILED={mf.group(1) if mf else 0}")
