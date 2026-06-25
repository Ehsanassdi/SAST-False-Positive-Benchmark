import subprocess

file_path = "report.txt"

subprocess.run(["wc", "-l", file_path], check=True)
