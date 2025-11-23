import ui

def main():
    ui.loginmenu()
    while True:
        auswahl = ui.hauptmenue()

        if auswahl == "1":
            ui.eintraege_anzeigen()
        elif auswahl == "2":
            ui.eintrag_anlegen()
        elif auswahl == "3":
            ui.eintrag_bearbeiten()
        elif auswahl == "4":
            ui.eintrag_loeschen()
        elif auswahl == "5":
            ui.passwortgenerieren()
        elif auswahl == "6":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()