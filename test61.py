from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'
  
client = TelegramClient('session_name', api_id, api_hash)
client.start()
 
channel_entity = client.get_entity(channel)
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=1,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))
messageId = posts.messages[0].id

reply_markup=ReplyInlineMarkup(
        rows=[
            KeyboardButtonRow(
                buttons=[
                    KeyboardButtonUrl(
                        text=' Go to website',
                        url='https://www.google.com'
                    ),
                ]
            ),
            KeyboardButtonRow(
                buttons=[
                    KeyboardButtonCallback(
                        text=' Report',
                        data=b'{"name":"ReportClick","id":"120326622"}'
                    ),
                    KeyboardButtonCallback(
                        text='⏩ Skip',
                        data=b'{"name":"SkipClick","id":"120326622"}'
                    ),
                ]
            ),
        ]
    ),

client(GetBotCallbackAnswerRequest(
    channel,
    messageId,
    data=posts.messages[0].reply_markup.rows[0].buttons[0]))


client.disconnect()