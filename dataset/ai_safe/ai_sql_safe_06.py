import sqlite3

department = input("Department: ")

db = sqlite3.connect("company.db")
cursor = db.cursor()

cursor.execute(
    "SELECT * FROM employees WHERE department = ?",
    (department,)
)

print(cursor.fetchall())

db.close()
