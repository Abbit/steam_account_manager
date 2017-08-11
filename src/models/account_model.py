import base64
import json
import os

import requests
from PIL import Image

from resourses import settings
from utility.parsingthread import ParsingThread


class SAMAccountModel(object):
    def __init__(self, login=None, password=None, steamlink=None, description=None):
        self._login = login
        self._password = password

        if steamlink is "":
            self._steamlink = None
        else:
            self._steamlink = steamlink

        if description is "":
            self._description = None
        else:
            self._description = description

        self._nickname = None

        if self.steamlink is not None:
            parsingthread = ParsingThread(self)
            parsingthread.start()
            parsingthread.join()
        else:
            self.get_default_avatar()

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def steamlink(self):
        return self._steamlink

    @property
    def nickname(self):
        if self._nickname is not None:
            return self._nickname
        else:
            return self._login

    @property
    def description(self):
        return self._description

    @login.setter
    def login(self, value):
        self._login = value

    @password.setter
    def password(self, value):
        self._password = base64.b64encode(bytes(value, 'utf-8')).decode('utf-8')

    @steamlink.setter
    def steamlink(self, value):
        self._steamlink = value

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

    @description.setter
    def description(self, value):
        self._description = value

    def check_json(self):
        if not os.path.exists(settings.JSON_PATH):
            open(settings.JSON_PATH, 'w', encoding='utf-8')

    def check_avatars_dir(self):
        if not os.path.exists('avatars/'):
            os.mkdir('avatars')

    def read_accs(self):
        self.check_json()
        with open(settings.JSON_PATH, 'r', encoding='utf-8') as accs_j:
            try:
                accs = json.load(accs_j)
            except Exception:
                accs = []
        return accs

    def take_accs(self):
        accs = self.read_accs()
        sam_accounts = []
        for acc in accs:
            login = acc['login']
            password = base64.b64decode(acc['password']).decode('utf-8')
            steamlink = acc['steamlink']
            description = acc['description']
            sam_account = SAMAccountModel(login=login,
                                          password=password,
                                          steamlink=steamlink,
                                          description=description)
            sam_accounts.append(sam_account)
        return sam_accounts

    def take_acc(self, key):
        acc = self.find_acc(key)
        login = acc['login']
        password = base64.b64decode(acc['password']).decode('utf-8')
        steamlink = acc['steamlink']
        description = acc['description']
        sam_acc = SAMAccountModel(login=login,
                                  password=password,
                                  steamlink=steamlink,
                                  description=description)
        return sam_acc

    def add_acc(self):
        if self.login is None or self.password is None:
            return False
        else:
            account = {
                'login': self.login,
                'password': base64.b64encode(bytes(self.password, 'utf-8')).decode('utf-8'),
                'steamlink': self.steamlink,
                'nickname': self._nickname,  # для того чтобы в json не записываля логин 2 раза если ник отсутствует
                'description': self.description
            }
            self.check_json()
            accs = self.read_accs()
            accs.append(account)
            self.write_to_json(accs)
            return True

    def delete_acc(self, key):
        accs = self.read_accs()
        accs.remove(self.find_acc(key))
        self.write_to_json(accs)

    def find_acc(self, data):
        login = data[data.index('(')+1: -1]
        accs = self.read_accs()
        for acc in accs:
            if login in acc.values():
                return acc
        return False

    def write_to_json(self, data):
        with open(settings.JSON_PATH, 'w', encoding='utf-8') as accs_j:
            json.dump(data, accs_j, indent=2, ensure_ascii=False)

    def get_default_avatar(self):
        if os.path.exists('avatars/default.jpg'):
            return 'avatars/default.jpg'
        try:
            response = requests.get(settings.STEAM_DEFAUL_AVATAR_URL, timeout=settings.TIMEOUT_TIME)
        except Exception:
            return False
        imagepath = self.download_avatar(response.content, 'default')
        return imagepath

    def download_avatar(self, data, imagename):
        self.check_avatars_dir()
        imagepath = 'avatars/' + imagename + '.jpg'
        out = open(imagepath, "wb")
        out.write(data)
        out.close()
        self.resize_image(imagepath)
        return imagepath

    def resize_image(self, imagepath):
        img = Image.open(imagepath)
        width = 64
        height = 64
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_img.save(imagepath)
