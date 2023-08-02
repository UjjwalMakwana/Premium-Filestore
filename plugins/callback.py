from configs import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram.errors import UserNotParticipant, QueryIdInvalid
from .forcesub import FSUB_CHANNEL
from bot import Filestore


@Filestore.on_callback_query()
async def callback(bot: Client, query: CallbackQuery):
    me = await bot.get_me()
    cb_data = query.data

    if cb_data == "delete":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

    elif cb_data == "help":
        await query.message.edit(
            HELP_TEXT.format(me.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                        InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")
                    ],
                    [
                        InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/NG_Continent")
                    ],
                    [
                        InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
                        InlineKeyboardButton("Close ❌", callback_data="delete")
                    ],
                    [
                        InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
                ]
                ]
            )
        )
    elif cb_data == "about":
        await query.message.edit(
            ABOUT_TEXT.format(me.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Hᴇʟᴩ", callback_data="help"),
                        InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")
                    ],
                    [
                        InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/NG_Continent")
                    ],
                    [
                        InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
                        InlineKeyboardButton("Close ❌", callback_data="delete")
                    ],
                    [
                        InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
                    ]
                ]
            )
        )
    elif cb_data == "earn_money":
        await query.message.edit(
            text="send /set_shortner & /set_api to know more",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Hᴇʟᴩ", callback_data="help"),
                        InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
                    ],
                    [
                        InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/NG_Continent")
                    ],
                    [
                        InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
                        InlineKeyboardButton("Close ❌", callback_data="delete")
                    ],
                    [
                        InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
                    ]
                ]
            )
        )

    elif cb_data == "start":
        await query.message.edit(
            START_TEXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                         InlineKeyboardButton("Hᴇʟᴩ & Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ", callback_data="help")
                    ],
                    [
                         InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url=f"https://t.me/NG_BotS"),
                         InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url=f"https://t.me/NG_Continent")
                    ],
                    [
                         InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")
                    ],
                    [
                         InlineKeyboardButton("Dᴇᴠʟᴏᴩᴇʀ 👨‍💻", user_id="6112935306"),
                         InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")
                    ]
                ]
            )
        )
            

    elif "del+" in cb_data:
        await query.answer()
        msg_id = query.data.split("+")[1]
        chat_id = int(DB_CHANNEL)
        message = await bot.get_messages(chat_id, int(msg_id))
        await message.delete()
        await query.message.edit("Deleted files successfully from the database 👨‍✈️")

    elif cb_data == "rfrsh":
        if FSUB_CHANNEL:
            try:
                user = await bot.get_chat_member(FSUB_CHANNEL, query.message.chat.id)
                if user.status == "banned":
                    await query.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/Ng_SupportS).",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await query.message.edit(
                    text="**I like Your Smartness But Don't Be Oversmart! 😑**\n\n",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("😇 Join Channel 😇", url=f"https://t.me/{FSUB_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh 🔄", callback_data="rfrsh")
                            ]
                        ]
                    )
                )
                return

            await query.message.edit(
                START_TEXT.format(query.from_user.mention),
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

    if cb_data.startswith("get_file_"):
        result = cb_data.split("_file_")[1]
        await query.answer(url=f"{result}")
    
