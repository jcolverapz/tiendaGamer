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
from telethon.tl.functions.messages import GetInlineBotResultsRequest
from telethon.tl.functions.messages import GetInlineBotResultsRequest, SendInlineBotResultRequest, SendMessageRequest, SetTypingRequest
from telethon.tl.types import SendMessageTypingAction, SendMessageCancelAction
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, User as _User, Chat as _Chat, Channel as _Channel
from telethon.errors.rpcbaseerrors import RPCError
import asyncio

#from telethon.tl.types import ChannelAdminLogEventAction
import asyncio
from datetime import datetime

from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
)

import telebot # Importamos las librería
from telepot.loop import MessageLoop
import time

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'
offset = 0
limit = 100
all_participants = []
#all_participants = client.get_participants(channel)
users = []
################################################
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
client.start()
  
TOKEN = '1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0'

bot = telebot.TeleBot(TOKEN)


#inicia el codigo
#mybot = client.get_entity('1686414837:AAEinjhPgAMJD8ABV_hD6rCtJ2jsbXwVCm0')
mychat = client.get_entity('@micanaljc')


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Press me', callback_data='press')],
               ])

  



def inline_query():
    print("Query Inline")
    bot_results = client(GetInlineBotResultsRequest(
        bot, mychat, '', ''
    ))

   
    if bot_results.results:
        query_id = bot_results.query_id
        # choose a result from the list
        result_id = getResultId(bot_results.results)
        client(SendInlineBotResultRequest(
            mychat,
            query_id,
            result_id
        ))
        #return True

    else:
        print(bot_results)
        #return None

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': inline_query}).run_as_thread()

print('Listening ...')

while 1:
    time.sleep(10)