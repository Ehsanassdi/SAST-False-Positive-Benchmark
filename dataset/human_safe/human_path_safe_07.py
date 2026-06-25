from pathlib import Path

base_dir = Path("data")
filename = "users.csv"

safe_path = base_dir / filename
print(safe_path)
