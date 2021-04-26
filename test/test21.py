from telethon import TelegramClient
from telethon import events
from telethon.tl.functions.channels import GetParticipantsRequest
#from telethon.tl.functions.channels import AdminLogEvent
from telethon.sync import TelegramClient

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@pruebastienda'
################################################

client = TelegramClient('sessionname', api_id, api_hash) 
client.start()
responses = client.get_participants(channel)
print(responses[0].first_name)
client.run_until_disconnected()
