import sqlite3

status = input("Enter order status: ")

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM orders WHERE status = ?", (status,))

print(cursor.fetchall())

conn.close()
