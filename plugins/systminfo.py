import subprocess
import time
import os
import requests
import speedtest
import json
import sys
import traceback
import psutil
import platform
import pyrogram

from pyrogram import __version__ as z
from datetime import datetime
from platform import python_version, uname
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, 
from telegram import Update, Bot, Message, Chat, ParseMode
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User


from telegram.error import BadRequest, Unauthorized


@Client.on_message(filters.command("sysinfo"))
async def status(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    query = update.callback_query

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

    
