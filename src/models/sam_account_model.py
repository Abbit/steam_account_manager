class SAMAccountModel(object):
    def __init__(self, login, password, nickname=None, steamlink=None, description=None):
        self._login = login
        self._password = password
        self._steamlink = steamlink
        self._nickname = nickname
        self._description = description

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
        self._password = value

    @steamlink.setter
    def steamlink(self, value):
        self._steamlink = value

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

    @description.setter
    def description(self, value):
        self._description = value
