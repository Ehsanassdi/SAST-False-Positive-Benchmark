from pathlib import Path

allowed_files = {"manual.pdf", "guide.pdf"}

requested_file = "manual.pdf"

if requested_file in allowed_files:
    print(Path("files") / requested_file)
