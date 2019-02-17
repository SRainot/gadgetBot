# -*- coding: utf-8 -*-
# Author:w k

import nonebot as rcnb
import asyncio
from gadget.untils.aiorequests import Aiorequests as requests


@rcnb.scheduler.scheduled_job('interval', days=10)
async def get_bd_token():
    # 获取百度语音合成的token
    bot = rcnb.get_bot()
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {
            'grant_type': 'client_credentials',
            'client_id': bot.config.BD_CLIENT_ID,
            'client_secret': bot.config.BD_CLIENT_SECRET,
    }
    headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
    response = await requests.post(token_url, data=data, headers=headers)
    key = response['access_token']
    if key:
        rcnb.get_bot().config.BD_TOKEN = key
    else:
        await asyncio.sleep(60)
        return await get_bd_token()


