import password_generator
from models import (
    get_all_entries,
    create_entry,
    delete_entry,
    find_entry_by_id,
)


def hauptmenue():
    print("\n--- Main Menu ---")
    print("1) Alle Einträge anzeigen")
    print("2) Neuen Eintrag hinzufügen")
    print("3) Eintrag bearbeiten")
    print("4) Eintrag löschen")
    print("5) Beenden")

    auswahl = input("Auswahl: ").strip()
    return auswahl

def eintraege_anzeigen():
    password_entries = get_all_entries()
    print("\n--- Gespeicherte Einträge ---")
    if not password_entries:
        print("\nKeine Einträge vorhanden.")
        return False

    print("[ID] Service | Login | Passwort")
    for e in password_entries:
        print(f"[{e['id']}] {e['service']} | {e['login']} | {e['password']}")
    return True

def eintrag_anlegen():
    print("\n--- Eintrag Anlegen ---")
    service = input("Service: ")
    login = input("Login: ")
    password = input("Password: ")
    create_entry(service, login, password)
    print("Eintrag angelegt.")

def eintrag_loeschen():
    if not eintraege_anzeigen():
        return
    print("\n--- Eintrag Löschen ---")
    try:
        eid = int(input("ID des zu löschenden Eintrags: "))
    except ValueError:
        print("Ungültige Eingabe.")
        return

    if delete_entry(eid):
        print("Eintrag gelöscht.")
    else:
        print("Eintrag nicht gefunden.")

def eintrag_bearbeiten():
    if not eintraege_anzeigen():
        return

    print("\n--- Eintrag Bearbeiten ---")
    try:
        eid = int(input("ID des zu bearbeitenden Eintrags: "))
    except ValueError:
        print("Ungültige Eingabe.")
        return

    eintrag = find_entry_by_id(eid)
    if eintrag is None:
        print("Eintrag nicht gefunden.")
        return

    print(f"Service aktuell: {eintrag['service']}")
    neu_service = input("Neuer Service (leer lassen zum Behalten): ").strip()
    if neu_service:
        eintrag["service"] = neu_service

    print(f"Login aktuell: {eintrag['login']}")
    neu_login = input("Neuer Login (leer lassen zum Behalten): ").strip()
    if neu_login:
        eintrag["login"] = neu_login

    print(f"Passwort aktuell: {eintrag['password']}")
    neu_pw = input("Neues Passwort (leer lassen zum Behalten): ").strip()
    if neu_pw:
        eintrag["password"] = neu_pw

    print("Eintrag aktualisiert.")

def passwortgenerieren():
    passswort = password_generator.generate_password()
    return passswort