import sqlite3

city = input("Enter city: ")

conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM customers WHERE city = ?", (city,))

print(cursor.fetchall())

conn.close()
