import os
from threading import Thread

import requests
from PIL import Image
from bs4 import BeautifulSoup

from resourses import settings


class ParsingThread(Thread):
    def __init__(self, acc):
        Thread.__init__(self)
        self.account = acc

    def run(self):
        html = self.get_html(self.account.steamlink)
        self.account.nickname = self.get_nickname(html)
        self.get_avatar(html)

    def get_html(self, url):
        try:
            r = requests.get(url, timeout=settings.TIMEOUT_TIME)
        except Exception:
            return False
        html = r.content
        return html

    def get_nickname(self, html):
        soup = BeautifulSoup(html, 'lxml')
        nickname = soup.find('span', class_='actual_persona_name').text
        return nickname

    def get_avatar(self, html):
        if os.path.exists('avatars/' + self.account.login + self.account.nickname + '.jpg'):
            return 'avatars/' + self.account.login + self.account.nickname + '.jpg'
        soup = BeautifulSoup(html, 'lxml')
        imagelink = soup.find('div', class_='playerAvatarAutoSizeInner').find('img')['src']
        imagepath = self.download_avatar(self.get_html(imagelink), self.account.login + self.account.nickname)
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

    def check_avatars_dir(self):
        if not os.path.exists('avatars/'):
            os.mkdir('avatars')
