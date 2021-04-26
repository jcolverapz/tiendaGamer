from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telegram.ext.filters import Filters
import asyncio
api_id=3409046
api_hash='48ae9fbdf79edda291e1fa5796fc4665'
channel = '@pruebastienda'
#entity = client.get_entity(chn)
# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect()
print(client.get_me().stringify())


#async def main():
# await asyncio.wait(
# client(functions.channels.JoinChannelRequest(
# channel='jcolvera1991')))