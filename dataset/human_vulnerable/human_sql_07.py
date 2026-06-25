import sqlite3

order_id = input("Enter order ID: ")
conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

query = "SELECT * FROM orders WHERE order_id = " + order_id
cursor.execute(query)

print(cursor.fetchall())
conn.close()
