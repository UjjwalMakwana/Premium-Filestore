import pymongo
from configs import DATABASE_URL

mongo_client = pymongo.MongoClient(DATABASE_URL)
fdb = mongo_client['files']
col = fdb['data']

async def save_media(strng, url):
    col.insert_one({"string": strng, "url": url})

async def get_file(strng):
    result = col.find_one({"string": strng})
    return result.get('url') if result else ''
