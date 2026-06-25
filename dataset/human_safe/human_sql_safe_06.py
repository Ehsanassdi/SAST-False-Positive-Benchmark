import sqlite3

department = input("Enter department: ")

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM employees WHERE department = ?", (department,))

print(cursor.fetchall())

conn.close()
