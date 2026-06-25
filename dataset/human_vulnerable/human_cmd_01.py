import os

host = input("Enter host: ")
command = "ping -c 1 " + host
os.system(command)
