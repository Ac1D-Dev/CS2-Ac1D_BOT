import json

NICKNAME_FILE = "nicknames.json"

def load_data(nickname_path):
    try:
        with open(nickname_path, "r") as nicknames:
            return json.load(nicknames)   # transforme le contenu JSON en dict Python
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_data(nickname_path, data):
    with open(nickname_path, "w") as nicknames:
        json.dump(data, nicknames)