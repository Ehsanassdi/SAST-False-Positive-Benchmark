import subprocess

target_host = "example.com"

subprocess.run(["ping", "-c", "1", target_host], check=True)
