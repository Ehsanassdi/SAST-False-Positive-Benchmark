import subprocess

directory = "/tmp"

subprocess.run(["ls", directory], check=True)
