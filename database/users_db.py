import motor.motor_asyncio
import datetime
from configs import *

class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
    
    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            shortner=None,
            api=None,
            fsub=None
        )

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
        return all_users

    async def set_shortner(self, user_id, shortner):
        await self.col.update_one({'id': int(user_id)}, {'$set': {'shortner': shortner}})

    async def get_shortner(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return user.get('shortner', None)

    async def set_api(self, user_id, api):
        await self.col.update_one({'id': user_id}, {'$set': {'api': api}})

    async def get_api(self, user_id):
        user = await self.col.find_one({'id': user_id})
        return user.get('api', None)

    async def set_fsub(self, user_id, fsub):
        await self.col.update_one({'id': user_id}, {'$set': {'fsub': fsub}})

    async def get_fsub(self, user_id):
        user = await self.col.find_one({'id': user_id})
        return user.get('fsub', None)


udb = Database(DATABASE_URL, BOT_USERNAME)
