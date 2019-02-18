# -*- coding: utf-8 -*-
# Author:w k

from nonebot.default_config import *
from os import path

COMMAND_START = {''}
DEBUG = True
SUPERUSERS = {}
NICKNAME = {'!', '花'}

# 数据存储文件
DATA_FOLDER = path.join(path.dirname(__file__), 'data')

# B站订阅的列表
BILIBILI_SUBSCRIPTION_INFO = []

# B站直播订阅时间（防止过快封IP,需要自己看着设置吧 0 0）
CHECK_OPEN_STATUS = 10  # 单位是秒
CHECK_CLOSE_STATUS = 10  # 单位是分钟

###CHAT SETTING
TX_CHAT_APPID = '2111616354'
TX_CHAT_APPKEY = 'wSLUnOTGuAkln8pv'
###


###BD SPEAK
BD_CLIENT_ID = '4LI50CEmqn4h4mNqfjwicu04'
BD_CLIENT_SECRET = 'PHBGwYHmWiz9Ce0eBV7jygGrUyKpSetn'
BD_TOKEN = ''
###
