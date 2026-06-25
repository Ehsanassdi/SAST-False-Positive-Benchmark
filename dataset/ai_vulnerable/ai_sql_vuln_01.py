import sqlite3

username = input("Username: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username = '" + username + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
