from bot import mxabot
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




@mxabot.on_message(filters.command('start'))
def start(bot: Client, message: Message):
  me = bot.get_me()
  message.reply_text("Hᴇʟʟᴏ {message.from_user.mention}, I Aᴍ {me.mention}!")
