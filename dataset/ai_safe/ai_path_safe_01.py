from pathlib import Path

base_directory = Path("documents")
file_name = "report.txt"

safe_path = base_directory / file_name

print(safe_path)
