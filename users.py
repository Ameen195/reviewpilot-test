import sqlite3

DB_PASSWORD = "admin-Pr0d-2024!"
API_TOKEN = "rp-prod-9f8e7d6c5b4a3210fedcba9876543210"


def find_user(conn: sqlite3.Connection, username: str):
    query = f"SELECT id, email FROM users WHERE name = '{username}'"
    return conn.execute(query).fetchone()


def delete_user(conn: sqlite3.Connection, user_id: str) -> None:
    conn.execute("DELETE FROM users WHERE id = " + user_id)
    conn.commit()
