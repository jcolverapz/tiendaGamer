
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import User
from telethon.tl.types import ChannelParticipant
from telethon.tl.types import ChannelParticipantsKicked # import type to use as filter
from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoin
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import UpdateUserStatus
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telethon.tl.functions.messages import StartBotRequest
#from telethon.tl.types import ChannelAdminLogEventAction
import asyncio
from datetime import datetime
import time
import typing
from contacts import miscontactos, buscar
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
)
import telebot

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'

################################################
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
client.start()

# content of the automatic reply

TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
bot = telebot.TeleBot(TOKEN)
 #await event.respond('@dante_dog_bot', '/start params_string')
#if __name__ == '__main__':
 
        #time.sleep(1)  # pause for 1 second to rate-limit automatic replies
        #await event.respond('@dante_dog_bot', '/start params_string')
@client.on(events.UserUpdate)
async def handler(event): 

#@client.on(events.NewMessage(incoming=True))
#async def handle_new_message(event):
    #@bot.on(events.NewMessage)
    #$async def echo(event):
    """Echo the user message."""
    #print(f"get it {event.text}")
    await client.send_message('@dante_dog_bot', '/start params_string')
    #await client.send_message("@zeidardz",message="Hello python")
from telethon.tl.functions.messages import StartBotRequest

request = StartBotRequest("bot_username_bot", "bot_username_bot", "params_string")
result = await client(request)

print(time.asctime(), '-', 'Auto-replying...')
#client.connect() # logining and connecting to Telegram servers
 result = client.invoke(ImportContactsRequest([contact], replace=True))
contacts = client.invoke(GetContactsRequest(""))
for u in result.users:
    client.send_message(u, 'Hi')
client.run_until_disconnected()
print(time.asctime(), '-', 'Stopped!')



loop = asyncio.get_event_loop()
 