# coding=utf-8
import json

from resourses import config


class SAMJson:
    @staticmethod
    def write_to_json(data):
        with open(config.JSON_PATH, 'w', encoding='utf-8') as accs_j:
            json.dump(data, accs_j, indent=2)

    @staticmethod
    def read_json():
        try:
            with open(config.JSON_PATH, 'r', encoding='utf-8') as accs_j:
                try:
                    accounts = json.load(accs_j)
                except:
                    accounts = []
        except:
            return []
        return accounts
