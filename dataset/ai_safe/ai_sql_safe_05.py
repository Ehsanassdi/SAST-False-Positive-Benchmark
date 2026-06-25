import sqlite3

status = input("Status: ")

db = sqlite3.connect("orders.db")
cursor = db.cursor()

cursor.execute(
    "SELECT * FROM orders WHERE status = ?",
    (status,)
)

print(cursor.fetchall())

db.close()
