import sqlite3

product = input("Product: ")

db = sqlite3.connect("shop.db")
cursor = db.cursor()

statement = "SELECT * FROM products WHERE name = ?"

cursor.execute(statement, (product,))

print(cursor.fetchall())

db.close()
