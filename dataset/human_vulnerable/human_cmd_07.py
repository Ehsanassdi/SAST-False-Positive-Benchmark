import os

service = input("Enter service name: ")
os.system("systemctl status " + service)
