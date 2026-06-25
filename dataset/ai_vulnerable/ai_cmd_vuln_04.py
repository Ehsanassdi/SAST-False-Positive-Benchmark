import subprocess

host = input("Enter host: ")
subprocess.run("ping -c 1 " + host, shell=True)
