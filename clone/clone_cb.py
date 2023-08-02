from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


@Client.on_callback_query()
async def cb_cl(bot: Client, query: CallbackQuery):
    cb_data = query.data
    if "delete" in cb_data:
        await query.message.delete()
