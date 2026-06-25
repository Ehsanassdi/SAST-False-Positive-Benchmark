import sqlite3

email = input("Email: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = f"SELECT * FROM users WHERE email = '{email}'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
