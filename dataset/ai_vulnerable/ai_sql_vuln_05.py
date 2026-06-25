import sqlite3

status = input("Order status: ")

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

query = "SELECT * FROM orders WHERE status = '" + status + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
