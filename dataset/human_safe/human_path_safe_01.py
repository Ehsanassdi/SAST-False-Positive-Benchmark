from pathlib import Path

base_dir = Path("safe_files")
filename = "report.txt"

safe_path = base_dir / filename
print(safe_path)
