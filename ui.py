import db
import password_generator
import users

def hauptmenue():
    #Zeigt das Hauptmenü an und gibt die Nutzerauswahl zurück.
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
    #Login-Ablauf: Nutzername eingeben, Masterpasswort einrichten/verifizieren.
    print("=== Login ===")
    user = input("Benutzername: ").strip()

    # 1) Falls Nutzer neu ist Masterpasswort anlegen
    users.setup_master_password(user)

    # 2) Passwort-Verifizierung
    if not users.verify_master_password(user):
        return None # Login fehlgeschlagen

    return user # Erfolgreich eingeloggt

def eintraege_anzeigen(user):
    #Zeigt alle Einträge eines Nutzers tabellarisch an.
    passwort_eintraege = db.get_all_entries(user)
    print("\n--- Gespeicherte Einträge ---")

    # Wenn keine Einträge existieren, abbrechen
    if not passwort_eintraege:
        print("Keine Einträge vorhanden.")
        return False

    # Tabellenkopf
    print(f"{'ID':<4} {'Service':<20} {'Login':<20} {'Passwort'}")
    print("-" * 70)

    # Einträge ausgeben
    for e in passwort_eintraege:
        print(f"{e['id']:<4} {e['service']:<20} {e['login']:<20} {e['password']}")
    return True

def eintraege_filtern(user):
    #Sucht Einträge anhand eines bestimmten Feldes (id, service, login, password).
    print("\n--- Gespeicherte Einträge ---")

    # Attribut wird ausgewählt
    feld = input("Suche nach (id,service,login,password): ").strip()
    if feld not in ("id", "service", "login", "password"):
        print("Bitte einen der Attribute auswählen und Schreibweise beachten.")
        return False
    wert = input("Suche: ")

    # Datensätze aus DB abrufen
    passwort_eintraege = db.get_entry_by_field(user, feld, wert)
    if not passwort_eintraege:
        print("Keine Einträge vorhanden.")
        return False

    # Tabelle ausgeben
    print(f"{'ID':<4} {'Service':<20} {'Login':<20} {'Passwort'}")
    print("-" * 70)

    for e in passwort_eintraege:
        print(f"{e['id']:<4} {e['service']:<20} {e['login']:<20} {e['password']}")
    return True


def eintrag_anlegen(user):
    #Legt einen neuen Passwort-Eintrag an.
    print("\n--- Eintrag Anlegen ---")
    service = input("Service: ")
    login = input("Login: ")
    password = input("Password (Enter für generieren): ")

    # Wenn kein Passwort eingegeben wurde Passwortgenerator nutzen
    if password == "":
        password = passwortgenerieren()

    if not password:
        print("Fehler: Es wurde kein Passwort erzeugt.")
        return

    # Eintrag in der Datenbank speichern
    db.insert(user, service, login, password)
    print("Eintrag angelegt.")

def eintrag_loeschen(user):
    #Löscht einen Eintrag anhand seiner ID.
    # Erst alle Einträge zeigen – wenn keine da sind, abbrechen
    if not eintraege_anzeigen(user):
        return
    print("\n--- Eintrag Löschen ---")
    try:
        eid = input("ID des zu löschenden Eintrags: ")
    except ValueError:
        print("Ungültige Eingabe.")
        return

    # Löschversuch
    if db.delete_entry(user, eid):
        print("Eintrag gelöscht.")
    else:
        print("Eintrag nicht gefunden.")

def eintrag_bearbeiten(user):
    #Ermöglicht das Bearbeiten eines existierenden Eintrags.
    # Ohne Einträge keine Bearbeitung möglich
    if not eintraege_anzeigen(user):
        return None

    print("\n--- Eintrag bearbeiten ---")
    entry_id = input("ID des Eintrags: ")

    entry = db.get_entry_by_id(user, entry_id)

    # Wenn ID nicht existiert
    if not entry:
        print("Eintrag nicht gefunden.")
        return False

    # Aktuelle Werte anzeigen
    print(f"\nAktuelle Werte:")
    print(f"Service:  {entry['service']}")
    print(f"Login:    {entry['login']}")
    print(f"Passwort: {entry['password']}")

    # Neue Werte abfragen
    print("\nNeue Werte (leer lassen = unverändert):")
    new_service = input("Neuer Service: ").strip() or entry["service"]
    new_login   = input("Neuer Login: ").strip() or entry["login"]
    new_pw      = input("Neues Passwort: ").strip() or entry["password"]

    # Änderungen speichern
    success = db.update_entry(user, entry_id, new_service, new_login, new_pw)

    if success:
        print("\nEintrag erfolgreich aktualisiert.")
    else:
        print("\nFehler beim Aktualisieren.")

def passwortgenerieren():
    #Dialog für die Passwortgenerierung und Rückgabe des erzeugten Passworts.
    print("\n--- Passwort generieren ---")
    laenge = input("Laenge (min. 6): ")
    grossbuchstaben = input("Grossbuchstaben (j/n): ")
    kleinbuchstaben = input("Kleinbuchstaben (j/n): ")
    zahlen = input("Zahlen (j/n): ")
    sonderzeichen = input("Sonderzeichen (j/n): ")

    # Passwort mittels Generator erstellen
    pw = password_generator.generate_password(laenge, grossbuchstaben, kleinbuchstaben, zahlen, sonderzeichen)

    # Falls Passwort generiert wurde ausgeben
    if not pw is None:
        print(pw)
    return pw