import sqlite3

title = input("Enter book title: ")

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM books WHERE title = ?", (title,))

print(cursor.fetchall())

conn.close()
