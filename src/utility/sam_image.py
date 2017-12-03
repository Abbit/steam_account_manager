# coding=utf-8
import os
import requests
from PIL import Image

from resourses import config


class SAMImage:
    @classmethod
    def get_default_avatar(cls):
        if os.path.exists('avatars/default.jpg'):
            return 'avatars/default.jpg'
        try:
            response = requests.get(config.STEAM_DEFAUL_AVATAR_URL, timeout=config.TIMEOUT_TIME)
        except:
            return False
        imagepath = cls.download_avatar(response.content, 'default')
        return imagepath

    @classmethod
    def download_avatar(cls, url, imagename):
        if not os.path.exists('avatars/'):
            os.mkdir('avatars/')
        data = requests.get(url).content
        imagepath = config.IMAGE_PATH.format(imagename)
        out = open(imagepath, "wb")
        out.write(data)
        out.close()
        return imagepath
