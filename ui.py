import db
import password_generator
import users

def hauptmenue():
    print("\n--- Main Menu ---")
    print("1) Alle Einträge anzeigen")
    print("2) Nach Einträgen suchen")
    print("3) Neuen Eintrag hinzufügen")
    print("4) Eintrag bearbeiten")
    print("5) Eintrag löschen")
    print("6) Passwort generieren")
    print("7) Beenden")

    auswahl = input("Auswahl: ").strip()
    return auswahl


def loginmenue():
    print("=== Login ===")
    user = input("Benutzername: ").strip()

    # 1) Falls Nutzer neu ist Masterpasswort anlegen
    users.setup_master_password(user)

    # 2) Passwort-Verifizierung
    if not users.verify_master_password(user):
        return None

    return user


def eintraege_anzeigen(user):
    passwort_eintraege = db.get_all_entries(user)
    print("\n--- Gespeicherte Einträge ---")

    if not passwort_eintraege:
        print("Keine Einträge vorhanden.")
        return False

    print(f"{'ID':<4} {'Service':<20} {'Login':<20} {'Passwort'}")
    print("-" * 70)

    for e in passwort_eintraege:
        print(f"{e['id']:<4} {e['service']:<20} {e['login']:<20} {e['password']}")
    return True

def eintraege_filtern(user):
    print("\n--- Gespeicherte Einträge ---")
    feld = input("Suche nach (id,service,login,password): ").strip()
    if feld not in ("id", "service", "login", "password"):
        print("Bitte einen der Attribute auswählen und Schreibweise beachten.")
        return False
    wert = input("Suche: ")
    passwort_eintraege = db.get_entry_by_field(user, feld, wert)
    if not passwort_eintraege:
        print("Keine Einträge vorhanden.")
        return False

    print(f"{'ID':<4} {'Service':<20} {'Login':<20} {'Passwort'}")
    print("-" * 70)

    for e in passwort_eintraege:
        print(f"{e['id']:<4} {e['service']:<20} {e['login']:<20} {e['password']}")
    return True


def eintrag_anlegen(user):
    print("\n--- Eintrag Anlegen ---")
    service = input("Service: ")
    login = input("Login: ")
    password = input("Password (Enter für generieren): ")
    if password == "":
        password = passwortgenerieren()
    db.insert(user, service, login, password)
    print("Eintrag angelegt.")

def eintrag_loeschen(user):
    if not eintraege_anzeigen(user):
        return
    print("\n--- Eintrag Löschen ---")
    try:
        eid = input("ID des zu löschenden Eintrags: ")
    except ValueError:
        print("Ungültige Eingabe.")
        return

    if db.delete_entry(user, eid):
        print("Eintrag gelöscht.")
    else:
        print("Eintrag nicht gefunden.")

def eintrag_bearbeiten(user):
    if not eintraege_anzeigen(user):
        return None

    print("\n--- Eintrag bearbeiten ---")
    entry_id = input("ID des Eintrags: ")

    entry = db.get_entry_by_id(user, entry_id)
    if not entry:
        print("Eintrag nicht gefunden.")
        return False

    print(f"\nAktuelle Werte:")
    print(f"Service:  {entry['service']}")
    print(f"Login:    {entry['login']}")
    print(f"Passwort: {entry['password']}")

    print("\nNeue Werte (leer lassen = unverändert):")
    new_service = input("Neuer Service: ").strip() or entry["service"]
    new_login   = input("Neuer Login: ").strip() or entry["login"]
    new_pw      = input("Neues Passwort: ").strip() or entry["password"]

    success = db.update_entry(user, entry_id, new_service, new_login, new_pw)

    if success:
        print("\nEintrag erfolgreich aktualisiert.")
    else:
        print("\nFehler beim Aktualisieren.")

def passwortgenerieren():
    print("\n--- Passwort generieren ---")
    laenge = input("Laenge (min. 6): ")
    grossbuchstaben = input("Grossbuchstaben (j/n): ")
    kleinbuchstaben = input("Kleinbuchstaben (j/n): ")
    zahlen = input("Zahlen (j/n): ")
    sonderzeichen = input("Sonderzeichen (j/n): ")
    pw = password_generator.generate_password(laenge, grossbuchstaben, kleinbuchstaben, zahlen, sonderzeichen)
    if not pw is None:
        print(pw)