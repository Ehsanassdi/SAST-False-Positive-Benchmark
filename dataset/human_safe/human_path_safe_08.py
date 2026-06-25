from pathlib import Path

allowed_name = "backup.zip"
safe_path = Path("backups") / allowed_name

print(safe_path)
