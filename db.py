import sqlite3
#https://docs.python.org/3/library/sqlite3.html
#https://www.w3schools.com/sql/sql_autoincrement.asp

DB_FILE = "passwords.db"

def connect():
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS password_entries(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL)""")