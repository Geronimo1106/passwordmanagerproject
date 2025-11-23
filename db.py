import sqlite3
import string
from datetime import datetime
#https://docs.python.org/3/library/sqlite3.html
#https://www.w3schools.com/sql/sql_autoincrement.asp
password_entries = []
DB_FILE = "passwords.db"
def connect(user):
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row
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

def get_all_entries(user):
    con, cur, table = connect(user)
    password_entries.clear()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    con.close()
    for row in rows:
        entry = {
            "id": row["id"],
            "service": row["service"],
            "login": row["login"],
            "password": row["password"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }
        password_entries.append(entry)

    return password_entries


def get_entry_by_field(user, field, value):
    con, cur, table = connect(user)
    password_entries.clear()
    allowed_fields = {"id", "service", "login", "password", "created_at", "updated_at"}
    if field not in allowed_fields:
        con.close()
        raise ValueError(f"Ungültiges Feld: {field}")

    search = f"SELECT * FROM {table} WHERE {field} = ?"
    cur.execute(search, (value,))
    rows = cur.fetchall()
    con.close()

    if not rows:
        return []

    for row in rows:
        entry = {
            "id": row["id"],
            "service": row["service"],
            "login": row["login"],
            "password": row["password"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }
        password_entries.append(entry)
    return [entry]

def get_entry_by_id(user, entry_id):
    con, cur, table = connect(user)
    cur.execute(
        f"SELECT id, service, login, password FROM {table} WHERE id = ?",
        (entry_id,)
    )
    row = cur.fetchone()
    con.close()

    if row is None:
        return None

    entry = {
        "id": row["id"],
        "service": row["service"],
        "login": row["login"],
        "password": row["password"],
    }
    return entry

def update_entry(user, entry_id, service, login, password):
    con, cur, table = connect(user)
    cur.execute(
        f"""
        UPDATE {table}
        SET service = ?, login = ?, password = ?
        WHERE id = ?
        """,
        (service, login, password, entry_id)
    )

    con.commit()
    con.close()
    return cur.rowcount > 0
