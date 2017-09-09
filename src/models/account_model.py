import base64
from models.account import Account
from utility.sam_image import SAMImage
from utility.sam_json import SAMJson


class SAMAccountModel(object):
    def __init__(self):
        self.sam_json = SAMJson()
        self.sam_image = SAMImage()

    def create_acc(self, login, password, steamlink, description):
        account = Account(
            login=login,
            password=password,
            steamlink=steamlink,
            description=description)
        return account

    def create_new_acc(self, login, password, steamlink, description):
        account = self.create_acc(login, password, steamlink, description)
        self.write_acc(account)
        return account

    def take_accs(self):
        accs = self.sam_json.read_json()
        accounts = []
        for acc in accs:
            login = acc['login']
            password = base64.b64decode(acc['password']).decode('utf-8')
            steamlink = acc['steamlink']
            description = acc['description']
            account = self.create_acc(login, password, steamlink, description)
            accounts.append(account)

        return accounts

    def take_acc(self, key):
        acc = self.find_acc(key)
        login = acc['login']
        password = base64.b64decode(acc['password']).decode('utf-8')
        steamlink = acc['steamlink']
        description = acc['description']
        account = self.create_acc(login, password, steamlink, description)
        return account

    def write_acc(self, acc):
        if acc.login is None or acc.password is None:
            return False
        else:
            account = {
                'login': acc.login,
                'password': base64.b64encode(bytes(acc.password, 'utf-8')).decode('utf-8'),
                'steamlink': acc.steamlink,
                'description': acc.description,
            }
            accs = self.sam_json.read_json()
            accs.append(account)
            self.sam_json.write_to_json(accs)
            return True

    def delete_acc(self, key):
        accs = self.sam_json.read_json()
        accs.remove(self.find_acc(key))
        self.sam_json.write_to_json(accs)

    def find_acc(self, data):
        login = data[data.index('(')+1: -1]
        accs = self.sam_json.read_json()
        for acc in accs:
            if login in acc.values():
                return acc
        return False
