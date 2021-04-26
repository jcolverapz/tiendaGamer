from telethon import TelegramClient
from telethon.tl.functions.channels import CheckUsernameRequest
from telethon.tl.types import InputChannelEmpty
from telethon.tl.functions.contacts import ResolveUsernameRequest
import asyncio

api_id=3409046
api_hash='48ae9fbdf79edda291e1fa5796fc4665'
channel = '@pruebastienda'

client = TelegramClient('sessionid', api_id=3409046, api_hash=api_hash)
#client.connect()
input_channel = InputChannelEmpty()
#result = client.invoke(CheckUsernameRequest(input_channel, channel))

async def eternity():
    # Sleep for
    await asyncio.sleep(100)
    print('yay!')