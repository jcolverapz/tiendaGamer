from telethon import TelegramClient
from telethon import events
from telethon.sync import TelegramClient
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
#phone_number = '+528132341246'
channel = '@pruebastienda'
################################################

client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect() # logining and connecting to Telegram servers
client.start() 
#@client.on(events.MessageDeleted)
#client.delete_messages() 
with TelegramClient('sessionname', api_id, api_hash) as client:
    client.add_event_handler(handlers.welcome.handler)

    client.run_until_disconnected()