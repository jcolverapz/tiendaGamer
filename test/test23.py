from telethon import TelegramClient, events
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputUser
from telethon.tl.types import ChannelAdminLogEventActionChangeAbout
from telethon.tl.types import ChannelAdminLogEventActionParticipantInvite
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoinByInvite
from telethon.tl.types import ChannelAdminLogEventActionParticipantJoin
from telethon.tl.types import ChannelAdminLogEventActionParticipantLeave
from telethon.tl.functions.channels import GetFullChannelRequest
api_id = 3409046
api_hash = '48ae9fbdf79edda291e1fa5796fc4665'
#phone_number = '+528132341246'
channel = '@pruebastienda'
################################################
client = TelegramClient('sessionname', api_id, api_hash) 
client.start()

def joined(self):
    print('joined')
    return isinstance(self.original.action,
                          ChannelAdminLogEventActionParticipantJoin)
        
def joined_invite(self):
    print('joined_invite')
    return isinstance(self.original.action,ChannelAdminLogEventActionParticipantInvite)

def joined_by_invite(self):
    return isinstance(self.original.action,
                          ChannelAdminLogEventActionParticipantJoinByInvite)

def left(self):
    print('left')
    return isinstance(self.original.action,
                          ChannelAdminLogEventActionParticipantLeave)

from telethon.tl.functions.channels import LeaveChannelRequest
    await client(LeaveChannelRequest(channel))

#ChatAction  events.ChatAction
#kicked_by
#get_user

@client.on(events.ChatAction)
# Welcome every new user
        await event.reply('Welcome!')
client.run_until_disconnected()