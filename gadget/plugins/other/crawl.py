# -*- coding: utf-8 -*-
# Author:w k


from gadget.aio import requests
import nonebot as rcnb
import asyncio

rcnbot = rcnb.get_bot()
MSG_LIST = list()


@rcnb.on_natural_language('爬取', only_to_me=False, only_short_message=False)
async def _(session: rcnb.NLPSession):
    if session.msg_text.startswith('爬取'):
        t = session.msg_text[2:4]
        if t == 'ht':
            t = None
        url = session.msg_text[2:] if not t else session.msg_text[4:]
        asyncio.get_event_loop().run_in_executor(None, run_more, url, session.ctx, t)
        await session.send('唔~我去看看')
        return


def run_more(url, ctx, t):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    ret = loop.run_until_complete(get_crawl(url, t))
    if not ret:
        ctx['message'] = '完球了。没获取到'
        MSG_LIST.append(ctx)
        return
    msg = ''
    for info in ret:
        for k, v in info.items():
            msg += f'{k}:{v}\n'
    count = len(msg)
    start = 0
    end = 1500
    while count > 1500:
        ctx['message'] = msg[start:end]
        MSG_LIST.append(ctx.copy())
        count = len(msg[end:])
        if count < 1500:
            ctx['message'] = msg[end:]
            MSG_LIST.append(ctx.copy())
            break
        start = end
        end = end * 2


async def get_crawl(url, t):
    if not url:
        return None
    api_url = 'https://api.diffbot.com/v3/analyze'
    if t == '视频':
        api_url = 'https://api.diffbot.com/v3/video'
    elif t == '图片':
        api_url = 'https://api.diffbot.com/v3/image'
    elif t == '文章':
        api_url = 'https://api.diffbot.com/v3/article'
    elif t == '商品':
        api_url = 'https://api.diffbot.com/v3/product'

    params = {
        'token': rcnbot.config.DIFFBOT_TOKEN,
        'url': url,
    }
    result = await requests.get(api_url, params=params)
    result = await result.json()
    if result:
        ret = result.get('objects', None)
        return ret


@rcnb.scheduler.scheduled_job('interval', seconds=2)
async def _():
    # 因为在线程里不知道为啥。。会发消息慢，。只能通过简单得来实现发消息（（
    for i in range(len(MSG_LIST)):
        ctx = MSG_LIST.pop(0)
        await rcnbot.send_msg(**ctx)
