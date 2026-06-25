import subprocess

folder = input("Enter folder: ")
subprocess.call("find " + folder + " -type f", shell=True)
