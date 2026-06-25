import sqlite3

city = input("City: ")

conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

query = "SELECT * FROM customers WHERE city = '" + city + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
