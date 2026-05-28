import json
import os
import sys


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE", os.getcwd())
    report_path = os.path.join(workspace, "reports", "report.json")
    output_path = os.path.join(workspace, "reports", "feishu_summary.json")

    if not os.path.exists(report_path):
        result = {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "skipped": 0,
            "failed_cases": [],
            "error": f"report.json not found: {report_path}"
        }
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0)

    with open(report_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    summary = data.get("summary", {})
    tests = data.get("tests", [])

    total = summary.get("total", len(tests))
    passed = summary.get("passed", 0)
    failed = summary.get("failed", 0)
    skipped = summary.get("skipped", 0)

    failed_cases = []
    for t in tests:
        if t.get("outcome") == "failed":
            failed_cases.append({
                "nodeid": t.get("nodeid", ""),
                "keywords": list(t.get("keywords", [])) if isinstance(t.get("keywords"), (list, set, tuple)) else [],
                "longrepr": (
                    t.get("call", {}).get("longrepr", "")
                    if isinstance(t.get("call"), dict) else ""
                )
            })

    result = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "failed_cases": failed_cases
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()