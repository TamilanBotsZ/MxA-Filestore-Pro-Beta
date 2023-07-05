from bot import mxabot
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

from plugins.forcesub import FSUB_CHANNEL

@mxabot.on_callback_query(filters.regex('^delete$'))
async def delete_button(bot: Client, query: CallbackQuery):
    await query.message.delete(True)
    return

@mxabot.on_callback_query(filters.regex('^rfrsh$'))
async def rfrsh_button(bot: Client, query: CallbackQuery):
    if UserNotParticipant:
        await query.answer("Please join the channel first, then click the button", show_alert=True)
        return

    await query.answer(url="https://t.me/NG_FilestoreBot?start=start")
