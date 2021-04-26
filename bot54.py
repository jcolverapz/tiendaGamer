from telethon import TelegramClient
from telethon import Button
# Remember to use your own values from my.telegram.org!

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
channel = '@micanaljc'

################################################
#      Create the client and connect
client = TelegramClient('newsession', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    #print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    #print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    #await client.send_message('me', 'Hello, myself!')
    # ...to some chat ID
    #await client.send_message(-100123456, 'Hello, group!')
    # ...to your contacts
    
   
    markup = client.build_reply_markup(Button.inline('hi'))
    # later
    #await client.send_message('+528119907899', 'Hello, friend!')
    await client.send_message('+528119907899', 'click me', buttons=markup)
    # ...or even to any username
    #await client.send_message('username', 'Testing Telethon!')

    # You can, of course, use markdown in your messages:
    message = await client.send_message(
        'me',
        'This message has **bold**, `code`, __italics__ and '
        'a [nice website](https://example.com)!',
        link_preview=False
    )

    # Sending a message returns the sent message object, which you can use
    print(message.raw_text)

    # You can reply to messages directly if you have a message object
    await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    #await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # You can print the message history of any chat:
    async for message in client.iter_messages('me'):
        print(message.id, message.text)
"""
        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        if message.photo:
            path = await message.download_media()
            #print('File saved to', path)  # printed after download is done
"""
with client:
    client.loop.run_until_complete(main())