import os 

class Config(object):
	#API_ID = int(os.environ.get("API_ID", "0"))
	#API_HASH = os.environ.get("API_HASH")
	#BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "NG_FileStoreBot")
	#DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	#BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
        LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
