from pyrogram import Client, filters
from pyrogram.types import Message
import os
from os import getenv
import logging
import logging.config


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
            in_memory=True
        )

    async def start(self):
      await super().start()
      logging.info('Bot started')



    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        logging.info(f"{me.first_name} is_...  ♻️Restarting...")





if __name__ == "__main__":
  app = mxabot()
  app.run()
