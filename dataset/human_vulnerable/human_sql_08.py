import sqlite3

city = input("Enter city: ")
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE city = '" + city + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
