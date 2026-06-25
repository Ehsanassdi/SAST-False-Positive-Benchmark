from pathlib import Path

allowed_files = {"report.txt", "summary.txt"}
filename = "report.txt"

if filename in allowed_files:
    print(Path("files") / filename)
