import math
import time
from typing import List, Union



def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (((str(days) + "d, ") if days else "") +
           ((str(hours) + "h, ") if hours else "") +
           ((str(minutes) + "m, ") if minutes else "") +
           ((str(seconds) + "s, ") if seconds else "") +
           ((str(milliseconds) + "ms, ") if milliseconds else ""))
    return tmp[:-2]


def timeformat_sec(seconds: int) -> str:
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (((str(days) + "d, ") if days else "") +
           ((str(hours) + "h, ") if hours else "") +
           ((str(minutes) + "m, ") if minutes else "") +
           ((str(seconds) + "s, ") if seconds else ""))
    return tmp[:-2]
