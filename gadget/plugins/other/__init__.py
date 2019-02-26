# -*- coding: utf-8 -*-
# Author:w k
import nonebot as rcnb

__plugin_name = 'other'

other = rcnb.CommandGroup('other', only_to_me=False)


from . import sign
from . import noop_chat
from . import speak
from . import crawl
from . import like