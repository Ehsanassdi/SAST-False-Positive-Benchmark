import subprocess

username = "ehsan"

subprocess.run(["id", username], check=True)
