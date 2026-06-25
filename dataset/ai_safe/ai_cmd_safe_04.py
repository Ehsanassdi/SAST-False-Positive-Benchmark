import subprocess

user_name = "student"

subprocess.run(["id", user_name], check=True)
