from pyrogram import Client, filters
from pyrogram.types import Message
import os
from os import getenv
import logging
import logging.config
#from MxA.bot.plugins import commands

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

class mxabot(Client):

    def __init__(self):
        super().__init__(
            "Mxa_Movies_Bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=300,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )
#Client('Mxa_Movies_Bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="plugins"))

#@mxabot.on_message(filters.private)
#async def hello(client, message):
  #  await message.reply("Hello {message.from_user.mention}!!")


#@mxabot.on_message(filters.command('start'))
#def start(client, message):
#  me = client.get_me()
#  message.reply_text("Hᴇʟʟᴏ {message.from_user.mention}, I Aᴍ {me.mention}!")
  
#mxabot.add_handler(commands.handler)
    async def start(self):
      await super().start()
      logging.info('Bot started')



    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        logging.info(f"{me.first_name} is_...  ♻️Restarting...")





if __name__ == "__main__":
  app = mxabot
  app.run()
