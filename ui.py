from models import (
    get_all_entries,
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
        print("Keine Einträge vorhanden.")
        return

    print("\n--- Gespeicherte Einträge ---")
    for e in password_entries:
        print(f"[{e['id']}] {e['service']} | {e['login']} | {e['password']}")

#def eintrag_anlegen:
#def eintrag_loeschen:
#def eintrag_bearbeiten: