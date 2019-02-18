# -*- coding: utf-8 -*-
# Author:w k

'''
每次程序启动加载需要的数据。
'''
from .schedule import get_bd_token
import asyncio
from .bilibili.live_subscription import read_subscription_info



#获取百度token
asyncio.get_event_loop().run_until_complete(get_bd_token())


#加载B站直播订阅房间信息
asyncio.get_event_loop().run_until_complete(read_subscription_info())