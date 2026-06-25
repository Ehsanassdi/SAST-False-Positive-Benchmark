import sqlite3

category = input("Category: ")

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

query = f"SELECT * FROM items WHERE category = '{category}'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
