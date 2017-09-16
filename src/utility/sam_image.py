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
    def download_avatar(cls, data, imagename):
        if not os.path.exists('avatars/'):
            os.mkdir('avatars/')
        imagepath = config.IMAGE_PATH.format(imagename)
        out = open(imagepath, "wb")
        out.write(data)
        out.close()
        cls.resize_image(imagepath)
        return imagepath

    @staticmethod
    def resize_image(imagepath):
        img = Image.open(imagepath)
        avatar_size = config.AVATAR_SIZE
        resized_img = img.resize(avatar_size, Image.ANTIALIAS)
        resized_img.save(imagepath)
