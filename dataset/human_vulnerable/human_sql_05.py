import sqlite3

customer = input("Enter customer name: ")
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

query = "SELECT * FROM customers WHERE name = '" + customer + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
