import sqlite3
from datetime import datetime
#https://docs.python.org/3/library/sqlite3.html
#https://www.w3schools.com/sql/sql_autoincrement.asp
password_entries = []

def connect(user):
    """
    Stellt eine Verbindung zur Benutzerdatenbank her.
    Jede*r Benutzer*in erhält eine eigene DB, z.B. 'alice_passwords.db'.

    Es wird automatisch eine Tabelle für den Benutzer angelegt, falls sie noch nicht existiert.
    """
    DB_FILE = f"{user}_passwords.db"
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    table = f"password_entries_{user}"
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {table}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                login TEXT NOT NULL,
                password TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL)""")
    return con, cur, table

def insert(user, service, login, password):
    """
    Legt einen neuen Eintrag in der Datenbank an.
    created_at und updated_at werden automatisch gesetzt.
    """
    now = datetime.now().isoformat()
    con, cur, table = connect(user)
    cur.execute(f"""INSERT INTO {table} (service, login, password, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)""",
        (service, login, password, now, now)
    )
    con.commit()
    con.close()

def get_all_entries(user):
    """
    Gibt alle Einträge eines Benutzers als Liste von Dicts zurück.
    """
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
    """
    Sucht Einträge anhand eines bestimmten Feldes.
    Nur bestimmte Felder sind erlaubt, um SQL-Injections zu verhindern.
    """
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
    """
    Holt einen Eintrag anhand seiner ID.
    Gibt ein Dict oder None zurück.
    """
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
    """
    Aktualisiert einen Eintrag anhand seiner ID.
    Gibt True zurück, wenn eine Zeile aktualisiert wurde.
    """
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
    updated_rows = cur.rowcount
    con.close()
    return updated_rows > 0

def delete_entry(user, entry_id):
    """
    Löscht einen Eintrag anhand seiner ID.
    Gibt True zurück, wenn etwas gelöscht wurde.
    """
    con, cur, table = connect(user)
    cur = con.cursor()

    cur.execute(
        f"""
        DELETE FROM {table}
        WHERE id = ?
        """,
        (entry_id)
    )

    con.commit()
    deleted = cur.rowcount
    con.close()

    return deleted > 0
