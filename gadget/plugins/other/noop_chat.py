# -*- coding: utf-8 -*-
# Author:w k


from . import other
from gadget.untils.chat_txai import Chat
from nonebot import CommandSession, NLPSession, on_natural_language, IntentCommand, on_command


@on_command('chat')
async def _(session: CommandSession):
    msg = session.get_optional('msg')
    report = await Chat.request(msg)
    await session.finish(report)
    return


@on_natural_language()
async def _(session: NLPSession):
    return IntentCommand(60.0, 'chat', {'msg': session.msg_text})
