import sqlite3

keyword = input("Search keyword: ")
conn = sqlite3.connect("articles.db")
cursor = conn.cursor()

query = "SELECT * FROM articles WHERE title LIKE '%" + keyword + "%'"
cursor.execute(query)

print(cursor.fetchall())
conn.close()
