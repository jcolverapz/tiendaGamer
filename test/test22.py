from telethon import TelegramClient, events

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputUser
from telethon.tl.types import ChannelAdminLogEventActionChangeAbout
from telethon.tl.functions.channels import GetFullChannelRequest
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@pruebastienda'
################################################

client = TelegramClient('sessionname', api_id, api_hash) 
client.start()

#group_id = ...

async def main():
# Could also get the user id from an event; this is just an example
    user_id = '@jcolvera1991'
    async with client.conversation(user_id) as conv:
    # Get a handle to the future event we'll wait for
        handle = conv.wait_event(events.ChatAction(
        channel,
        func=lambda e: e.user_joined and e.user_id == user_id
    ))
    # Perform whatever action in between
    await conv.send_message('Please join')
    # Wait for the event we registered above to fire
    event = await handle
    # Continue with the conversation
    await conv.send_message('Thanks!')

    