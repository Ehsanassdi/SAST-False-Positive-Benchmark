import sqlite3

city = input("City: ")

db = sqlite3.connect("customers.db")
cursor = db.cursor()

cursor.execute(
    "SELECT * FROM customers WHERE city = ?",
    (city,)
)

print(cursor.fetchall())

db.close()
