import sqlite3

user_id = input("User ID: ")

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

query = "SELECT balance FROM accounts WHERE id = " + user_id
cursor.execute(query)

print(cursor.fetchone())
conn.close()
