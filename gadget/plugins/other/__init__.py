# -*- coding: utf-8 -*-
# Author:w k
import nonebot as nb

__plugin_name = 'other'
other = nb.CommandGroup('other', only_to_me=False)
from . import sign
from . import noop_chat