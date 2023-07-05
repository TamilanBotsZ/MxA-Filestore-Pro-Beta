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

@mxabot.on_message(filters.command('start'))
def start(client, message):
 message.delete()
 # me = self.get_me()
 message.reply_text(
  START_TEXT.format(cmd.from_user.mention),
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
    await query.message.delete(true)
    return
# try:
 # await query.answer()
# except QueryIdInvalid: pass



