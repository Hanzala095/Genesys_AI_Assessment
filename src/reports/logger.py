import sqlite3
from datetime import datetime


DB_PATH = "database/compliance.db"


def log_detection(
    predicted_class,
    severity,
    policy_section,
    confidence,
    image_path
):

    conn = sqlite3.connect(DB_PATH)

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
        predicted_class,
        severity,
        policy_section,
        confidence,
        image_path
    ))

    conn.commit()

    conn.close()

    print("Detection Logged")