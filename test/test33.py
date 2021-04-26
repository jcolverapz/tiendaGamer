from telethon import TelegramClient, events
from telethon.sync import TelegramClient, events
from telethon import functions, types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import ChannelParticipantsKicked # import type to use as filter
from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoin
from telethon.tl.types import ChannelParticipantsSearch
import asyncio

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
channel = '@pruebastienda'
offset = 0
limit = 100
all_participants = []
users = []

# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect() # logining and connecting to Telegram servers
client.start()
#   Todos los comentarios
#d = client.get_dialogs(10)


    #await event.respond('!pong')
    #if event.user_joined:
     #   await event.reply('Welcome to the group!')
    
    #client.remove_event_handler(handler, events.Raw)
    #if event.uploading:
        #await client.send_message(event.user_id,'What are you sending?')
    #me = await client.get_me()
    #print("click")
    #await event.reply('Hey!')
    #await event.messages.reply('Welcome to the group!')
    #client.send_message('@pruebastienda','hellooo')
        #update.message.reply_text("New user joined")
    #client.send_message(channel, "New user joined")
        #print("Evento")
#async def pruebas()   
  