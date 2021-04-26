from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telegram.ext.filters import Filters

def new_user(update, context):
    update.message.reply_text("New user joined.")

def main():  
    updater.dispatcher.add_handler(
        MessageHandler(Filters.status_update.new_chat_members, new_user)
    )

def addChannel(request):
    api_id   =   XXXXXX
    api_hash = 'xxxxxxxxxxxxxxxxxxxxx'
    client = TelegramClient('+254716550762', api_id, api_hash )
    with client:
        client.loop.run_until_complete(join(client))
    return HttpResponse('addChannel')

MessageHandler(Filters.new_chat_members, ...)



with client:
    client.loop.run_until_complete(main())