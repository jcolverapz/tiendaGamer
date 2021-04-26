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
offset = 0
limit = 100
all_participants = []
usernames = []

client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect() # logining and connecting to Telegram servers

channel_use = client(ResolveUsernameRequest('pruebastienda')) # Your channel username
#print(channel_use)
#admins = [InputUserSelf(), InputUser(user.users[0].id, user.users[0].access_hash)] # admins
admins = [] # No need admins for join and leave and invite filters

##print(result)
#result = client(GetFullChannelRequest(channel))
#print(result)
# Then we need a loop to work with
loop = asyncio.get_event_loop()

# We also need something to run
async def main():
    #for char in 'Hello, world!\n':
        #print(char, end='', flush=False)
        #await asyncio.sleep(1)
    for _user in result.users:
        print(_user.id,_user.first_name, _user.last_name, flush=True)
        await asyncio.sleep(0.5)
# Then, we need to run the loop with a task
loop.run_until_complete(main())

client.disconnect()
print("Desconectado")
#for _user in result.users:
    #print(_user.first_name, _user.last_name)
    #with open(''.join(['users/', str(_user.id)]), 'w') as f:
     #   f.write(str(_user.id))

#client.run_until_disconnected()