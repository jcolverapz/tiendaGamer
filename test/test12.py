from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telegram.ext.filters import Filters

def switch(update, context):
    try:
        for new_member in update.message.new_chat_members:
            callback_id = str(new_member.id)
            # This is where I'm stuck

    except AttributeError:
        pass


def main():
    updater = Updater(str(TOKEN), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.chat(int(CHAT_ID)), switch))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

    def new_member(client, update):
    for member in update.message.new_chat_members:
        print(member)