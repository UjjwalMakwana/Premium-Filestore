import os
import asyncio
from pyrogram import Client, filters
#from pyrogram.file_id import FileId #FileID
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
from configs import *





#async def download_profile_photo(client: Client, user_id: int) -> str:
#    photos = await client.get_user_profile_photos(user_id, limit=1)
#    if photos and len(photos) > 0:
#        photo = photos[0].photos[0]
#        photo_file = photo.file_id
#        user_photo_path = f"./DOWNLOADS/user_photos/{user_id}.jpg"
#        await client.download_media(photo_file, file_name=user_photo_path)
#        return user_photo_path
#    else:
#        return None


#async def download_profile_photo(client: Client, message: Message):
#    try:
#        user = message.from_user
#        if user.photo:
#            photo = user.photo.big_file_id
#            user_photo_path = f"./DOWNLOADS/user_photos/{user.id}.jpg"
#            await asyncio.gather(
#                client.download_media(photo, file_name=user_photo_path)
#            )
#            return user_photo_path
#    except Exception as e:
#        print(f"Error occurred while downloading media: {e}")
#    return None

#async def send_welcome_message(mxabot: Client, message: Message):
#    stkr = await message.reply_sticker("CAACAgUAAxkBAAEDfBxkDaqQnQgeUhiSB-EOqOy2cHinOgACVgQAAuwJUFdwcdRqspNGrx4E")
 #   await message.delete()
#    stm = await message.reply_text("Generating A Special Welcome message For You...")
    #photos = await mxabot.get_profile_photos(message.from_user.id, limit=1)
   # if photos and len(photos) > 0:
   #     photo = photos[0]
   #     photo_file = photo.file_id
     #   user_photo_path = f"./DOWNLOADS/user_photos/{message.from_user.id}.jpg"
  #      try:
  #          await mxabot.download_media(photo_file, file_name=user_photo_path)
  #      except Exception as e:
 #           print(f"Error occurred while downloading media: {e}")
 #           await mxabot.send_message(message.chat.id, "Failed to download your profile photo.")
#            return
#    else:
  #      await mxabot.send_message(message.chat.id, "No profile photo found.")
 #       return
    #user_photo_path = await download_profile_photo(mxabot, message)


#====================================================================================================================================#



async def send_welcome_message(mxabot: Client, message: Message):
    stkr = await message.reply_sticker("CAACAgUAAxkBAAEDfBxkDaqQnQgeUhiSB-EOqOy2cHinOgACVgQAAuwJUFdwcdRqspNGrx4E")
    await message.delete()
    user_photo_path = f"./DOWNLOADS/user_photos/{message.from_user.id}.jpg"
    stm = await message.reply_text("Generating A Special Welcome message For You...")
    try:
        await mxabot.download_media(message.from_user.photo.big_file_id, file_name=user_photo_path)
    except Exception as e:
        print(f"Error occurred while downloading media: {e}")
        await mxabot.send_message(message.chat.id, "Failed to download your profile photo.")
        return

    
    welcome_photo_path = "./img_font.py/welcome_img.png"
    welcome_photo = Image.open(welcome_photo_path)
    user_photo = Image.open(user_photo_path)
    circular_size = (680, 680)
    user_photo = user_photo.resize(circular_size)
    mask = Image.new("L", circular_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, circular_size[0], circular_size[1]), fill=255)
    user_photo.putalpha(mask)
    position = ((welcome_photo.width - user_photo.width) // 2 - 773, (welcome_photo.height - user_photo.height) // 2)
    welcome_photo.paste(user_photo, position, user_photo)

    user_id_text = f"ID: {message.from_user.id}"
    font = ImageFont.truetype("./img_font.py/font_text.ttf", 65) 
    draw = ImageDraw.Draw(welcome_photo)
    text_position = (270, user_photo.height + 460)
    draw.text(text_position, user_id_text, fill="white", font=font)
    os.remove(user_photo_path)
    final_image_path = f"./DOWNLOADS/user_welcome_images/{message.from_user.id}_welcome.png"
    os.makedirs(os.path.dirname(final_image_path), exist_ok=True)
    welcome_photo.save(final_image_path, quality=170)
    
    return final_image_path, stkr, stm


   #await stm.edit("Generated, Now Sending...")
    #await asyncio.gather(
    #    mxabot.send_photo(message.chat.id, photo=final_image_path, caption=START_TEXT.format(message.from_user.mention), reply_markup=reply_markup)
    #)

    #await asyncio.sleep(0.5)
   # await stkr.delete()

   # await stm.delete()
