from bot import mxabot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




@mxabot.on_message(filters.command('start'))
def start(client, message):
  
  
