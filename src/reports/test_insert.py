import sqlite3
from datetime import datetime


conn = sqlite3.connect("database/compliance.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO violations
(
timestamp,
predicted_class,
severity,
policy_section,
confidence,
image_path
)
VALUES (?, ?, ?, ?, ?, ?)
""",
(
str(datetime.now()),
"1_unauthorized_intervention",
"HIGH",
"4.3.2",
97.5,
"sample.jpg"
))

conn.commit()

print("Record Inserted")

conn.close()