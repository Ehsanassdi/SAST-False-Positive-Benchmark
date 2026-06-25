import sqlite3

category = input("Category: ")

db = sqlite3.connect("inventory.db")
cursor = db.cursor()

cursor.execute(
    "SELECT * FROM items WHERE category = ?",
    (category,)
)

print(cursor.fetchall())

db.close()
