import sqlite3
import os


DB_PATH = "database/compliance.db"


def create_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS violations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        predicted_class TEXT,
        severity TEXT,
        policy_section TEXT,
        confidence REAL,
        image_path TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database Ready")


if __name__ == "__main__":
    create_database()