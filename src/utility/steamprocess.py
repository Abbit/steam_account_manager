import os
import psutil
import time
import subprocess

from models.account_model import SAMAccountModel
from resourses import config
from utility.sam_cfg import SAMCfg


class SteamProcess:
    def __init__(self):
        self.sam_cfg = SAMCfg()

    # Находим процесс steam'а
    def get_process(self):
        for proc in psutil.process_iter():
            if proc.name() == config.PROCESS_NAME:
                steam_proc = (proc.pid, proc.exe())
                return steam_proc

    # Убиваем процесс steam'а
    def kill_process(self, pid):
        os.kill(pid, -1)

    # Запускаем новый процесс steam'а с параметрами логина
    def start_process(self, login, password):
        subprocess.Popen(self.sam_cfg.get_steam_path() + ' ' + '-login' + ' ' + login + ' ' + password)

    def login(self, key):
        account_model = SAMAccountModel()
        account = account_model.take_acc(key)
        process = self.get_process()
        if process is not None:
            process_pid = process[0]
            self.kill_process(process_pid)
            time.sleep(1)
        self.start_process(account.login, account.password)
