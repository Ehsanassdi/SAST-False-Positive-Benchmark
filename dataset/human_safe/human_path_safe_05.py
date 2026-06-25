from pathlib import Path

base_dir = Path("logs")
filename = "app.log"

safe_path = base_dir / filename
print(safe_path)
