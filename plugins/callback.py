from bot import mxabot
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from plugins.commands import start
from plugins.commands import FSUB_CHANNEL

@mxabot.on_callback_query(filters.regex('^delete$'))
async def delete_button(bot: Client, query: CallbackQuery):
    await query.message.delete(True)
    return


@mxabot.on_callback_query(filters.regex('^rfrsh$'))
async def delete_button(bot: Client, query: CallbackQuery):
        rfrsh_msg = query.reply("Checking Please wait...")
    if FSUB_CHANNEL:
        try:
            user = client.get_chat_member(FSUB_CHANNEL, message.from_user.id)
            if user.status == "banned":
                cmd.reply_text("Sorry you are banned 🥲")
                return
        except UserNotParticipant:
            cmd.reply_text(
                text="Hey bruh you have to subscribe my updates channel to use me",
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
