from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import InputChannel
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import ChannelParticipantsKicked # import type to use as filter
from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoin
from telethon.tl.types import ChannelParticipantsSearch
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
phone_number = '+528132341246'
channel = '@pruebastienda'
################################################
offset = 0
limit = 100
all_participants = []
users = []
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
client = TelegramClient("session", api_id, api_hash)
client.session.report_errors = False
client.start()

channel = client(ResolveUsernameRequest('@pruebastienda')) # Your channel username
user = client(ResolveUsernameRequest('jcolvera1991')) # Your channel admin username
