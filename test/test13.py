from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telegram.ext.filters import Filters
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import InviteToChannelRequest # For channels (which includes megagroups)


api_id=3409046
api_hash='48ae9fbdf79edda291e1fa5796fc4665'
channel = '@pruebastienda'
# Create the client and connect
client = TelegramClient('sessionname', api_id, api_hash)  # feel free to edit %sessionname% as you want
client.connect()

async def main():
#await client(JoinChannelRequest(channel))
    await client(InviteToChannelRequest(
    channel,
    ['@jcolvera1991']
))
from telethon.tl.functions.messages import AddChatUserRequest

await client(GetBotCallbackAnswerRequest(
            peer=pruebastienda,
            msg_id=event.message.id,
            data=event.message.reply_markup.rows[0].buttons[1].data
            ))