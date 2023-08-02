from configs import *
from database import udb as db
from pyrogram import Client
from pyrogram.types import Message
from plugins.forcesub import force_sub

async def adduser(bot: Client, message: Message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        if LOG_CHANNEL:
            await bot.send_message(
                LOG_CHANNEL,
                f"#new_user :-\n\n{message.from_user.mention} started @{BOT_USERNAME}!"
            )

async def handle_private_message(client: Client, message: Message):
    await adduser(client, message)
    fsub = await force_sub(client, message)
    if fsub == 400:
        return
