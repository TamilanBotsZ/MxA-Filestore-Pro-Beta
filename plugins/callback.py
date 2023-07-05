from bot import mxabot
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)
from plugins.commands import start
from plugins.forcesub import FSUB_CHANNEL

@mxabot.on_callback_query(filters.regex('^delete$'))
async def delete_button(bot: Client, query: CallbackQuery):
    await query.message.delete(True)
    return

@mxabot.on_callback_query(filters.regex('^rfrsh$'))
async def rfrsh_button(bot: Client, query: CallbackQuery):
    rfrsh_msg = await query.reply("Checking Please wait...")
    if FSUB_CHANNEL:
        try:
            user = bot.get_chat_member(FSUB_CHANNEL, query.from_user.id)
            if user.status == "banned":
                await query.reply_text("Sorry you are banned 🥲")
                await rfrsh_msg.delete()
                return
        except UserNotParticipant:
            await query.reply_text(
                text="Hey bruh you have to subscribe to my updates channel to use me",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Channel", url=f"t.me/{FSUB_CHANNEL}")
                        ],
                        [
                            InlineKeyboardButton("Contact Admin", url="t.me/Ng_IB_Bot")
                        ]
                    ]
                )
            )
            return start
    await rfrsh_msg.delete()
