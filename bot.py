from pyrogram import Client, filters
import os
from os import getenv
from MxA.bot.plugins import commands

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

mxabot = Client('Mxa_Movies_Bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

mxabot.add_handler(commands.handler)

if __name__ == "__main__":
  mxabot.run()

