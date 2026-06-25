import subprocess

domain = input("Enter domain: ")
command = "nslookup " + domain
subprocess.call(command, shell=True)
