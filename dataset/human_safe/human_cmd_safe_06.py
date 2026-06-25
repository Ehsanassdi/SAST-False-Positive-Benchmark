import subprocess

service = "ssh"

subprocess.run(["systemctl", "status", service], check=False)
