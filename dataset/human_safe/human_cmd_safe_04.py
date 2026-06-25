import subprocess

host = "example.com"

subprocess.run(["ping", "-c", "1", host], check=True)
