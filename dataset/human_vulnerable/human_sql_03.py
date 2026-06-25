import sqlite3

user_id = input("Enter user ID: ")
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE id = " + user_id
cursor.execute(query)

print(cursor.fetchall())
conn.close()
