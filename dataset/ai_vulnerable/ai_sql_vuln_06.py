import sqlite3

department = input("Department: ")

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

query = f"SELECT name FROM employees WHERE department = '{department}'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
