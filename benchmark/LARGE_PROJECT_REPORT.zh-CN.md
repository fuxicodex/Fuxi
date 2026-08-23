# 🏆 FuXi 大型代码库对比评测报告

**FuXi vs Claude Code · 多文件分层项目（orderapp）**

<div align="center">

| | | |
|:---:|:---:|:---:|
| **🏗️ 项目规模** | **🎯 测试维度** | **✅ 通过率** |
| **`25+ 文件` · `5 层`** | **`4`** | **`100%`** |
| models · services · api · storage · utils | 跨文件缺陷修复 · 功能开发 · 重构 · 集成调试 | 两模型全部满分 |

</div>

> **一句话结论：** 在一个真实的多文件分层项目（订单管理系统，25+ 文件、5 层
> 架构）上，FuXi + `deepseek` **与 Claude Code + `claude-opus-5`
> 完全打平**——4 个开发维度全部满分、零失败、零人工干预。

---

## 🖥️ 客户端真实环境

| 客户端 | 版本 | 构建 |
|---|---|---|
| **FuXi CLI** | `0.15` | 预计发布版本 |
| **Claude Code** | `2.1.241` | 官方 npm `@anthropic-ai/claude-code` |

| 环境 | 值 |
|---|---|
| 操作系统 | macOS 26.3 (arm64) |
| Python / pytest | 3.9.6 / 8.4.2 |
| FuXi 已注册工具 | 51 |

真实执行命令：

```bash
# FuXi 侧
fuxi -p --permission-mode bypassPermissions --max-turns 30 --max-thinking-tokens 8000 "<任务>"

# Claude Code 侧
claude -p --dangerously-skip-permissions "<任务>"
```

---

## 🏗️ 被测项目

`orderapp` 是一个真实的订单管理系统，非玩具项目：

```
orderapp/
├── models/          # Order、Customer、Product、OrderItem、OrderStatus + rules + pricing
├── services/        # OrderService、InventoryService、CustomerService
├── api/             # Api 门面（place_order、order_report）
├── storage/         # MemoryStore、JsonFileStore
└── utils/           # formatting、report
```

缺陷被**刻意植入在跨模块边界**，模型必须理解跨文件依赖（如 pricing → order_service、
api → inventory）才能修复——这是真实的工程任务，而非单文件谜题。

---

## 📊 评测结果

| # | 维度 | 任务 | FuXi | Claude Code |
|:--:|---|:---:|:---:|:---:|
| D1 | 跨文件缺陷修复 | 折扣符号 bug（`pricing.py` → `order_service.py`） | ✅ 15 passed | ✅ 15 passed |
| D2 | 功能开发 | 实现 `JsonFileStore.save()` 持久化 | ✅ 18 passed | ✅ 18 passed |
| D3 | 跨模块重构 | 去重 `report.py`（3 组重复函数） | ✅ 18 passed | ✅ 18 passed |
| D4 | 集成层调试 | `place_order()` 丢弃了收集的 items | ✅ 15 passed | ✅ 15 passed |

**总计：两模型 4/4 维度全部通过，零失败。**

---

## 💎 代码质量观察（真实、可核实）

| 维度 | 模型实际做了什么 |
|---|---|
| D2（功能） | 构建了递归 JSON 序列化器，处理 dataclass、枚举、datetime；保存时保留磁盘已有内容；调整 `load()`/`get_order()` 以保持字符串 key 一致 |
| D3（重构） | 提取 `_product_info` / `_customer_name_email` / `_order_item_info`；Claude Code 额外跑了 500 组随机输入 diff 保证字节级一致，并正确避开了 `format_price`（千分位分隔符）以保持输出完全不变 |

两模型不仅通过了测试，还产出了**带正确性推理的工程级代码**——而非过拟合的补丁。

---

## 🎯 能力矩阵

| 能力 | FuXi | Claude Code |
|:---|:---:|:---:|
| 跨文件依赖理解 | 🟢 | 🟢 |
| 多层导航（models→services→api→storage） | 🟢 | 🟢 |
| 功能实现（持久化） | 🟢 | 🟢 |
| 行为保持重构 | 🟢 | 🟢 |
| 集成层调试 | 🟢 | 🟢 |
| 迭代式测试驱动验证 | 🟢 | 🟢 |

---

## 🏁 结论

1. **能力打平**——两模型在 25+ 文件分层项目上 4 维度全部满分。
2. **真实工程**——缺陷跨越模块边界；两模型都正确导航并修复。
3. **可验证**——FuXi 让 `deepseek` 在非平凡代码库上达到 `claude-opus-5` 同级能力。
4. **成本优势**——`deepseek` 为轻量档，成本显著更低。

---

## ⚠️ 局限与诚实声明

| 局限 | 说明 |
|---|---|
| 单一项目 | 一个分层项目，非多仓库/多领域 |
| 单次运行 | 每维度运行一次 |
| 规模 | 25+ 文件是"中型"，非上万文件的巨型单体 |
| 模型身份 | 配置/代理声明 ID，未独立核实 |

---

*真实端到端执行（`fuxi -p` / `claude -p`）+ pytest 客观评分 · 零人工干预*
