import os
import psutil
import time
import subprocess
import json
import configparser
import base64

PROCESS_NAME = "Steam.exe"
DEFAULT_STEAM_PATH = 'C:\Program Files (x86)\Steam\Steam.exe'


# Находим процесс steam'а
def get_process():
    for proc in psutil.process_iter():
        if proc.name() == PROCESS_NAME:
            steam_proc = (proc.pid, proc.exe())
            return steam_proc


# Убиваем процесс steam'а
def kill_process(pid):
    os.kill(pid, -1)


# Запускаем новый процесс steam'а с параметрами логина
def start_process(login, passwrd):
    p = subprocess.Popen(get_steam_path() + ' ' + '-login' +
                         ' ' + login + ' ' + passwrd)


def check_json():
    if not os.path.exists('accounts.json'):
        open('accounts.json', 'w', encoding='utf-8')


def check_cfg():
    if not os.path.exists('settings.cfg'):
        open('settings.cfg', 'w', encoding='utf-8')
        set_steam_path(DEFAULT_STEAM_PATH)


def read_accs():
    check_json()
    with open('accounts.json', 'r', encoding='utf-8') as accs_j:
        try:
            accs = json.load(accs_j)
        except Exception as e:
            accs = {}
    return accs


def add_acc(user_login, user_pass):
    if (user_login is None) or (user_pass is None):
        return False
    else:
        account = {user_login: {
            'login': user_login,
            'password': base64.b64encode(bytes(user_pass, 'utf-8')).decode('utf-8')
        }
        }
        check_json()
        accs = read_accs()
        accs.update(account)
        with open('accounts.json', 'w', encoding='utf-8') as accs_j:
            json.dump(accs, accs_j, indent=2, ensure_ascii=False)
            return True


def login(account):
    process = get_process()
    if process is not None:
        process_pid = process[0]
        kill_process(process_pid)
        time.sleep(1)
    start_process(account['login'], base64.b64decode(account['password']).decode('utf-8'))


def get_steam_path():
    check_cfg()
    cfg = configparser.ConfigParser()
    cfg.read('settings.cfg')
    return cfg['PATH']['steam_path']


def set_steam_path(steam_path):
    cfg = configparser.RawConfigParser()
    cfg.add_section('PATH')
    cfg.set('PATH', 'steam_path', steam_path)
    with open('settings.cfg', 'w', encoding='utf-8') as config:
        cfg.write(config)


def autoheight():
    accs = read_accs()
    return len(accs)*32+60


def delete_acc(key):
    accs = read_accs()
    del accs[key]
    with open('accounts.json', 'w', encoding='utf-8') as accs_j:
        json.dump(accs, accs_j, indent=2, ensure_ascii=False)
