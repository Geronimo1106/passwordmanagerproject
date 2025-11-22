import sqlite3
import string
from datetime import datetime
#https://docs.python.org/3/library/sqlite3.html
#https://www.w3schools.com/sql/sql_autoincrement.asp

DB_FILE = "passwords.db"
def connect(user):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    table = f"password_entries_{user}"
    #cur.execute("""DROP TABLE password_entries_Gero""")
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {table}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                login TEXT NOT NULL,
                password TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL)""")
    return con, cur, table

def insert(user, service, login, password):
    now = datetime.now().isoformat()
    con, cur, table = connect(user)
    cur.execute(f"""INSERT INTO {table} (service, login, password, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)""",
        (service, login, password, now, now)
    )
    con.commit()
    con.close()

def select_all(user):
    con, cur, table = connect(user)