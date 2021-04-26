from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
#from telethon.tl.functions.channels import get_participants

api_id=3409046
api_hash='48ae9fbdf79edda291e1fa5796fc4665'
client = TelegramClient('anon', api_id, api_hash)
entity = client.get_entity("t.me/micanaljc") #omit @
channel = "@micanaljc"

# get all the users and print them
for u in client.get_participants(channel):
    print(u.id, u.first_name, u.last_name, u.username)

    #with TelegramClient('sessionname', api_id, api_hash) as client:
        #r = client(functions.channels.JoinChannelRequest(channel='@pruebastienda'))
    #print(r)