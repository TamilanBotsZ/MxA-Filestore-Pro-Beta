import os
from os import getenv
import logging
import logging.config
import asyncio
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

class mxabot(Client):
    def __init__(self):
        super().__init__(
            "NG_FileStoreBot",
            bot_token=BOT_TOKEN,
            api_id=API_ID,
            api_hash=API_HASH,
            workers=300,
            plugins={"root": "plugins"},
            sleep_threshold=10
        )
    
    def start(self):
        super().start()
        print("Bot started. Listening for commands...")

    def run():
        bot = mxabot()
        bot.start()


if __name__ == "__main__":
    app = mxabot()
    app.run()
