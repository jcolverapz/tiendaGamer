from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser
from telethon import types

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
phone_number = '+528132341246'
channel = '@pruebastienda'
################################################

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
client = TelegramClient(channel, api_id, api_hash)
client.start()

async def main():
    username = await client.get_entity('@pruebastienda')
    #entity = await client.get_entity('@pruebastienda')
    print(username)

#client.remove_event_handler()