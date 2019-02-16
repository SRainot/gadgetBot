# -*- coding: utf-8 -*-
# Author:w k

from aiohttp import ClientSession
import json


class Aiorequests(object):
    '''
    把aiohttp 常用2个方法放一起方便调用
    '''
    @staticmethod
    async def get(url, params=None, headers=None, **kwargs):
        async with ClientSession(headers=headers) as session:
            async with session.get(url, params=params, **kwargs) as response:
                try:
                    return json.loads(await response.text())
                except:
                    return await response.text()

    @staticmethod
    async def post(url, data=None, json=None, headers=None, **kwargs):
        async with ClientSession(headers=headers) as session:
            async with session.post(url, data=data, json=json, **kwargs) as response:
                try:
                    return json.loads(await response.text())
                except:
                    return await response.text()




