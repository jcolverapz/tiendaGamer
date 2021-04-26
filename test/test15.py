from telethon.sync import TelegramClient, events, utils
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telegram.ext.filters import Filters
from telethon.tl.functions.channels import InviteToChannelRequest
import asyncio

api_id=3409046
api_hash='48ae9fbdf79edda291e1fa5796fc4665'
channel = '@pruebastienda'
# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect()
client.start()

@client.on(events.NewMessage(pattern=r'(?i).*\b(hello|hi)\b'))
async def handler(event):
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    await event.reply('hi!')
    print(name, 'said', event.text, '!')

@client.on(events.NewMessage(pattern=r'(?i).*diablos'))
async def my_handler(event):
    await event.delete()

async def my_event_handler(event):
    await event.reply('hi!')

try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()