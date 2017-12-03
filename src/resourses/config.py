# coding=utf-8
from PyQt5 import QtCore

JSON_PATH = 'accounts.json'

TIMEOUT_TIME = 60

PROCESS_NAME = 'Steam.exe'

DEFAULT_STEAM_PATH = 'C:\Program Files (x86)\Steam\Steam.exe'

STEAM_DEFAUL_AVATAR_URL = 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/fe' \
                          '/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_full.jpg'

LISTVIEW_ITEM_ICON_SIZE = QtCore.QSize(32, 32)

LISTVIEW_SPACING = 3

AVATAR_SIZE = (64, 64)

IMAGE_PATH = 'avatars/{}.jpg'

STEAM_API_KEY = '9AC22DCF0B280FF82FF45BAF9CA70CD3'

STEAM_API_GET_STEAMID = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=' + STEAM_API_KEY + '&vanityurl={}'

STEAM_API_GET_SUMMARIES = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + STEAM_API_KEY + '&steamids={}'