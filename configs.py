import os
from pyrogram import Client
bot = Client.get_me()
username = bot.username
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME", f"{username}")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001702190728"))
BOT_OWNER = int(os.environ.get("BOT_OWNER", "6532169397"))
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001901246736"))


START_TEXT = '''<b>
Hᴇʟʟᴏ {}, Iᴍ Pʀɪᴍɪᴜᴍ Fɪʟᴇsᴛᴏʀᴇ Bᴏᴛ!.
I ᴄᴀɴ sᴛᴏʀᴇ Mᴇᴅɪᴀ ғɪʟᴇs ᴀɴᴅ Gɪᴠᴇ ʏᴏᴜ Sʜᴀʀᴇᴀʙʟᴇ Lɪɴᴋ.
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.
</b>
'''


HELP_TEXT = '''<b>
⚝ Hᴏᴡ ᴛᴏ ᴜsᴇ [ᴍᴇ]({}) ⚝,

⍟ Sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴍᴇᴅɪᴀ ғɪʟᴇ ɪ ᴡɪʟʟ sᴇɴᴅ ʏᴏᴜ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ᴛʜᴀᴛ ғɪʟᴇ.

⍟ Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ɪᴛ ᴡɪᴛʜ ʏᴏᴜʀ ғʀɪᴇɴᴅs ᴏʀ sᴜʙsᴄʀɪʙᴇʀs ᴡʜᴇɴ ᴛʜᴇʏ sᴛᴀʀᴛ ᴍᴇ ᴜsɪɴɢ ᴛʜᴀᴛ ʟɪɴᴋ ɪ ᴡɪʟʟ sᴇɴᴅ ᴀ sᴛᴏʀᴇᴅ ᴍᴇᴅɪᴀ ғɪʟᴇ(s).

⍟ Tᴏ ᴀᴠᴏɪᴅ Cᴏᴘʏʀɪɢʜᴛ ᴍᴇᴅɪᴀ ғɪʟᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴛɪᴍᴇ ᴜsᴇʀs ᴄᴀɴ ғᴏʀᴡᴀʀᴅ ɪᴛ ᴛᴏ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ᴏʀ ᴀɴʏᴡʜᴇʀᴇ.

‼️ Nᴏᴛᴇ :-
   Dᴏɴᴛ ᴜsᴇ ʙᴏᴛ ᴛᴏ sʜᴀʀᴇ NSFW ᴏʀ PʀᴇDVD, Cᴀᴍʀɪᴩ ᴄᴏɴᴛᴇɴᴛs.

• Fᴏʀ ᴀɴʏ ǫᴜᴇʀʏs ᴊᴏɪɴ :- <a href="https://t.me/NG_Continent">Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ</a>
</b>
'''

ABOUT_TEXT = '''
<b>
╔════❰ NG FɪʟᴇSᴛᴏʀᴇ Bᴏᴛ ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ MʜOᴡɴᴇʀ -> @V_Ujjwal
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> <a href="tg://resolve?domain=NG_BotS">••NG Bᴏᴛs••</a>
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> <a href="tg://resolve?domain=NG_Continent">NG Bᴏᴛs Sᴜᴩᴩᴏʀᴛ</a>
║ ┣ 
║ ┗━━━━━━━━━❥
╚═════❰ @NG_BotS ❱═════❍
</b>

'''
