from telethon.sync import TelegramClient, events
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telegram.ext.filters import Filters
from telethon.tl.functions.channels import InviteToChannelRequest
import asyncio
#import plugins

api_id=3409046
api_hash='48ae9fbdf79edda291e1fa5796fc4665'
channel = '@pruebastienda'
# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect()
client.start()


async def join_start(event):
    if True :
        print('Joined')
        await client(JoinChannelRequest(channel))
        # Join the channel
        print('Verifying...')
        # Clicks the joined
        
@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')

async def main():
    try:
       # await plugins.init(client)
        await client.run_until_disconnected()
    finally:
            await client.disconnect()

    if __name__ == '__main__':
        asyncio.run(main())