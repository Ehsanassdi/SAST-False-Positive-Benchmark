import sqlite3

email = input("Enter email: ")
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE email = '" + email + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
