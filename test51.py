
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import StartBotRequest

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'
################################################
#client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
#client.start()

with TelegramClient('session', api_id, api_hash) as client:
    client.connect()
    result = client(StartBotRequest(
        bot='dante_dog_bot', 
        peer='dante_dog_bot',
        start_param='some string here'))
        

#print(result.stringify())
print('Fin')


