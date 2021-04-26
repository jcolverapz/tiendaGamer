from telethon import events
from telethon import TelegramClient
from telethon.tl.custom import Button
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'

#bot = TelegramClient(...)
client = TelegramClient('newsession', api_id, api_hash)  # feel free to edit %sessionname% as you want
#client.connect() # logining and connecting to Telegram servers
client.start()

@client.on(events.CallbackQuery)
async def handler(event):
    await event.answer('You clicked {}!'.format(event.data))

client.send_message(1204307512, 'Pick one', buttons=[
    [Button.inline('Left'), Button.inline('Right')]]
    )