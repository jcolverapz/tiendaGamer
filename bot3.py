import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from pytest import mark
from telethon import TelegramClient
from telethon.tl.custom.message import Message
import asyncio
# Your API ID, hash and session string here
#api_id = int(os.environ["TELEGRAM_APP_ID"])
#api_hash = os.environ["TELEGRAM_APP_HASH"]
#session_str = os.environ["TELETHON_SESSION"]

api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@micanaljc'
#client = TelegramClient('newsession', api_id, api_hash)

@pytest.fixture(scope="session")
async def client() -> TelegramClient:
    # Connect to the server
    await client.connect()
    # Issue a high level command to start receiving message
    await client.get_me()
    # Fill the entity cache
    await client.get_dialogs()

    yield TelegramClient(
        StringSession('newsession'), api_id, api_hash,
        sequential_updates=True
    )
    
    #await client.disconnect()
    #await client.disconnected


@mark.asyncio
async def test_help(client: TelegramClient):
    # Create a conversation
    with client.conversation("@dante_dog_bot", timeout=5) as conv:
        # Send a command
        await conv.send_message("/help")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "@dante_dog_bot" in resp.raw_text
        assert "👍" in resp.raw_text
        assert "👎" in resp.raw_text

from pytest import mark
from secrets import token_urlsafe
from telethon import TelegramClient
from telethon.tl.custom.message import Message
#from telethon.tl.message import BotCallbackAnswer

@mark.asyncio
async def test_start(client: TelegramClient):
    # Create a conversation
    with client.conversation("@dante_dog_bot", timeout=5) as conv:
        # User > /start
        await conv.send_message("/start")
        # Bot < Let's create a message with emoji like-buttons. First, send
        # me the message. It can be anything — a text, photo, video, even a
        # sticker.

        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "create a message" in resp.raw_text

        # User > Message body L9b_vp7IV6hVAR5ADsYxYL9w7YPQw-HLlqHopcwf20I
        message = f"Message body {token_urlsafe(32)}"
        # Bot < Now send me one or more emoticons that we will use for buttons
        # (up to 6 emoji). Use /cancel if you changed your mind.
        await conv.send_message(message)
        resp = await conv.get_response()
        assert "emoticon" in resp.raw_text
        assert "6" in resp.raw_text
        assert "/cancel" in resp.raw_text

        # User > 🆗🆒❤️🤣
        #emojis = ["🆗", "🆒", "❤️", "🤣"]
       # await conv.send_message(emojis.join(""))

        # Bot < 👍 Post created. Now use the ‘Publish’ button to send it to
        # your friends.
        resp = await conv.get_response()
        assert "👍" in resp.raw_text
        assert "Publish" in resp.raw_text

        # Bot < Message body L9b_vp7IV6hVAR5ADsYxYL9w7YPQw-HLlqHopcwf20I
        # [🆗][🆒][❤️][🤣]
        # [    Publish    ]
        resp = await conv.get_response()
        assert resp.raw_text == message
        #assert resp.button_count == len(emojis) + 1
        #assert [i.text for i in resp.buttons[0]] == emojis
        assert resp.buttons[1][0].text == "Publish"

        # Test reaction
        # Click on button [🆗]
        #answer: BotCallbackAnswer = await resp.click(text=emojis[0])
        # Bot gives response > You 🆗 this.
        #assert emojis[0] in answer.message
        # Bot (edited) < Message body L9b_vp7IV6hVAR5ADsYxYL9w7YPQw-HLlqHopcwf20I
        # [🆗1][🆒][❤️][🤣]
        # [     Publish    ]
        resp = conv.get_edit(message=resp)
        assert "1" in resp.buttons[0][0].text

async def main():
    try:
        #await plugins.init(client)
        await client.run_until_disconnected()
    #finally:
    except:
        print('Exception')
            #await client.disconnect()

    if __name__ == '__main__':
        asyncio.run(main()) 