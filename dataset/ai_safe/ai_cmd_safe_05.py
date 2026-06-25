import subprocess

service_name = "ssh"

subprocess.run(["systemctl", "status", service_name], check=False)
