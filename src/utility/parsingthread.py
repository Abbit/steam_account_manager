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
        html = self.get_html(self.account.steamlink)
        self.account.nickname = self.get_nickname(html)
        self.get_avatar(html)

    def get_html(self, url):
        try:
            r = requests.get(url, timeout=config.TIMEOUT_TIME)
        except Exception:
            return False
        html = r.content
        return html

    def get_nickname(self, html):
        soup = BeautifulSoup(html, 'lxml')
        nickname = soup.find('span', class_='actual_persona_name').text
        return nickname

    def get_avatar(self, html):
        if os.path.exists('avatars/{0}.jpg'.format(self.account.login)):
            return 'avatars/{0}.jpg'.format(self.account.login)
        soup = BeautifulSoup(html, 'lxml')
        imagelink = soup.find('div', class_='playerAvatarAutoSizeInner').find('img')['src']
        imagepath = self.sam_image.download_avatar(self.get_html(imagelink), self.account.login)
        return imagepath
