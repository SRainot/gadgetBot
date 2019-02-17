# -*- coding: utf-8 -*-
# Author:w k


'''
基于百度语音合成所以需要获取一个toekn(会过期),所以每天请求一次。也可以请求时加上是否token过期
'''
from . import other
import nonebot as rcnb


@other.command('speak')
async def say(session: rcnb.CommandSession):
    pass
