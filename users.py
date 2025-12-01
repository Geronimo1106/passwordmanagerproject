import os
import hashlib
import sqlite3

DB_FILE = "password.db"

def connect(user):
    DB_FILE = f"{user}_passwords.db"
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    table = f"master_auth_{user}"
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            user TEXT PRIMARY KEY,
            salt BLOB NOT NULL,
            pw_hash BLOB NOT NULL
        )
    """)
    return con, cur, table

def setup_master_password(user):
    con, cur, table = connect(user)

    # Prüfen, ob es für diesen User schon einen Eintrag gibt
    cur.execute(f"SELECT 1 FROM {table} WHERE user = ?", (user,))
    if cur.fetchone():
        con.close()
        return  # schon vorhanden

    while True:
        print("\n=== Master-Passwort festlegen ===")
        pw1 = input("Neues Master-Passwort: ")
        pw2 = input("Master-Passwort wiederholen: ")

        if pw1 != pw2:
            print("Passwörter stimmen nicht überein. Nochmal.")
            continue

        if len(pw1) < 6:
            print("Bitte ein längeres Passwort wählen (mind. 6 Zeichen).")
            continue

        # Salt erzeugen
        salt = os.urandom(16)
        # Hash mit PBKDF2
        pw_hash = hashlib.pbkdf2_hmac("sha256", pw1.encode(), salt, 200_000)

        cur.execute(
            f"INSERT INTO {table} (user, salt, pw_hash) VALUES (?, ?, ?)",
            (user, salt, pw_hash)
        )
        con.commit()
        con.close()

        print("Master-Passwort wurde gespeichert.")
        break

def verify_master_password(user):
    con, cur, table = connect(user)

    cur.execute(f"SELECT salt, pw_hash FROM {table} WHERE user = ?", (user,))
    row = cur.fetchone()

    # Kein Eintrag
    if row is None:
        setup_master_password(user)
        cur.execute(f"SELECT salt, pw_hash FROM {table} WHERE user = ?", (user,))
        row = cur.fetchone()
        if row is None:
            print("Fehler: Kein Master-Passwort gefunden.")
            return False

    salt, saved_hash = row
    con.close()

    print("\n=== Login mit Master-Passwort ===")
    for attempt in range(3):
        pw = input("Master-Passwort: ")
        pw_hash = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, 200_000)

        if pw_hash == saved_hash:
            print("Login erfolgreich.\n")
            return True
        else:
            print("Falsches Passwort.")

    print("Zu viele Fehlversuche. Programm wird beendet.")
    return False