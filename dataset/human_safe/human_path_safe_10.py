from pathlib import Path

base_dir = Path("storage")
filename = "document.txt"

safe_path = base_dir / filename
print(safe_path)
