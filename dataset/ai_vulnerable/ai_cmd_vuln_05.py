import subprocess

filename = input("Enter file: ")
subprocess.run("cat " + filename, shell=True)
