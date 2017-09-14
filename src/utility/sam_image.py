import os
import requests
from PIL import Image

from resourses import config


class SAMImage:
    def __init__(self):
        pass

    def get_default_avatar(self):
        if os.path.exists('avatars/default.jpg'):
            return 'avatars/default.jpg'
        try:
            response = requests.get(config.STEAM_DEFAUL_AVATAR_URL, timeout=config.TIMEOUT_TIME)
        except Exception:
            return False
        imagepath = self.download_avatar(response.content, 'default')
        return imagepath

    def download_avatar(self, data, imagename):
        if not os.path.exists('avatars/'):
            os.mkdir('avatars/')
        imagepath = config.IMAGE_PATH.format(imagename)
        out = open(imagepath, "wb")
        out.write(data)
        out.close()
        self.resize_image(imagepath)
        return imagepath

    def resize_image(self, imagepath):
        img = Image.open(imagepath)
        avatar_size = config.AVATAR_SIZE
        resized_img = img.resize(avatar_size, Image.ANTIALIAS)
        resized_img.save(imagepath)
