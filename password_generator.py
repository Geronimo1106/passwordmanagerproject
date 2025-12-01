import secrets
import string
#https://docs.python.org/3/library/secrets.html
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

    while True:
        try:
            length = int(length)
            if length <= 0:
                print("Fehler: Die Länge muss größer als 0 sein!")
                length = input("Laenge: ")
                continue
            break
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben!")
            length = input("Laenge: ")

    charset = ""
    if use_upper == "j":
        charset += string.ascii_uppercase
    if use_lower == "j":
        charset += string.ascii_lowercase
    if use_digits == "j":
        charset += string.digits
    if use_symbols == "j":
        charset += "!@#$%^&*()-_=+[]{};:,.<>/?"

    if not charset:
        print("Fehler: Es muss mindestens eine Zeichengruppe ausgewählt werden!")
        return None

    password = ''.join(secrets.choice(charset) for i in range(length))
    return password