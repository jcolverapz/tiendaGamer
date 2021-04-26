import sys
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient, events
from telethon.sync import TelegramClient

from telethon import functions, types

from telethon.tl.functions.users import GetFullUserRequest
import json
from telethon import utils

TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'

#client = TelegramClient("new",api_id,api_hash).start(bot_token=TOKEN)

#full = await client(GetFullUserRequest(1204307512))
# or even
#full = await client(GetFullUserRequest())

#bio = full.about

with TelegramClient("new", api_id, api_hash) as client:
    full  = client(functions.users.GetFullUserRequest(id=1496283722))
    username = full.user.username
    first_name = full.user.first_name
    phone = full.user.phone
    
    #users= result.json()
    #users = json.dumps(result, separators=(','))
    #ini_string = json.dumps(result,separators=",")
    #userStr = json.dumps(result, outfile, cls=DateTimeEncoder)
    #JSON.parse(userStr, (key, value) => {
    #if (typeof value === 'string') {
    #return value.toUpperCase();
    #return value
  