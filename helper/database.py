import motor.motor_asyncio
from config import Config
import math, time, pytz, datetime

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.user

    def new_user(self, id):
        return dict(
            _id=int(id),                                   
        )

    async def send_log(b, u):
        me = await b.get_me()
        if Config.LOG_CHANNEL is not None:
            curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            date = curr.strftime('%d %B, %Y')
            time = curr.strftime('%I:%M:%S %p')
            await b.send_message(
            Config.LOG_CHANNEL,
            f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {u.mention}\nIᴅ: `{u.id}`\nUɴ: @{u.username}\n\nDᴀᴛᴇ: {date}\nTɪᴍᴇ: {time}\n\nBy: {me.mention}"
        )
        
    async def add_user(self, b, m):
        u = m.from_user
        if not await self.is_user_exist(u.id):
            user = self.new_user(u.id)
            await self.col.insert_one(user)            
            await self.send_log(b, u)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'_id': int(user_id)})
    
    async def set_site(self, id, base_site):
        await self.col.update_one({'_id': int(id)}, {'$set': {'base_site': base_site}})

    async def get_site(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('base_site', None)
        
    async def set_api(self, id, api_key):
        await self.col.update_one({'_id': int(id)}, {'$set': {'api_key': api_key}})

    async def get_api(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('api_key', None)

db = Database(Config.DB_URL, Config.DB_NAME)
