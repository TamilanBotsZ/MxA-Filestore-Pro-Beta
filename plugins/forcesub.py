from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant


FSUB_CHANNEL = "NG_BotS"
async def force_sub(client, message):
    if FSUB_CHANNEL:
        try:
            user = await client.get_chat_member(FSUB_CHANNEL, message.from_user.id)
            if user.status == "kicked":
                await message.reply_text("Sorry, you are banned 🥲")
                return 400
        except UserNotParticipant:
            await message.reply_text(
                text="Hey bruh, you have to subscribe to my update channel to use me",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Channel 📣", url="t.me/NG_BotS"),
                            InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306")
                        ]
                    ]
                )
            )
            return 400
    return 200
