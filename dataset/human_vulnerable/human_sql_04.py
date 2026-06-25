import sqlite3

product = input("Enter product name: ")
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

query = "SELECT * FROM products WHERE name = '" + product + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
