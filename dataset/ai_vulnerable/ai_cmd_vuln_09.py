import os

process = input("Enter process name: ")
os.system("pgrep " + process)
