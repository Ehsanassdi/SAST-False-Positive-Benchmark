import sqlite3

role = input("Enter role: ")
conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

query = "SELECT * FROM accounts WHERE role = '" + role + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
