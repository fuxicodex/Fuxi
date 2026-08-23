#!/usr/bin/env bash
# Multi-dimensional FuXi benchmark driver (11 scenarios).
# Usage: run_multi.sh <model-name> <base-url> <api-key>
set -u

MODEL_NAME="$1"; BASE_URL="$2"; API_KEY="$3"

SCRATCH="/private/var/folders/z3/9wtwrkrx5b79h1zrvlqtk8z80000gn/T/fuxi-501/-Users-aivenue-Desktop-Fuxi-github-promo/c506e182-bb52-4c1d-ab7f-b96a3ec9451a/scratchpad"
BENCH="$SCRATCH/multi-bench"; SCEN="$BENCH/scenarios"

export FUXI_BASE_URL="$BASE_URL"; export FUXI_API_KEY="$API_KEY"; export FUXI_MODEL="$MODEL_NAME"
RESULT="$BENCH/result-$MODEL_NAME.json"
echo "{" > "$RESULT"

# prompt map: dir -> prompt
prompt_for() {
  case "$1" in
    d1_bugfix) echo "读取 tests/test_jsonutil.py 了解期望行为，然后修复 src/jsonutil.py 中的 bug：1) parse 应在输入非法 JSON 时抛 ValueError；2) get 应支持点分路径（如 'a.b.c'）访问嵌套字典；3) 保持 stringify 正确。用 python3 -m pytest 验证直到全部通过。";;
    d2_feature) echo "在 src/cache.py 中实现一个 memoize 装饰器（缓存函数结果，相同参数只计算一次，支持任意可哈希参数，并用 functools.wraps 保留元数据）。在 src/stats.py 中实现 mean、median、mode（空列表都抛 ValueError）。用 python3 -m pytest tests/test_feature.py 验证直到全部通过。";;
    d3_refactor) echo "重构 src/geometry.py：保持所有函数对外行为完全不变（tests/test_geometry.py 必须继续全部通过），但消除代码重复、改进命名、提取常量、使代码更清晰。运行 python3 -m pytest 确认行为不变。";;
    d4_testgen) echo "为 src/stringops.py 中的 StringOps 类编写完整的 pytest 测试，覆盖所有方法（word_count、to_title、find_all、is_anagram、snake_case），包括边界情况。把测试写到 tests/ 目录。目标是达到尽可能高的代码覆盖率，并确保测试全部通过。运行 python3 -m pytest --cov=src.stringops 检查覆盖率。";;
    d5_review) echo "审查并修复 src/bank.py 中的逻辑 bug：1) deposit 应拒绝负数金额（抛 ValueError）；2) withdraw 应拒绝余额不足和负数金额（抛 ValueError）；3) transfer 应校验余额充足（抛 ValueError）。用 python3 -m pytest tests/test_bank.py 验证直到全部通过。";;
    d6_lru) echo "修复 src/lru.py 中的 LRUCache：get 应把访问的 key 标记为最近使用，put 应支持 LRU 淘汰（容量满时逐出最久未使用项）以及更新已存在 key。用 python3 -m pytest tests/test_lru.py 验证直到全部通过。";;
    d7_graph) echo "修复 src/graph.py 中的图算法：1) bfs 应返回正确的 BFS 遍历顺序；2) shortest_path 应返回最短边数或 -1；3) has_cycle 应正确检测有向图中的环。用 python3 -m pytest tests/test_graph.py 验证直到全部通过。";;
    d8_threadsafe) echo "修复 src/counter.py 使 SafeCounter 线程安全：increment/decrement 应加锁避免并发丢失更新，并暴露锁属性。用 python3 -m pytest tests/test_counter.py 验证直到全部通过。";;
    d9_validation) echo "修复 src/validation.py：1) validate_email 用正则校验邮箱格式；2) validate_phone 校验电话号码格式；3) sanitize_html 用 html.escape 转义 HTML 特殊字符。用 python3 -m pytest tests/test_validation.py 验证直到全部通过。";;
    d10_regex) echo "修复 src/textproc.py：1) extract_urls 用正则提取所有 http/https URL；2) mask_credit_card 保留末 4 位其余掩码；3) count_words 正确处理标点和多余空白。用 python3 -m pytest tests/test_textproc.py 验证直到全部通过。";;
    d11_multifile) echo "修复多文件 Todo 应用：1) src/storage.py 的 complete 应把 done 设为 True（而非 False）；2) src/service.py 的 pending 应返回未完成项、done 应返回已完成项（不要抛 NotImplementedError）。用 python3 -m pytest tests/test_service.py 验证直到全部通过。";;
  esac
}

run_scenario() {
  local dir="$1"; local prompt; prompt=$(prompt_for "$dir")
  local repo="$SCEN/$dir"
  echo "===== [$MODEL_NAME] $dir ====="
  if [ -d "$repo/.orig" ]; then
    rm -rf "$repo/src" "$repo/tests"; cp -R "$repo/.orig/src" "$repo/src"; cp -R "$repo/.orig/tests" "$repo/tests"
  fi
  local base; base=$(cd "$repo" && python3 -m pytest -q --tb=no 2>&1 | tail -1)
  local log="$BENCH/log-$MODEL_NAME-$dir.log"
  fuxi -p -d "$repo" --permission-mode bypassPermissions --max-turns 25 --max-thinking-tokens 8000 "$prompt" > "$log" 2>&1
  local fx=$?
  local final
  if [ "$dir" = "d4_testgen" ]; then
    final=$(cd "$repo" && python3 score.py 2>&1 | grep -E "COVERAGE=|PASSED=|FAILED=" | tr '\n' ' ')
  else
    final=$(cd "$repo" && python3 -m pytest -q --tb=no 2>&1 | tail -1)
  fi
  echo "  baseline: $base"; echo "  fuxi exit: $fx"; echo "  final: $final"
  python3 - "$RESULT" "$dir" "$base" "$final" "$fx" <<'PYEOF'
import json, sys
path, d, base, final, fx = sys.argv[1:6]
data = {}
try: data = json.load(open(path))
except Exception: pass
data[d] = {"baseline": base, "final": final, "fuxi_exit": int(fx)}
json.dump(data, open(path, "w"), ensure_ascii=False, indent=2)
PYEOF
}

for d in d1_bugfix d2_feature d3_refactor d4_testgen d5_review d6_lru d7_graph d8_threadsafe d9_validation d10_regex d11_multifile; do
  run_scenario "$d"
done

echo "}" >> "$RESULT"
echo "===== DONE $MODEL_NAME ====="
cat "$RESULT"
