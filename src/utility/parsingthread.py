# coding=utf-8
import os
from threading import Thread

import requests
from bs4 import BeautifulSoup

from resourses import config
from utility.sam_image import SAMImage


class ParsingThread(Thread):
    def __init__(self, acc):
        Thread.__init__(self)
        self.sam_image = SAMImage()
        self.account = acc

    def run(self):
        self.account.steamid = self.get_steamid()
        summaries = self.get_steam_summaries(self.account.steamid)
        self.account.nickname = self.get_nickname(summaries)
        self.account.avatar_url = self.get_avatar(summaries)

    def get_steamid(self):
        if self.account.steamid is not None:
            return self.account.steamid
        elif self.account.steamlink.split('/')[-2] == 'profiles':
            return self.account.steamlink.split('/')[-1]
        else:
            try:
                r = requests.get(config.STEAM_API_GET_STEAMID.format(self.account.steamlink.split('/')[-1]), timeout=config.TIMEOUT_TIME)
            except:
                return None
            response = r.json()
            if response['response']['success'] == 1:
                return response['response']['steamid']
            else:
                return None

    def get_steam_summaries(self, steamid):
        try:
            r = requests.get(config.STEAM_API_GET_SUMMARIES.format(steamid), timeout=config.TIMEOUT_TIME)
        except:
            return False
        response = r.json()
        return response['response']['players'][0]

    def get_nickname(self, summaries):
        return summaries['personaname']

    def get_avatar(self, summaries):
        if summaries['avatarmedium'] != self.account.avatar_url:
            imagepath = self.sam_image.download_avatar(summaries['avatarmedium'], self.account.login)
        return summaries['avatarmedium']
