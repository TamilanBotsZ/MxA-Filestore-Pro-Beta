from bot import mxabot
from pyrogram import Client, filters
#from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
#from pyrogram.errors import QueryIdInvalid

START_TEXT = '''Hᴇʟʟᴏ {}, I Aᴍ MxA Pɪᴍɪᴜᴍ Fɪʟᴇsᴛᴏʀᴇ Bᴏᴛ!'''
fsub = -1001974852033
@mxabot.on_message(filters.command('start'))
async def start(client, message):
 await force_sub(client, message, fsub=fsub)
    return
 await message.delete()
 # me = self.get_me()
 await  message.reply_text(
  START_TEXT.format(message.from_user.mention),
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

@mxabot.on_callback_query(filters.regex('^delete$'))
async def delete_button(bot: Client, query: CallbackQuery):
    await query.message.delete(True)
    return
# try:
 # await query.answer()
# except QueryIdInvalid: pass



