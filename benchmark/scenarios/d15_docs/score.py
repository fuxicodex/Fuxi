#!/usr/bin/env python3
"""Score d15_docs: verify docstrings were actually added.
Docs task is judged by presence of docstrings + tests still passing."""
import ast, os, subprocess, sys

repo = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(repo, "src", "mathmod.py")

with open(src) as f:
    tree = ast.parse(f.read())

# Collect all function/class definitions
defs = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
documented = 0
total = 0
for n in defs:
    if n.name.startswith("_"):
        continue
    total += 1
    if ast.get_docstring(n):
        documented += 1

# Run pytest too
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=repo, capture_output=True, text=True)
out = r.stdout + r.stderr
print(out)
print(f"DOCUMENTED={documented}")
print(f"TOTAL_DEFS={total}")
print(f"DOC_COVERAGE={round(documented/total*100) if total else 0}")
