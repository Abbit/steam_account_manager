# coding=utf-8
import configparser

import os

from resourses import config


class SAMCfg:
    @classmethod
    def check_cfg(cls):
        if not os.path.exists('settings.cfg'):
            open('settings.cfg', 'w', encoding='utf-8')
            cls.set_steam_path(config.DEFAULT_STEAM_PATH)

    @classmethod
    def get_steam_path(cls):
        cls.check_cfg()
        cfg = configparser.ConfigParser()
        cfg.read('settings.cfg')
        return cfg['PATH']['steam_path']

    @staticmethod
    def set_steam_path(steam_path):
        cfg = configparser.RawConfigParser()
        cfg.add_section('PATH')
        cfg.set('PATH', 'steam_path', steam_path)
        with open('settings.cfg', 'w', encoding='utf-8') as settings:
            cfg.write(settings)
