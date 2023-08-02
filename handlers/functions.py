import pytz
from datetime import date
import random
import string
from database import save_media as save_file
import base64

async def decode(base64_string):
    base64_bytes = base64_string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string

async def encode_string(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

async def generate_random_string(num: int):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(num))
    return random_string

async def gen_link(bot, url):
    rndm = await generate_random_string(15)
    await save_file(rndm, url)
    code = await encode_string(rndm)
    response_text = f"https://t.me/{bot.username}?start=getfiles{code}"
    return response_text


def humanbytes(size_in_bytes):
    if not size_in_bytes:
        return ""

    power_of_2 = 2 ** 10
    exponent = 0
    size = size_in_bytes

    byte_units = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}

    while size > power_of_2:
        size /= power_of_2
        exponent += 1

    return f"{round(size, 2)} {byte_units[exponent]}B"


def TimeFormatter(milliseconds: int) -> str:
    total_seconds, milliseconds_remainder = divmod(int(milliseconds), 1000)
    total_minutes, seconds_remainder = divmod(total_seconds, 60)
    total_hours, minutes_remainder = divmod(total_minutes, 60)
    total_days, hours_remainder = divmod(total_hours, 24)

    time_parts = []
    if total_days:
        time_parts.append(f"{total_days} days")
    if total_hours:
        time_parts.append(f"{total_hours} hrs")
    if total_minutes:
        time_parts.append(f"{total_minutes} min")
    if total_seconds:
        time_parts.append(f"{total_seconds} sec")
    if milliseconds_remainder:
        time_parts.append(f"{milliseconds_remainder} millisec")

    return ", ".join(time_parts)


TOKENS = {}
VERIFIED = {}

async def check_token(bot, userid, token):
    user = await bot.get_users(userid)
    if user.id in TOKENS.keys():
        TKN = TOKENS[user.id]
        if token in TKN.keys():
            is_used = TKN[token]
            if is_used == True:
                return False
            else:
                return True
    else:
        return False


async def get_token(bot, userid, link):
    user = await bot.get_users(userid)
    token = await generate_random_string(7)
    TOKENS[user.id] = {token: False}
    link = f"{link}verify-{user.id}-{token}"
    shortened_verify_url = await get_shortlink(link)
    return str(shortened_verify_url)

async def verify_user(bot, userid, token):
    user = await bot.get_users(userid)
    TOKENS[user.id] = {token: True}
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    VERIFIED[user.id] = str(today)

async def check_verification(bot, userid):
    user = await bot.get_users(userid)
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    if user.id in VERIFIED.keys():
        EXP = VERIFIED[user.id]
        years, month, day = EXP.split('-')
        comp = date(int(years), int(month), int(day))
        if comp < today:
            return False
        else:
            return True
    else:
        return False
