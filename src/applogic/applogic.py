import os
import psutil
import time
import subprocess
import configparser
import base64

from models.account_model import SAMAccountModel

PROCESS_NAME = 'Steam.exe'
DEFAULT_STEAM_PATH = 'C:\Program Files (x86)\Steam\Steam.exe'


class AppLogic:
    def __init__(self):
        pass

    # Находим процесс steam'а
    def get_process(self):
        for proc in psutil.process_iter():
            if proc.name() == PROCESS_NAME:
                steam_proc = (proc.pid, proc.exe())
                return steam_proc

    # Убиваем процесс steam'а
    def kill_process(self, pid):
        os.kill(pid, -1)

    # Запускаем новый процесс steam'а с параметрами логина
    def start_process(self, login, passwrd):
        p = subprocess.Popen(self.get_steam_path() + ' ' + '-login' +
                             ' ' + login + ' ' + passwrd)

    def check_cfg(self):
        if not os.path.exists('settings.cfg'):
            open('settings.cfg', 'w', encoding='utf-8')
            self.set_steam_path(DEFAULT_STEAM_PATH)

    def get_steam_path(self):
        self.check_cfg()
        cfg = configparser.ConfigParser()
        cfg.read('settings.cfg')
        return cfg['PATH']['steam_path']

    def set_steam_path(self, steam_path):
        cfg = configparser.RawConfigParser()
        cfg.add_section('PATH')
        cfg.set('PATH', 'steam_path', steam_path)
        with open('settings.cfg', 'w', encoding='utf-8') as config:
            cfg.write(config)

    def login(self, key):
        account_model = SAMAccountModel()
        account = account_model.find_acc(key)
        process = self.get_process()
        if process is not None:
            process_pid = process[0]
            self.kill_process(process_pid)
            time.sleep(1)
        self.start_process(account['login'], base64.b64decode(account['password']).decode('utf-8'))
