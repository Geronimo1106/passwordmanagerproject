import secrets
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

    # Länge prüfen
    while True:
        try:
            length = int(length)
            if length <= 5:
                print("Fehler: Die Länge muss größer als 6 sein!")
                length = input("Länge: ")
                continue
            break
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben!")
            length = input("Länge: ")

    # Zeichen-Auswahl prüfen
    while True:
        charset = ""
        if use_upper == "j":
            charset += string.ascii_uppercase
        if use_lower == "j":
            charset += string.ascii_lowercase
        if use_digits == "j":
            charset += string.digits
        if use_symbols == "j":
            charset += "!@#$%^&*()-_=+[]{};:,.<>/?"

        if charset:
            break  # gültig
        else:
            print("Fehler: Es muss mindestens eine Zeichengruppe ausgewählt werden!")
            use_upper   = input("Großbuchstaben (j/n): ").lower().strip()
            use_lower   = input("Kleinbuchstaben (j/n): ").lower().strip()
            use_digits  = input("Zahlen (j/n): ").lower().strip()
            use_symbols = input("Sonderzeichen (j/n): ").lower().strip()

    # Passwort generieren
    password = ''.join(secrets.choice(charset) for _ in range(length))
    return password
