import json

from resourses import config


class SAMJson:
    def __init__(self):
        pass

    def write_to_json(self, data):
        with open(config.JSON_PATH, 'w', encoding='utf-8') as accs_j:
            json.dump(data, accs_j, indent=2, ensure_ascii=False)

    def read_json(self):
        with open(config.JSON_PATH, 'r', encoding='utf-8') as accs_j:
            try:
                accounts = json.load(accs_j)
            except Exception:
                accounts = []
        return accounts
