import sqlite3

def create_db():

    conn = sqlite3.connect("databases/train.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS houses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        area REAL,
        bedrooms INTEGER,
        bathrooms INTEGER,
        age INTEGER,
        location INTEGER,
        price REAL
    )
    """)

    conn.commit()
    conn.close()

    conn = sqlite3.connect("databases/test.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS houses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        area REAL,
        bedrooms INTEGER,
        bathrooms INTEGER,
        age INTEGER,
        location INTEGER,
        price REAL
    )
    """)

    conn.commit()
    conn.close()