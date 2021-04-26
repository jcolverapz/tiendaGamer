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
channel = '@pruebastienda'

@events.register(events.ChatAction(func=lambda e: e.action_message is None))
def chat_action_empty(event: events.ChatAction.Event):
    #print(event.stringify())
    print('this event')
async def main():
    client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
    client.add_event_handler(chat_action_empty)
    await client.start()
    me = await client.get_me()
    #print('Logged in as {} with Telethon version {}'.format(me.username, TelegramClient.__version__))
    await client.run_until_disconnected()
asyncio.get_event_loop().run_until_complete(main())

async def handler(event):
# event.input_chat may be None, use event.get_input_chat()

async def main():
    async for message in client.iter_messages('me', 10):
# Methods from the client always have these properties ready