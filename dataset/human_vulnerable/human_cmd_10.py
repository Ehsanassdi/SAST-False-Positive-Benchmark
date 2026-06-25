import subprocess

process = input("Enter process name: ")
subprocess.call("ps aux | grep " + process, shell=True)
