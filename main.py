import ui

def main():
    user = ui.loginmenue()
    if not user:
        return

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