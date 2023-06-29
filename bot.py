from pyrogram import Client, filters
from pyrogram.types import Message
import os
from os import getenv
#from MxA.bot.plugins import commands

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

mxabot = Client('Mxa_Movies_Bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@mxabot.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello {message.from_user.mention!!")


@mxabot.on_message(filters.command('start'))
def start(client, message):
  me = client.get_me()
  message.reply_text("Hᴇʟʟᴏ {message.from_user.mention}, I Aᴍ {me.mention}!")
  
#mxabot.add_handler(commands.handler)

if __name__ == "__main__":
  mxabot.run()

