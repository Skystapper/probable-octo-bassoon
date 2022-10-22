import os
import re
import shutil
import time
from asyncio import sleep
from sys import executable

import psutil
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, RPCError
from pyrogram.types import Message


from config import Config

from datetime import datetime
from platform import python_version, uname
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram import Client

from helper_funcs.display_progress import humanbytes, timeformat_sec


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def convert(speed):
    return round(int(speed) / 1048576, 2)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time



@Client.on_message(filters.command("stats"))
async def send_stats(_, message: Message):
    stats_msg = await message.reply("`Processing… ⏳`")
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(psutil.net_io_counters().bytes_sent)
    recv = humanbytes(psutil.net_io_counters().bytes_recv)
    cpu_usage = psutil.cpu_percent(interval=0.2)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    uptime = timeformat_sec(time.time() - boottime)
    total_users = await count_users()
    total_banned_users = await count_banned_users()
    if message.from_user.id == Config.BOT_OWNER:
        await stats_msg.edit(f"""
**💫 Current bot stats 💫**

**👥 Users :**
 ↳ **Users in database :** `{total_users}`
 ↳ **Total banned users :** `{total_banned_users}`

**💾 Disk usage :**
 ↳ **Total Disk Space :** `{total}`
 ↳ **Used :** `{used} - {disk_usage}%`
 ↳ **Free :** `{free}`

**🌐 Network usage :**
 ↳ **Uploaded :** `{sent}`
 ↳ **Downloaded :** `{recv}`

**🎛 Hardware usage :**
 ↳ **CPU usage :** `{cpu_usage}%`
 ↳ **RAM usage :** `{ram_usage}%`
 ↳ **Uptime :** `{uptime}`""")
    else:
        await stats_msg.edit(f"""
**💫 Current bot stats 💫**

**💾 Disk usage :**
 ↳ **Total Disk Space :** `{total}`
 ↳ **Used :** `{used} - {disk_usage}%`
 ↳ **Free :** `{free}`

**🎛 Hardware usage :**
 ↳ **CPU usage :** `{cpu_usage}%`
 ↳ **RAM usage :** `{ram_usage}%`
 ↳ **Uptime :** `{uptime}`""")


    
