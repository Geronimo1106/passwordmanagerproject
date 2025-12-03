#Prototyp, der die einträge in einer Liste gespeichert hat vor Db implementierung
#nicht mehr in benutzung
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

def delete_entry(entry_id):
    for e in password_entries:
        if e["id"] == entry_id:
            password_entries.remove(e)
            return True
    return False

def find_entry_by_id(entry_id):
    for e in password_entries:
        if e["id"] == entry_id:
            return e
    return None