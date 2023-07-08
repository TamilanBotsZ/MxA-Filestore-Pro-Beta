import datetime
import motor.motor_asyncio
from configs import Config


class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[ngfilestorebot]
        self.col = self.db.users


    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat()
        )
         #   ban_status=dict(
     #           is_banned=False,
      #          ban_duration=0,
       #         banned_on=datetime.date.max.isoformat(),
        #        ban_reason='',
         #       api=None,
          #      shortner=None,
             #   fsub=None
          #  )
       # )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_user


db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
