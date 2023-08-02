from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import PeerIdInvalid

START_TEXT = '''Hᴇʟʟᴏ {}, I Aᴍ {} Cʟᴏɴᴇᴅ Fɪʟᴇsᴛᴏʀᴇ Bᴏᴛ!\n\nMade Using @NG_FileStoreBot'''

@Client.on_message(filters.command('start'))
async def cl_start(client: Client, message: Message):
  try:
    bot = await client.get_me()
    await message.reply_text(
      START_TEXT.format(message.from_user.mention, bot.mention),
      disable_web_page_preview=True,
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
            InlineKeyboardButton("Close ❌", callback_data="delete")
          ]
        ]
      )
    ) 
  except PeerIdInvalid:
    pass
  
