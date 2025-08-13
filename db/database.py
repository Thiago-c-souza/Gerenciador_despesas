import sqlite3 as sql
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent /"data.db"

def get_conn():
    conn = sql.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS despesas (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     valor REAL NOT NULL,
                     data TEXT NOT NULL,  --formato ISO: YYYY-MM-DD
                     categoria TEXT NOT NULL,
                     descricao TEXT
                     );
""")