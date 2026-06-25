import subprocess

host = input("Enter IP address: ")
subprocess.call("ping -c 1 " + host, shell=True)
