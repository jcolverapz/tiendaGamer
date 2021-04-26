from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
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
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
client.start()

@client.on(events.UserUpdate)
#async def handler(event):
   
async def callback(event):
    await event.edit('Thank you for clicking {}!'.format(event.data))

client.send_message(chat, 'A single button, with "clk1" as data',
                    buttons=Button.inline('Click me', b'clk1'))

client.send_message(chat, 'Pick one from this grid', buttons=[
    [Button.inline('Left'), Button.inline('Right')],
    [Button.url('Check this site!', 'https://lonamiwebs.github.io')]
])
             
         
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'
bot = telebot.TeleBot(TOKEN)

with bot.conversation(chat) as conv:
    conv.send_message('Hi!')
    hello = conv.get_response()

    conv.send_message('Please tell me your name')
    name = conv.get_response().raw_text

    while not any(x.isalpha() for x in name):
        conv.send_message("Your name didn't have any letters! Try again")
        name = conv.get_response().raw_text

    conv.send_message('Thanks {}!'.format(name))

 