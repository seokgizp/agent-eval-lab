import json
import time
from pathlib import Path

CASES = Path(__file__).with_name("cases.json")


def keyword_score(answer, expect):
    hits = sum(1 for kw in expect if kw.lower() in answer.lower())
    return hits / max(1, len(expect))


def run(agent_fn, cases):
    rows = []
    for c in cases:
        t0 = time.time()
        answer = agent_fn(c["input"])
        rows.append({
            "name": c["name"],
            "score": keyword_score(answer, c["expect_keywords"]),
            "latency_s": round(time.time() - t0, 2),
        })
    return rows


def mock_agent(prompt):
    # replace with your chain: llm.call(prompt) etc
    return "echo: " + prompt


def main():
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    rows = run(mock_agent, cases)
    for r in rows:
        print("%-24s score=%.2f latency=%.2fs"
              % (r["name"], r["score"], r["latency_s"]))
    passed = sum(1 for r in rows if r["score"] >= 0.8)
    print("passed %d/%d" % (passed, len(rows)))
    raise SystemExit(0 if passed == len(rows) else 1)


if __name__ == "__main__":
    main()
