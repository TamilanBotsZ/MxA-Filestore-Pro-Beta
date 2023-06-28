from bot import mxabot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




@mxabot.on_message(filters.command('start'))
def start(bot: Client, message: Message):
  me = client.get_me()
  await message.reply_text("Hᴇʟʟᴏ {message.from_user.mention}, I Aᴍ {me.mention}!\n\n"I Cᴀɴ Sᴛᴏʀᴇ Mᴇᴅɪᴀ Aɴᴅ Gɪᴠᴇ Yᴏᴜ A Lɪɴᴋ Wʜɪᴄʜ Cᴀɴ Usᴇ Tᴏ Gᴇᴛ Sᴛᴏʀᴇᴅ Mᴇᴅɪᴀ")
