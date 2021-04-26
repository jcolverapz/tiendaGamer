import asyncio
from telethon import TelegramClient, events

from telethon.tl.types import ChannelParticipant
from telethon.tl.types import ChannelParticipantsKicked

from telethon.tl.functions.messages import StartBotRequest

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@pruebastienda'
################################################
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
client.start()

request = StartBotRequest("@dante_dog_bot","@dante_dog_bot", "params_string")
result =  client(request)

def main():
    kicked_members = client.get_participants(channel, filter=ChannelParticipantsKicked)
    # bannedMembers = client.get_participants(getBannedUsersFrom, filter=ChannelParticipantsKicked)
    print(kicked_members)

   

main()