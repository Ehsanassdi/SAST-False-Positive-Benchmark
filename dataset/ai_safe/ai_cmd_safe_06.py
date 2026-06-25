import subprocess

report_file = "report.txt"

subprocess.run(["wc", "-l", report_file], check=True)
