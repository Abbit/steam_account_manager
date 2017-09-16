# coding=utf-8
import base64
from models.account import Account
from utility.sam_json import SAMJson


class SAMAccountModel(object):
    @staticmethod
    def create_acc(login, password, steamlink, description):
        account = Account(
            login=login,
            password=password,
            steamlink=steamlink,
            description=description)
        return account

    @classmethod
    def create_acc_from_json(cls, acc):
        login = acc['login']
        password = base64.b64decode(acc['password']).decode('utf-8')
        steamlink = acc['steamlink']
        description = acc['description']
        account = cls.create_acc(login, password, steamlink, description)
        return account

    @classmethod
    def create_new_acc(cls, login, password, steamlink, description):
        account = cls.create_acc(login, password, steamlink, description)
        cls.write_acc(account)
        return account

    @classmethod
    def take_accs(cls):
        accs = SAMJson.read_json()
        accounts = []
        for acc in accs:
            accounts.append(cls.create_acc_from_json(acc))
        return accounts

    @classmethod
    def take_acc(cls, key):
        acc = cls.find_acc(key)
        return cls.create_acc_from_json(acc)

    @staticmethod
    def write_acc(acc):
        if acc.login is None or acc.password is None:
            return False
        else:
            account = {
                'login': acc.login,
                'password': base64.b64encode(bytes(acc.password, 'utf-8')).decode('utf-8'),
                'steamlink': acc.steamlink,
                'description': acc.description,
            }
            accs = SAMJson.read_json()
            accs.append(account)
            SAMJson.write_to_json(accs)
            return True

    @classmethod
    def delete_acc(cls, key):
        accs = SAMJson.read_json()
        accs.remove(cls.find_acc(key))
        SAMJson.write_to_json(accs)

    @staticmethod
    def find_acc(data):
        if data.find('(') != -1:
            login = data[data.index('(')+1: -1]
        else:
            login = data
        accs = SAMJson.read_json()
        for acc in accs:
            if login in acc.values():
                return acc
        return False
