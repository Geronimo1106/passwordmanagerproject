from sympy.codegen import Print

from models import (
    get_all_entries,
    create_entry,
    delete_entry,
)


def hauptmenue():
    print("\n--- Passwortmanager ---")
    print("1) Alle Einträge anzeigen")
    print("2) Neuen Eintrag hinzufügen")
    print("3) Eintrag bearbeiten")
    print("4) Eintrag löschen")
    print("5) Beenden")

    auswahl = input("Auswahl: ").strip()
    return auswahl

def eintraege_anzeigen():
    password_entries = get_all_entries()
    if not password_entries:
        print("\nKeine Einträge vorhanden.")
        return

    print("\n--- Gespeicherte Einträge ---")
    for e in password_entries:
        print(f"[{e['id']}] {e['service']} | {e['login']} | {e['password']}")

def eintrag_anlegen():
    print("\n--- Eintrag Anlegen ---")
    service = input("Service: ")
    login = input("Login: ")
    password = input("Password: ")
    create_entry(service, login, password)
    print("Eintrag angelegt.")

def eintrag_loeschen():
    print("\n--- Eintrag Löschen ---")
    eintraege_anzeigen()
    try:
        eid = int(input("ID des zu löschenden Eintrags: "))
    except ValueError:
        print("Ungültige Eingabe.")
        return

    if delete_entry(eid):
        print("Eintrag gelöscht.")
    else:
        print("Eintrag nicht gefunden.")

#def eintrag_bearbeiten():