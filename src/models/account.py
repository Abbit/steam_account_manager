import base64

from utility.parsingthread import ParsingThread


class Account(object):
    def __init__(self, login, password, steamlink, description):
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

        if steamlink is not None:
            self.parse_steamlink()

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
    def description(self):
        return self._description

    @property
    def nickname(self):
        if self._nickname is not None:
            return self._nickname
        else:
            return self._login

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

    def parse_steamlink(self):
        parsing_thread = ParsingThread(self)
        parsing_thread.start()
        parsing_thread.join()
