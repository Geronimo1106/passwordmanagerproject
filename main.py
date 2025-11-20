from models import PasswortEintrag
import ui

def main():
    # Später hier: Login / Master-Passwort
    eintraege: list[PasswortEintrag] = []

    while True:
        auswahl = ui.hauptmenue()

        if auswahl == "1":
            ui.eintraege_anzeigen(eintraege)
        elif auswahl == "2":
            ui.eintrag_anlegen(eintraege)
        elif auswahl == "3":
            ui.eintrag_bearbeiten(eintraege)
        elif auswahl == "4":
            ui.eintrag_loeschen(eintraege)
        elif auswahl == "5":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()