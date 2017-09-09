import asyncio

import aiohttp
import os
from bs4 import BeautifulSoup

from resourses import config


class SteamlinkParser:
    def __init__(self, acc):
        self.account = acc
        self.client = aiohttp.ClientSession()
        self.queue = asyncio.Queue()

    async def run(self):
        tasks = [asyncio.ensure_future(self.start_parse())]
        await asyncio.wait(tasks)

        self.client.close()

    async def start_parse(self):
        html = await self.get_html(self.account.steamlink)
        self.account.nickname = await self.get_nickname(html)
        await self.get_avatar(html)

    async def get_html(self, url):
        async with self.client.get(url) as response:
            if response.status != 200:
                return False
            return await response.text()

    async def get_nickname(self, html):
        soup = BeautifulSoup(html, 'lxml')
        nickname = soup.find('span', class_='actual_persona_name').text
        return nickname

    async def get_avatar(self, html):
        if os.path.exists('avatars/{0}.jpg'.format(self.account.login)):
            return 'avatars/{0}.jpg'.format(self.account.login)
        soup = BeautifulSoup(html, 'lxml')
        imagelink = soup.find('div', class_='playerAvatarAutoSizeInner').find('img')['src']
        await self.download_avatar(imagelink)

    async def download_avatar(self, url):
        async with self.client.get(url) as response:
            imagepath = config.IMAGE_PATH.format(self.account.login)
            if response.status != 200:
                return False
            tmp = imagepath + '.chunks'
            with open(tmp, 'ab') as file:
                while True:
                    # Читаем буфер и записываем полученные данные в файл.
                    # Здесь всё синхронно.
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file.write(chunk)
            os.rename(tmp, imagepath)
        return imagepath
