import secrets
import string
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

    charset = ""
    while length > 0:
        if use_upper == "j":
            charset += string.ascii_uppercase
        if use_lower == "j":
            charset += string.ascii_lowercase
        if use_digits == "j":
            charset += string.digits
        if use_symbols == "j":
            charset += "!@#$%^&*()-_=+[]{};:,.<>/?"
        if not charset:
            break
        password = ''.join(secrets.choice(charset) for i in range(length))
        return password