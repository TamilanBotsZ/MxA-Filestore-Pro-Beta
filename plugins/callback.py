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
    if FSUB_CHANNEL:
        try:
            user = await bot.get_chat_member(FSUB_CHANNEL.id, query.message.chat.id)
            if user.status == "banned":
                await query.message.edit(
                    text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/TeleRoid14).",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await query.message.edit(
                text="**I like Your Smartness But Don't Be Oversmart! 😑**\n\n",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("😇 Join Channel 😇", url=f"https://t.me/{FSUB_CHANNEL}")
                        ],
                        [
                            InlineKeyboardButton("🔄 Refresh 🔄", callback_data="rfrsh")
                        ]
                    ]
                )
            )
            return
        except Exception:
            await query.message.edit(
                text="Something went Wrong. Contact my [Support](https://t.me/NG_ib_bot).",
                disable_web_page_preview=True
            )
            return

    await message.delete()
    await query.reply.message.edit(
        START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
                    InlineKeyboardButton("Close ❌", callback_data="delete")
                ]
            ]
        )
    )
