import subprocess

log_file = input("Enter log file: ")
subprocess.call("grep error " + log_file, shell=True)
