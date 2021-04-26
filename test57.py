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

CHAT_ID = 1204307512

bot = telebot.TeleBot(TOKEN)

"""
def notify(message):
    #bot.send_message(CHAT_ID, 'Notification from ' + ':\n' + message)
    #bot.send_message(CHAT_ID, 'Example', reply_markup=reply_markup)
    #bot.send_message(CHAT_ID, 'hi', buttons=Button.text('hi!', selective=True))

notify('Hello world!')

client.send_message(CHAT_ID, 'Welcome', buttons=[
    Button.text('Thanks!', resize=True, single_use=True),
    Button.request_phone('Send phone'),
    Button.request_location('Send location')
])
"""
results = client.inline_query('like', 'Do you like Telethon?')
#Forcing a reply or removing the keyboard can also be done:
#client.send_message(CHAT_ID, 'Reply to me', buttons=Button.force_reply())
#client.send_message(CHAT_ID, 'Bye Keyboard!', buttons=Button.clear())