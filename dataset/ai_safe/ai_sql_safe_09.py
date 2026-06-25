import sqlite3

title = input("Book title: ")

db = sqlite3.connect("library.db")
cursor = db.cursor()

cursor.execute(
    "SELECT * FROM books WHERE title = ?",
    (title,)
)

print(cursor.fetchall())

db.close()
