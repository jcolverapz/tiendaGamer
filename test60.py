from telethon import TelegramClient, sync, events
from telethon.sync import TelegramClient
from telethon import functions, types

from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telethon.tl.functions.messages import StartBotRequest
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telethon import Button

channel_username = '@pruebastienda'
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
################################################
# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)
client.start()

@client.on(events.NewMessage(pattern="Hi"))
async def my_event_handler(event):
    print(event.text)
    """
    messages = client.get_messages('GOOGLE')
    messages[0].click()
    
    sender = await event.get_sender()
    messages = await client.get_messages(sender.username)
    await messages[0].click(0)
    #client.forward_messages(chat, message_id, from_chat)
    client.forward_messages(1511413607, 1511413607, "from_chat")
        message.forward_to(chat)
    """
    await client.send_message(1204307512, 'Pick one from this grid', buttons=[
        [Button.inline('Left'), Button.inline('Right')],
        [Button.url('Check this site!', 'https://lonamiwebs.github.io')]
        ])



client.run_until_disconnected()