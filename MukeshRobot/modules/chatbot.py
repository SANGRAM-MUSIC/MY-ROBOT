import html
import json
import re
from time import sleep

import requests
from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
    User,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html

import MukeshRobot.modules.sql.chatbot_sql as sql
from MukeshRobot import BOT_ID, BOT_NAME, BOT_USERNAME, dispatcher
from MukeshRobot.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from MukeshRobot.modules.log_channel import gloggable


@
__help__ = f"""
*{BOT_NAME} ʜᴀs ᴀɴ ᴄʜᴀᴛʙᴏᴛ ᴡʜɪᴄʜ  ᴘʀᴏᴠɪᴅᴇs ʏᴏᴜ ᴀ sᴇᴇᴍɪɴɢʟᴇss ᴄʜᴀᴛᴛɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ :*

 »  /ᴄʜᴀᴛʙᴏᴛ *:* sʜᴏᴡs ᴄʜᴀᴛʙᴏᴛ ᴄᴏɴᴛʀᴏʟ ᴘᴀɴᴇʟ

☆............𝙱𝚈 » [νιρ вσყ](https://t.me/the_vip_boy)............☆
"""

__mod_name__ = "♨️Cʜᴀᴛʙᴏᴛ♨️"


