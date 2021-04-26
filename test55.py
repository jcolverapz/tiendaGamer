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

from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

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
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0' 

bot = telebot.TeleBot(TOKEN) 

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
channel = '@micanaljc'
################################################
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)
client.start()

#bot.send_message(1204307512, 'A single button, with "clk1" as data',
    #buttons=Button.inline('Click me', b'clk1'))

keyboard=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="First Button")]])
#client.send_message(1204307512, 'Use custom keyboard', reply_markup=keyboard)

#time.sleep(4)

#bot.sendMessage(1204307512, 'Use inline keyboard', reply_markup=keyboard)

#bot.sendMessage(1204307512, 'Example', reply_markup=reply_markup)
bot.send_message(1204307512, 'hi', buttons=Button.text('hi!', selective=True))
# status = bot.send_message(chat_id='@monsterKing_bot', text=msg, parse_mode=telegram.ParseMode.HTML)  
#with client, bot:
@client.on(events.NewMessage(from_users=1204307512))
async def handler(event):
    await event.click()
    print('on click')
    #client.disconnect()



   
"""
url = f'https://t.me/{me.username}?start=captcha'
                await event.reply(
                    'Welcome! Please solve a captcha before talking',
                    buttons=Button.url('Solve captcha', url))
"""
client.run_until_disconnected()