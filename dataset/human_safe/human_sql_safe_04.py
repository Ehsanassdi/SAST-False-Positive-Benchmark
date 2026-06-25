import sqlite3

product_name = input("Enter product name: ")

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM products WHERE name = ?", (product_name,))

print(cursor.fetchall())

conn.close()
