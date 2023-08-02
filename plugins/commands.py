import os
from .welcome import send_welcome_message
import requests
import asyncio
from handlers import *
import urllib
from urllib.parse import quote
from pyrogram import Client, filters
from database import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from .forcesub import force_sub
from configs import *
from bot import Filestore


@Client.on_message(filters.command('start'))
async def start(client, message):
    await handle_private_message(client, message)

    text = message.text
    cmd = text.split("_", 1)[-1]

    if cmd == "/start":
        try:
            final_image_path, stkr, stm = await send_welcome_message(client, message)
            await stm.edit("Generated, Now Sending...")
            await asyncio.gather(
                message.reply_photo(
                    #chat_id=message.chat.id,
                    photo=final_image_path,
                    caption=START_TEXT.format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Hᴇʟᴩ & Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ", callback_data="help")
                            ],
                            [
                                InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url=f"t.me/{UPDATES_CHANNEL}"),
                                InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url=f"t.me/{SUPPORT_GRPUP}")
                            ],
                            [
                                InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")
                            ],
                            [
                                InlineKeyboardButton("Dᴇᴠʟᴏᴩᴇʀ 👨‍💻", user_id=f"{OWNER}"),
                                InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")
                            ]
                        ]
                    )
                )
            )
            await stkr.delete()
            await stm.delete()
            os.remove(final_image_path)
        except Exception as e:
            print(f"Error replying to message: {e}")

    elif len(text) > 1 and "getfiles" not in text:
        try:
            code = message.text.split()[1]
            user_id, file_id = code.split('_')
            msg = await client.get_messages(int(DB_CHANNEL), int(file_id))
            send_media = await msg.copy(message.from_user.id)
            await message.reply_text(
                "**‼️Fɪʟᴇ ᴡɪʟʟ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ɪɴ 𝟸 ᴍɪɴᴜᴛᴇs😱**"
                "__💡Fᴏʀᴡᴀʀᴅ ɪᴛ ᴛᴏ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ᴏʀ ᴀɴʏᴡʜᴇʀᴇ ʙᴇғᴏʀᴇ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ.😁__"
                f"**😇Jᴏɪɴ @{UPDATES_CHANNEL}**"
            )
            await message.delete()
            await asyncio.sleep(120)  # Sleep for 2 minutes (2 * 60 = 120 seconds)
            await send_media.delete()
        except Exception as e:
            print(f"Error processing media: {e}")

    elif "getfiles" in text:
        try:
            text = text.split(maxsplit=1)[1][8:]
            decoded_string = await decode(text)
            result = await get_file(decoded_string)
            if result is not None:
                temp_msg = await message.reply(f"Please wait...")
                base64_string = result.split("?start=")[1]
                user_id, file_id = base64_string.split('_')
                msg = await client.get_messages(int(DB_CHANNEL), int(file_id))
                caption = msg.caption
                button1 = InlineKeyboardButton("Get Files", callback_data=f"get_file_{result}")
                button2 = InlineKeyboardButton("Close", callback_data="delete")
                markup = InlineKeyboardMarkup([[button1, button2]])
                await temp_msg.edit(
                    f"Hello {message.from_user.first_name}, here are your files\n\nfile name: {caption}\n\nClick on the Button Below to get files\n\nNote: Files will be deleted in a few minutes, so forward them to saved messages ASAP.",
                    reply_markup=markup
                )
        except Exception as e:
            print(f"Error decoding or getting short URL: {e}")
            pass
            
        await message.delete()

        
# Define other functions like handle_private_message, force_sub, decode, and get_short here if not already done.


#  elif "short" in text:
#    text = text.split(maxsplit=1)[1][5:]
#    result=await get_short(text)
#    try:
#        result = result[text]
#    except:
#        return

#    temp_msg = await message.reply("Please wait...")

#    try:
#        base64_string = result.split("=", maxsplit=1)[1]
   # except:
#        return

#    string = await decode(base64_string)
#    argument = string.split("-")
#    if len(argument) == 3:
 #       try:
 #           start = int(int(argument[1]) / abs(client.db_channel.id))
 #           end = int(int(argument[2]) / abs(client.db_channel.id))
#        except:
#            return
  #      if start <= end:
#            ids = range(start, end+1)
 #       else:
#            ids = []
#            i = start
#            while True:
  #              ids.append(i)
 #               i -= 1
#                if i < end:
 #                   break
 #   elif len(argument) == 2:
#        try:
#            ids = [int(int(argument[1]) / abs(client.db_channel.id))]
#        except:
#            return

#    try:
#        messages = await get_messages(client, ids[:4])
#    except:
 #       await message.reply_text("Something went wrong..!")
     #   return
 #    await temp_msg.delete()
  #   txt = ""
 #   ctr = 1
 #   for msg in messages:
#        if len(ids) > 4 and ctr == 5:
 #           break
#        txt += f"➤ <code>{msg.caption}</code>\n"
 #       ctr += 1

#    if len(ids) > 4:
 #       txt += f"➤ <code>And More</code>\n"

#    await message.reply_text(f'''<b>Hey 👋 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>, Your File(s) With Name(s)
        
#{txt.strip()}

#Is Ready To Be Sent , Open The Below Link To Get Your File(s)</b>''', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("• Open Link •", url=result)], [InlineKeyboardButton("• Join •", url="https://t.me/NG_BotS")]]))

    
@Client.on_message((filters.document|filters.video|filters.audio|filters.photo) & filters.incoming & ~filters.regex(r'^edited'))
async def sv_file(client: Client, message : Message):
    send_message = await message.reply_text("**Processing...**", quote=True)
    media = message.document or message.video or message.audio or message.photo
    text = ""

    if not message.photo:
        text = "--**🗃️ Fɪʟᴇ Dᴇᴛᴀɪʟs:**--\n\n"
        text += f"📂 ** Fɪʟᴇ ɴᴀᴍᴇ :** `{media.file_name}`\n\n" if media.file_name else ""
        text += f"🍃 **Mɪᴍᴇ Tʏᴘᴇ:** __{media.mime_type}__\n\n" if media.mime_type else ""
        text += f"📦 **Fɪʟᴇ ꜱɪᴢᴇ :** __{humanbytes(media.file_size)}__\n\n" if media.file_size else ""

        if not message.document:
            text += f"🎞 **Dᴜʀᴀᴛɪᴏɴ:** __{TimeFormatter(media.duration * 1000)}__\n\n" if media.duration else ""
            if message.audio:
                text += f"🎵 **Tɪᴛʟᴇ:** __{media.title}__\n\n" if media.title else ""
                text += f"🎙 **Pᴇʀғᴏʀᴍᴇʀ:** __{media.performer}__\n\n" if media.performer else ""

        text += f"**✏ Cᴀᴘᴛɪᴏɴ:** __{message.caption}__\n\n" if message.caption else ""
        text += f"**🍁--Uᴘʟᴏᴀᴅᴇᴅ Bʏ :--** [{message.from_user.first_name}](tg://user?id={message.from_user.id}) \n\n"

        msg = await message.copy(int(DB_CHANNEL))
        info = await msg.reply(text)

        bot = await client.get_me()
        link = await gen_link(bot, f"https://t.me/{bot.username}?start={message.chat.id}_{msg.id}")
        url = await get_shorturl(link, u_id=message.from_user.id)

        txt = quote(text.replace('--', ''))
        share_url = f"tg://share?url={txt}File%20Link%20👉%20{url}"

        buttons = [[
            InlineKeyboardButton(text="Oᴘᴇɴ Uʀʟ 🔗", url=url),
            InlineKeyboardButton(text="Sʜᴀʀᴇ Lɪɴᴋ 👤", url=share_url)
        ], [
            InlineKeyboardButton(text="Dᴇʟᴇᴛᴇ Fɪʟᴇ🗑", callback_data=f"del+{msg.id}")
        ]]

        await send_message.edit(
            text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

        info_buttons = [[
            InlineKeyboardButton(text="Oᴘᴇɴ Uʀʟ 🔗", url=link),
          #  InlineKeyboardButton(text="Sʜᴀʀᴇ Lɪɴᴋ 👤", url=share_url)
        ],  [
            InlineKeyboardButton(text="Dᴇʟᴇᴛᴇ Fɪʟᴇ🗑", callback_data=f"del+{msg.id}")
        ]]
        
        await info.edit(
            text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )









@Client.on_message(filters.command('set_shortner') & filters.private)
async def set_shortner(client: Client, m: Message):
    if len(m.command) == 1:
        return await m.reply_text("**Give me shortner url to set**\n\n**Example - /set_shortner shortner domain(example.com , example.in)**")

    user_id = m.from_user.id
    shortner = m.text.split(' ', 1)[1]
    await udb.set_shortner(m.from_user.id, shortner=shortner)
    await m.reply_text(f'**Your Shortner saved successfully!**\n\n**Your Shortner: `{shortner}`**')

@Client.on_message(filters.command('set_api') & filters.private)
async def set_api(client: Client, m: Message):
    if len(m.command) == 1:
        return await m.reply_text("**Give me api to set**\n\n**Example - /set_api yourapi**\n\n**Get your api [here](https://cyberurl.me/member/tools/api)**")

    user_id = m.from_user.id
    api = m.text.split(' ', 1)[1]
    await udb.set_api(m.from_user.id, api=api)
    await m.reply_text(f'**API key saved successfully!**\n\n**Your API: `{api}`**')

@Client.on_message(filters.command('set_fsub') & filters.private)
async def set_fsub(client: Client, m: Message):
    if len(m.command) == 1:
        return await m.reply_text("**Give me channel id to set**\n\n**Example - /set_fsub channel id**\n\n**Get your channel's id in rose bot**")

    user_id = m.from_user.id
    u_fsub = m.text.split(' ', 1)[1]

    if u_fsub and u_fsub.startswith("-100"):
        fsub = int(u_fsub)
    elif u_fsub and (not u_fsub.startswith("-100")):
        await m.reply_text("send your channel id to set/ngo to rose bot and get your channel id")
    else:
        await udb.set_fsub(m.from_user.id, fsub=fsub)
        await m.reply_text(f"**Channel id saved successfully!**\n**Your Channel id: `{fsub}`**\nDon't forget to make me admin to force users to join your channel**")

_shortener = os.environ.get("SHORTENER_SITE")
_shortener_api = os.environ.get("SHORTENER_API")

async def shrt_limk(longurl, message):
    if not longurl.startswith("http://") and not longurl.startswith("https://"):
        # If the URL doesn't start with http:// or https://,
        snd_msg = await message.reply_text("Send http:// or https:// link to short")
        return snd_msg

    try:
        res = requests.get(f'https://{_shortener}/api?api={_shortener_api}&url={quote(longurl)}')
        res.raise_for_status()  # Check for any request errors
        response_data = res.json()
        shorted = response_data.get('shortenedUrl')

        # Send the shortened link as a reply
        reply_text = f"Shortened URL: {shorted}"
        return await message.reply_text(reply_text)
    
    except requests.exceptions.RequestException as e:
        err_msg = f"An error occurred: {e}"
        print(err_msg)
        return await message.reply_text(err_msg)



@Client.on_message(filters.command('getfile'))
async def getfile(client, message):
    await message.delete()
    fsub = await force_sub(client, message)
    if fsub == 400:
        return
    if len(message.command) > 1:
        try:
            message.command[1] = await decode(message.command[1])
        except:
            pass
        user_id, file_id = message.command[1].split('_')
        msg = await client.get_messages(int(DB_CHANNEL), int(file_id)) #if DB_CHANNEL else await client.get_messages(int(user_id), int(file_id))
        send_media = await msg.copy(message.from_user.id)
        await message.reply_text("**‼️ File will auto delete in few minutes😱**\n__💡Forward it to saved massages or anywhere before downloading.😁__\n**😇Join @NG_BotS**")
        await asyncio.sleep(50)
        await send_media.delete()










#@mxabot.on_message(filters.text & filters.private)
#async def get_shrtlimk(client, message):
#    msg_txt = message.text
#    if msg_txt.startswith("http://") and msg_txt.startswith("https://"):
 #       await shrt_limk(msg_txt, message)

