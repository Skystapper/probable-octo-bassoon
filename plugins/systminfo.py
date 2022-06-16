import subprocess
import time
import os
import requests

import json
import sys
import traceback
import psutil
import platform
import pyrogram

from pyrogram import __version__ as z
from datetime import datetime
from platform import python_version, uname
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram import Client




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



@Client.on_message(filters.command("sysinfo"))
async def status(client, message):
    cmd = message.command
    msg = "*Bot information*\n"
    msg += f"Pyrogram Version: `{z}`\n"
    msg += f"Python: `{python_version()}`\n"
    uptime = get_readable_time((time.time() - StartTime))
    msg += f"Uptime: `{uptime}`\n\n"
    uname = platform.uname()
    msg += "*System information*\n"
    msg += f"OS: `{uname.system}`\n"
    msg += f"Version: `{uname.version}`\n"
    msg += f"Release: `{uname.release}`\n"
    msg += f"Processor: `{uname.processor}`\n"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    msg += f"Boot time: `{bt.day}/{bt.month}/{bt.year} - {bt.hour}:{bt.minute}:{bt.second}`\n"
    msg += f"CPU cores: `{psutil.cpu_count(logical=False)} physical, {psutil.cpu_count()} logical`\n"
    msg += f"CPU freq: `{psutil.cpu_freq().current:.2f}Mhz`\n"
    msg += f"CPU usage: `{psutil.cpu_percent()}%`\n"
    ram = psutil.virtual_memory()
    msg += f"RAM: `{get_size(ram.total)} - {get_size(ram.used)} used ({ram.percent}%)`\n"
    disk = psutil.disk_usage('/')
    msg += f"Disk usage: `{get_size(disk.total)} total - {get_size(disk.used)} used ({disk.percent}%)`\n"
    swap = psutil.swap_memory()
    msg += f"SWAP: `{get_size(swap.total)} - {get_size(swap.used)} used ({swap.percent}%)`\n"

    
