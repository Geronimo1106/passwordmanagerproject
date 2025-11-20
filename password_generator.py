import secrets
import string

length: int = 16
use_upper: bool = True
use_lower: bool = True
use_digits: bool = True
use_symbols: bool = True


def generate_password(length, use_upper, use_lower, use_digits) ->str:

    charset = ""
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += "!@#$%^&*()-_=+[]{};:,.<>/?"

    if not charset:
        raise ValueError("Mindestens ein Zeichensatz muss aktiviert sein!")

    # Passwort-Liste, um sicherzustellen, dass jede aktivierte Gruppe vorkommt
    password_chars = []

    if use_upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password_chars.append(secrets.choice(string.digits))
    if use_symbols:
        password_chars.append(secrets.choice("!@#$%^&*()-_=+[]{};:,.<>/?"))

    # Rest zufällig auffüllen
    while len(password_chars) < length:
        password_chars.append(secrets.choice(charset))

    # Durchmischen, damit die Pflicht-Zeichen nicht immer am Anfang sind
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
