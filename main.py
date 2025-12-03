import ui

def main():
    # Startet das Login-Menü und gibt den eingeloggten Benutzer zurück.
    # Wenn kein Benutzer zurückgegeben wird (Login abgebrochen/fehlgeschlagen),
    # wird das Programm direkt beendet.
    user = ui.loginmenue()
    if not user:
        return

    # Hauptprogrammschleife – zeigt immer wieder das Hauptmenü an,
    # bis der Nutzer das Programm beendet.
    while True:
        auswahl = ui.hauptmenue()

        if auswahl == "1":
            ui.eintraege_anzeigen(user)
        elif auswahl == "2":
            ui.eintraege_filtern(user)
        elif auswahl == "3":
            ui.eintrag_anlegen(user)
        elif auswahl == "4":
            ui.eintrag_bearbeiten(user)
        elif auswahl == "5":
            ui.eintrag_loeschen(user)
        elif auswahl == "6":
            ui.passwortgenerieren()
        elif auswahl == "7":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()