from bot import mxabot
from handlers.adduser import *
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
from plugins.forcesub import force_sub

async def get_bot_info():
    async with mxabot() as bot:
        me = await bot.get_me()
        bot_name = me.first_name
        bot_id = me.id
    return bot_name, bot_id

START_TEXT = '''Hᴇʟʟᴏ {}, I Aᴍ [{}](tg://user?id={})'''

@mxabot.on_message(filters.private)
async def _(client, message):
    await add_user_in_db(client, message)
    return

@mxabot.on_message(filters.command('start'))
async def start(client, message):
    await message.delete()
    fsub = await force_sub(client, message)
    if fsub == 400:
        return
    bot_name, bot_id = await get_bot_info()
    await message.reply_text(
        START_TEXT.format(message.from_user.mention, bot_name, bot_id),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
                    InlineKeyboardButton("Close ❌", callback_data=f"delete")
                ]
            ]
        )
    )
