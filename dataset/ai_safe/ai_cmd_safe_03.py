import subprocess

directory = "logs"

subprocess.run(["ls", directory], check=True)
