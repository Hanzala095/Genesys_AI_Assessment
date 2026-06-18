import sqlite3


conn = sqlite3.connect("database/compliance.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM violations"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()