from telethon import TelegramClient
from telethon import events

import asyncio
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@pruebastienda'
################################################
client = TelegramClient('sessionname', api_id, api_hash)
#client.connect()
client.start()
#d=client.get_dialogs()
#p=client.get_participants(channel)
m=client.get_messages(channel, 100)
print(m)
