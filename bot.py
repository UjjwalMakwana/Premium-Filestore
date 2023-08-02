import os
import logging
import logging.config
import asyncio
import pyrogram

logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyromod import listen
from pyrogram import Client, idle, __version__ as pv
#from plugins.clone_cmd import *
from configs import *

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("mb")

class Filestore(Client):
    def main():
        plugins = dict(root="plugins")
        mb = Client(
            "Filestore",
            bot_token=BOT_TOKEN,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=plugins,
            workers=500,
            in_memory=True
        )
        
        with mb:
            me = mb.get_me()
            bn = me.first_name

        mb.start()
        print(f"{bn} with latest version({pv}) Started successfully..😎🤏")
        idle()

if __name__ == "__main__":
    Filestore.main()
