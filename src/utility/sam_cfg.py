import configparser

import os

from resourses import config


class SAMCfg:
    def __init__(self):
        pass

    def check_cfg(self):
        if not os.path.exists('settings.cfg'):
            open('settings.cfg', 'w', encoding='utf-8')
            self.set_steam_path(config.DEFAULT_STEAM_PATH)

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
