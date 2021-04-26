from telethon import TelegramClient, events
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputUser
from telethon.tl.types import ChannelAdminLogEventActionChangeAbout
from telethon.tl.types import ChannelAdminLogEventActionParticipantInvite
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoinByInvite
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoin
from telethon.tl.types import ChannelAdminLogEventActionParticipantLeave
from telethon.tl.functions.channels import GetFullChannelRequest
import asyncio
#from telethon.tl.functions.channels import EventBuilder, EventCommon
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@pruebastienda'
################################################
client = TelegramClient('pruebastienda', api_id, api_hash) 
client.start()
# https://t.me/joinchat/CKxShUHGRWA3MDVh

@client.on(events.NewMessage(pattern='hello'))
async def handler(event):
    # Respond whenever someone says "Hello" and something else
    await event.reply('Hey!')

@client.on(events.NewMessage(outgoing=True, pattern='!ping'))
async def handler(event):
    # Say "!pong" whenever you send "!ping", then delete both messages
    m = await event.respond('!pong')
    await asyncio.sleep(5)
    await client.delete_messages(event.chat_id, [event.id, m.id])


@client.on(events.ChatAction)
# Welcome every new user
async def handler(event):
    await event.reply('Welcome!')

#class EventCommon(channel, abc.ABC):
#telethon.events.common.EventBuilder(channel)

client.run_until_disconnected()