import sqlite3

department = input("Enter department: ")
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

query = "SELECT * FROM employees WHERE department = '" + department + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
