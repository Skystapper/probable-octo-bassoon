import os
import asyncio
from pyrogram import Client
from translation import Translation
from helper_funcs.xtra  import get_info
from pyrogram.errors import FloodWait
from helper_funcs.ytscrch import youtube_search
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent


if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


@Client.on_inline_query()
async def inline_search(bot, query: InlineQuery):
    me = []
    try:
        me = await Client.get_me(bot)
    except FloodWait as e:
        await asyncio.sleep(e.x)
    id = query.from_user.id
    results = []
    #
    defaults = await get_info(me.username)
    results.extend(defaults)
    #
    try:
        if Config.AUTH_USERS and (id not in Config.AUTH_USERS):
            await query.answer(results=results,
                               switch_pm_text=Translation.NOT_AUTH_TXT,
                               switch_pm_parameter="help"
                               )
            return
    except FloodWait as e:
        await asyncio.sleep(e.x)
    #
    search = query.query.strip()
    string = await youtube_search(search)
    for data in string:
        count = data['viewCount']
        thumb = data['thumbnails']
        results.append(
            InlineQueryResultArticle(
                title=data['title'][:35] + "..",
                input_message_content=InputTextMessageContent(
                    message_text=data['link']
                ),
                thumb_url=thumb[0]['url'],
                description=Translation.DESCRIPTION.format(data['duration'], count['text'])
            )
        )
    if string:
        switch_pm_text = Translation.RESULTS_TXT
        try:
            await query.answer(
                results=results,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="start"
            )
        except Exception:
            pass
    else:
        switch_pm_text = Translation.NO_RESULTS
        try:
            await query.answer(
                results=results,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="start"
            )
        except Exception:
            pass
