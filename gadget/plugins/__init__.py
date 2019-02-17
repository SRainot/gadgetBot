# -*- coding: utf-8 -*-
# Author:w k
from .schedule import get_bd_token
import asyncio


asyncio.get_event_loop().run_until_complete(get_bd_token())