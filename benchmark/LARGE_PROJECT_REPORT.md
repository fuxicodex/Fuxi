# 🏆 FuXi Large-Codebase Benchmark Report

**FuXi vs Claude Code · Multi-file Layered Project (orderapp)**

<div align="center">

| | | |
|:---:|:---:|:---:|
| **🏗️ Project scale** | **🎯 Dimensions** | **✅ Pass rate** |
| **`25+ files` · `5 layers`** | **`4`** | **`100%`** |
| models · services · api · storage · utils | cross-file bug-fix · feature dev · refactor · integration debug | Both models, all green |

</div>

> **Bottom line:** On a real multi-file layered project (an order-management
> system with 25+ files across 5 layers), FuXi + `deepseek-v4-flash` **ties
> Claude Code + `claude-opus-5`** across all 4 development dimensions — 100%
> pass, zero failures, zero human intervention.

---

## 🖥️ Real Client Environment

| Client | Version | Build |
|---|---|---|
| **FuXi CLI** | `0.15` | planned release |
| **Claude Code** | `2.1.241` | official npm `@anthropic-ai/claude-code` |

| Environment | Value |
|---|---|
| OS | macOS 26.3 (arm64) |
| Python / pytest | 3.9.6 / 8.4.2 |
| FuXi registered tools | 51 |

Real commands:

```bash
# FuXi side
fuxi -p --permission-mode bypassPermissions --max-turns 30 --max-thinking-tokens 8000 "<task>"

# Claude Code side
claude -p --dangerously-skip-permissions "<task>"
```

---

## 🏗️ The Project Under Test

`orderapp` is a realistic order-management system, not a toy:

```
orderapp/
├── models/          # Order, Customer, Product, OrderItem, OrderStatus + rules + pricing
├── services/        # OrderService, InventoryService, CustomerService
├── api/             # Api facade (place_order, order_report)
├── storage/         # MemoryStore, JsonFileStore
└── utils/           # formatting, report
```

Defects are planted **across module boundaries**, so a model must understand
cross-file dependencies (e.g., pricing → order_service, api → inventory) to fix
them — this is a genuine engineering task, not a single-file puzzle.

---

## 📊 Results

| # | Dimension | Task | FuXi | Claude Code |
|:--:|---|:---:|:---:|:---:|
| D1 | Cross-file bug fix | discount sign bug (`pricing.py` → `order_service.py`) | ✅ 15 passed | ✅ 15 passed |
| D2 | Feature development | implement `JsonFileStore.save()` persistence | ✅ 18 passed | ✅ 18 passed |
| D3 | Cross-module refactor | dedupe `report.py` (3 groups of duplicated fns) | ✅ 18 passed | ✅ 18 passed |
| D4 | Integration debug | `place_order()` dropped collected items | ✅ 15 passed | ✅ 15 passed |

**Total: 4/4 dimensions passed, both models. Zero failures.**

---

## 💎 Code Quality Observations (real, verifiable)

| Dimension | What the model actually did |
|---|---|
| D2 (feature) | Built a recursive JSON serializer handling dataclasses, enums, datetimes; preserved existing file content on save; adjusted `load()`/`get_order()` for string-key consistency |
| D3 (refactor) | Extracted `_product_info` / `_customer_name_email` / `_order_item_info`; Claude Code additionally ran a 500-input randomized diff to guarantee byte-identical behavior, and correctly avoided reusing `format_price` (thousands separator) to preserve exact output |

Both models not only passed tests but produced **engineering-grade code with
correctness reasoning** — not over-fitted patches.

---

## 🎯 Capability Matrix

| Capability | FuXi | Claude Code |
|:---|:---:|:---:|
| Cross-file dependency understanding | 🟢 | 🟢 |
| Multi-layer navigation (models→services→api→storage) | 🟢 | 🟢 |
| Feature implementation (persistence) | 🟢 | 🟢 |
| Behavior-preserving refactor | 🟢 | 🟢 |
| Integration-layer debugging | 🟢 | 🟢 |
| Iterative test-driven verification | 🟢 | 🟢 |

---

## 🏁 Conclusion

1. **Tied ability** — both models pass all 4 dimensions on a 25+ file layered project.
2. **Real engineering** — defects span module boundaries; both models navigated and fixed them correctly.
3. **Verifiable** — FuXi lets `deepseek-v4-flash` reach `claude-opus-5`-level ability on non-trivial codebases.
4. **Cost advantage** — `deepseek-v4-flash` is a lightweight tier, substantially cheaper.

---

## ⚠️ Limitations & Honest Disclosures

| Limitation | Note |
|---|---|
| Single project | one layered project, not multiple repos/domains |
| Single run | each dimension run once |
| Scope | 25+ files is "medium", not a 10k-file monolith |
| Model identity | config/proxy-declared IDs, not independently verified |

---

*Real end-to-end execution (`fuxi -p` / `claude -p`) + pytest objective scoring · zero human intervention*
