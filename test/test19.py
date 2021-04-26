from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import ChannelParticipantsBots
from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoin
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser

import asyncio
import logging

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
################################################
channel = '@poolpruebas'
offset = 0
limit = 100
all_participants = []
usernames = []

client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect() # logining and connecting to Telegram servers

channel_use = client(ResolveUsernameRequest('poolpruebas')) # Your channel username

@events.register(events.ChatAction(func=lambda e: e.action_message is None))
async def chat_action_empty(event: events.ChatAction.Event):
    print(event.stringify())
    
@client.on(events.ChatAction("@poolpruebas"))
async def handler(event):
# Welcome every new user
    print(event)
    if event.user_joined:
        await event.reply('Welcome to the group!')

@classmethod
def build(cls, update, others=None, self_id=None):
     if isinstance(update, types.UpdateChatParticipantAdd):
            return cls.Event(types.PeerChat(update.chat_id),
                             added_by=update.inviter_id or True,
                             users=update.user_id)



client.run_until_disconnected()