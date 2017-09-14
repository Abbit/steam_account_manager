import json

from resourses import config


class SAMJson:
    def __init__(self):
        pass

    def write_to_json(self, data):
        with open(config.JSON_PATH, 'w', encoding='utf-8') as accs_j:
            json.dump(data, accs_j, indent=2)

    def read_json(self):
        try:
            with open(config.JSON_PATH, 'r', encoding='utf-8') as accs_j:
                try:
                    accounts = json.load(accs_j)
                except Exception:
                    accounts = []
        except:
            return []
        return accounts
