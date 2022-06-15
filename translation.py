class Translation(object):
    START_TEXT = """Hi 🖖 {},
I'm X-URL-Uploader!
You can upload HTTP/HTTPS direct link, Using this bot!

/help for more details!"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "⤵️⬇️Now Downloading..⇊⇊"
    UPLOAD_START = "⤴️⬆️Now Uploading..⇮⇮"
    RCHD_TG_API_LIMIT = "➠Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "➠Thanks for using @URLX_bot)"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "➥Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@HEXAX_bot"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "➥ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """➥How to Use Me? Follow These steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

If bot didn't respond, contact @shado_hackers"""

    ABOUT = """
**About This Bot** 
Bot created by @shado_hacker
My name is 📨:@URLX_bot
Hosted🗃️ : Heroku
Leech 🌡️: [@nexleech]
Language ✨: Python
Support⚡:  [@OMG INFO]
Developer👨‍💻 : @shado_hackers
Create on🗓️ : 10/06/2022 """
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "➥Reply /genthumbnail to a media album, to generate custom thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NOT_AUTH_TXT = "<b>Error : </b>\n\n<code>You are not Authorized to use this bot.</code>"
    RESULTS_TXT = "👀 Results:"
    NO_RESULTS = "❌ No Results"
    DESCRIPTION = "Duration: {} || {}"
    DEFAULT_TITLE = "create by Lusifer"
    DEFAULT_LINK = "https://t.me/shado_hackers"
    DEFAULT_THUMB_URL = "https://telegra.ph/file/3f4ed58e53927dbf5b2a8.jpg"
    DEFAULT_DESCRIPTION = "Link: lusifer | Telegram"
    DEV_TITLE = "support information"
    DEV_THUMB_URL = "https://telegra.ph/file/a7823975c07961870cc45.jpg"
    DEV_LINK = "https://t.me/OMG_info"
    DEV_DESCRIPTION = "Name: OMG INFO | Telegram"
    SHARE_BUTTON_TEXT = "Hi.. 👋\nCheckout : @{username}\nFor search and download TouTube Videos"
