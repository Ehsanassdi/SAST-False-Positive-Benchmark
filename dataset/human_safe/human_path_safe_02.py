from pathlib import Path

base_dir = Path("documents")
filename = "notes.txt"

safe_path = base_dir / filename
print(safe_path)
