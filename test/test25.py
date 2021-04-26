import asyncio


api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@pruebastienda'
################################################


from telethon import TelegramClient, events
@events.register(events.ChatAction(func=lambda e: e.action_message is None))
async def chat_action_empty(event: events.ChatAction.Event:
    print(event.stringify())


async def main():
    client = TelegramClient('pruebastienda', api_id, api_hash) 
    client.add_event_handler(chat_action_empty)
    await client.start()
    me = await client.get_me()
    print('Logged in as {} with Telethon version {}'.format(me.username, TelegramClient.__version__))
    await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())