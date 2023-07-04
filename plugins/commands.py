from bot import mxabot
from pyrogram import Client, filters
from pyrogram.types import Message #,InlineKeyboardMarkup, InlineKeyboardButton




@mxabot.on_message(filters.command('start'))
def start(client, message):
  me = mxabot.get_me()
  message.reply_text("Hᴇʟʟᴏ {message.from_user.mention}, I Aᴍ {me.mention}!")
