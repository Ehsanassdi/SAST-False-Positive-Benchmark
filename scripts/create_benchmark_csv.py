import json, csv, os

outputs = [
    ("Semgrep", "results/semgrep/semgrep_results.json"),
    ("Bandit", "results/bandit/bandit_results.json"),
    ("Snyk", "results/snyk/snyk_results.json"),
]

rows = []

def add(tool, filename, rule, severity, message):
    rows.append({
        "Tool": tool,
        "Filename": filename,
        "Rule_ID": rule,
        "Severity": severity,
        "Message": message
    })

# Semgrep
with open("results/semgrep/semgrep_results.json") as f:
    data = json.load(f)
for r in data.get("results", []):
    add("Semgrep", r.get("path", ""), r.get("check_id", ""), r.get("extra", {}).get("severity", ""), r.get("extra", {}).get("message", ""))

# Bandit
with open("results/bandit/bandit_results.json") as f:
    data = json.load(f)
for r in data.get("results", []):
    add("Bandit", r.get("filename", ""), r.get("test_id", ""), r.get("issue_severity", ""), r.get("issue_text", ""))

# CodeQL SARIF
with open("results/codeql/codeql_results.sarif") as f:
    data = json.load(f)
for run in data.get("runs", []):
    for r in run.get("results", []):
        locs = r.get("locations", [])
        filename = ""
        if locs:
            filename = locs[0].get("physicalLocation", {}).get("artifactLocation", {}).get("uri", "")
        add("CodeQL", filename, r.get("ruleId", ""), r.get("level", ""), r.get("message", {}).get("text", ""))

# Snyk
with open("results/snyk/snyk_results.json") as f:
    data = json.load(f)
for run in data.get("runs", []):
    for r in run.get("results", []):
        locs = r.get("locations", [])
        filename = ""
        if locs:
            filename = locs[0].get("physicalLocation", {}).get("artifactLocation", {}).get("uri", "")
        add("Snyk", filename, r.get("ruleId", ""), r.get("level", ""), r.get("message", {}).get("text", ""))

os.makedirs("results", exist_ok=True)

with open("results/benchmark_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Tool", "Filename", "Rule_ID", "Severity", "Message"])
    writer.writeheader()
    writer.writerows(rows)

summary = {}
for r in rows:
    summary[r["Tool"]] = summary.get(r["Tool"], 0) + 1

with open("results/metrics_summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Tool", "Total_Findings"])
    for tool, count in summary.items():
        writer.writerow([tool, count])

print("Created results/benchmark_results.csv")
print("Created results/metrics_summary.csv")
print(f"Total findings: {len(rows)}")
