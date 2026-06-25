import sqlite3

category = input("Enter category: ")

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM items WHERE category = ?", (category,))

print(cursor.fetchall())

conn.close()
