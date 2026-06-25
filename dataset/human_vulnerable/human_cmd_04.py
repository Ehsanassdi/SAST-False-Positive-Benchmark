import subprocess

folder = input("Enter folder name: ")
subprocess.call("ls " + folder, shell=True)
