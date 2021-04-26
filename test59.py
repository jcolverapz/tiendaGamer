from telethon import TelegramClient
from telethon import Button
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
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

 
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
from telebot import types

TOKEN = '1650639438:AAFgE3DIx0qzmAvBJc8Wu5acXUVoFSHE_vY'
#TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0' 
bot = telebot.TeleBot(TOKEN) 

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
channel = '@micanaljc'
CHAT_ID = 1204307512 
"""
################################################
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)
client.start()
"""
client = TelegramClient("session", api_id, api_hash)
#client = TelegramClient("bot", api_id, api_hash).start(bot_token=TOKEN)
client.start()

@client.on(events.NewMessage(pattern="/options"))
async def handler(event):
    print('event')

    keyboard = [
        [  
            Button.inline("First option", b"1"), 
            Button.inline("Second option", b"2")
        ],
        [
            Button.inline("Third option", b"3"), 
            Button.inline("Fourth option", b"4")
        ],
        [
            Button.inline("Fifth option", b"5")
        ]
    ]

    await client.send_message(event.chat_id, "Clic on:" )
    #await client.send_message('+528115180877', "Choose an option:", buttons=keyboard)
    #await client.send_message(event.chat_id, "Choose an option:", buttons=keyboard)
    """
    await client.send_message(1204307512, "Hola, da clic en el boton para enviar su contacto", 
    buttons=[Button.request_phone(text='Request phone')],silent=True)
"""
async def main():
    print('finish')
    await client.send_message('+528119907899', 'click me')
    # ...or even to any username
    #await client.send_message('username', 'Testing Telethon!')

    # You can, of course, use markdown in your messages:
    message = await client.send_message(
        'me',
        'This message has **bold**, `code`, __italics__ and '
        'a [nice website](https://example.com)!',
        link_preview=False
    )

    # You can reply to messages directly if you have a message object
    #await message.reply('Cool!')
    
with client:
    client.loop.run_until_complete(main())

"""
client.start()
client.run_until_disconnected()