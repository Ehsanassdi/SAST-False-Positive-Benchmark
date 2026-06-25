import sqlite3

account_id = int(input("Account ID: "))

db = sqlite3.connect("accounts.db")
cursor = db.cursor()

cursor.execute(
    "SELECT balance FROM accounts WHERE id = ?",
    (account_id,)
)

print(cursor.fetchone())

db.close()
