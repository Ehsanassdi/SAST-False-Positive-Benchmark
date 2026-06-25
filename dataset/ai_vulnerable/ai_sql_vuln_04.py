import sqlite3

product = input("Product name: ")

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

query = f"SELECT * FROM products WHERE name = '{product}'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
