password_entries = []

def create_entry(service, login, password):
    if password_entries:
        new_id = max(e["id"] for e in password_entries) + 1
    else:
        new_id = 1

    entry = {
        "id": new_id,
        "service": service,
        "login": login,
        "password": password,
    }
    password_entries.append(entry)
    return entry


def get_all_entries():
    return password_entries