from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import InputPeerEmpty

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
################################################
channel = '@pruebastienda'
offset = 0
limit = 100
all_participants = []
usernames = []

# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect

result = client(ResolveUsernameRequest('@pruebastienda'))
#found_chats = result.chats
#found_users = result.users
#r = client(GetFullChannelRequest(result.chats[0]))