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
async def rfrsh_button(bot: Client, query: CallbackQuery, message: Message):
    rfrsh_msg = await message.reply_text("Checking Please wait...")
    if FSUB_CHANNEL:
        try:
            user = bot.get_chat_member(FSUB_CHANNEL, query.from_user.id)
            if user.status == "banned":
                await message.reply_text("Sorry you are banned 🥲")
                await rfrsh_msg.delete()
                return
        except UserNotParticipant:
            await query.answer(" Pls join channel then click on button", show_alert=True)
            await rfrsh_msg.delete()
            return

        await query.answer(url="https://t.me/NG_FilestoreBot?start=start")
