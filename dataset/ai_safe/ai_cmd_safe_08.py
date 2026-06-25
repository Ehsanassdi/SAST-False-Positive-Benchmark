import subprocess

process_name = "python"

subprocess.run(["pgrep", process_name], check=False)
