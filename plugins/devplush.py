from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import shutil
import requests
import os

import time
from datetime import timedelta

timestarted = timedelta(seconds=int(time.time())

@Client.on_message(filters.command('uptime'))
def uptime(client, message):
    timecheck = timedelta(seconds=int(time.time()))
    uptime = timecheck - timestarted
    app.send_message(chat_id=message.from_user.id, text=f"__**Uptime :**__ __{uptime}__",
                     parse_mode='md')
