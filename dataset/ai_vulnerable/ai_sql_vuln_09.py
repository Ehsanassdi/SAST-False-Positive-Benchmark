import sqlite3

title = input("Book title: ")

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

query = "SELECT * FROM books WHERE title = '" + title + "'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
