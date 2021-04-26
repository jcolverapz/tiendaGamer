
async def Bienvenido(arg):
    #await main()
    #global old_value
    #value = await client.get_admin_log(channel, limit=1, join= True)
    #print('id:' + str(value[0].id))
    
    if arg in all_participants:
        print("Si existe")
    else:
        all_participants.append(arg)
        #Enviar mensaje al Canal
       
        #array[:, 1:3] : Accede a todos los elementos del eje 0 pero con índice 1 y 2 en el eje 1.
        #var1 = a[3]
    # Añadir 2 elementos al final de un array:
    # a = np.array([1, 2, 3, 4, 5])
    #a = np.append(a, [6, 7])
    #y=  store()
    #z=  y.damenumero()
   # y.almacenar(value[0].id)
    #user = m[0].user_id 
    #await b.almacenar(value[0].id) 
    #await store(value) 
    #await asyncio.sleep(5)


#participants = client(GetParticipantsRequest(channel,ChannelParticipantsSearch(''),0,0,hash=0))
# participants = await client(GetParticipantsRequest(channel, ChannelParticipantsKicked,0,100,hash=0))
#all_participants = participants.users
#for u in participants.users:
    #lista1.append(u.username)
#print('main:' + str(lista1))
#      Cantidad de usuarios del canal
#inf = client(GetFullChannelRequest(channel))
#cant = inf.full_chat.participants_count
#print(cant)
#@client.on(events.ChatAction(chats=channel))
#m=[]
#m = client.get_admin_log(channel, join= True) 
#print(m[0])
#print (m.stringify())
#for i in m:
    #all_participants.append(u.id)
    #print(m[1].user_id)
#last_id=miId
#if miId > last_id:
#user_list=[0] 
#@client.on(events.register)
#@client.on(events.ChatAction)
#@client.on(events.CallbackQuery)


class store:
    def almacenar(self, num):
        self.store_value = num
        print(num)

    async def damenumero(self):
        
        return self.store_value

#for user in await client.iter_participants(channel, filter=ChannelParticipantsKicked):
#kicked_members =  await client.get_participants(channel, filter=ChannelParticipantsKicked)
#r= client.iter_participants('@pruebastienda', limit: float = None, *, search: str = '', filter: types.TypeChannelParticipantsFilter = None, aggressive: bool = False)
#telethon.client.chats._ParticipantsIter
#for u in r
#print(u)
#result = client(GetParticipantsRequest(InputChannel(channel_username.chats[0].id, channel_username.chats[0].access_hash), filter, num, 100, 0))
#admins = [InputUserSelf(), InputUser(user.users[0].id, user.users[0].access_hash)] # admins
#admins = [] # No need admins for join and leave and invite filters
#filter = None # All events
#param: (join, leave, invite, ban, unban, kick, unkick, promote, demote, info, settings, pinned, edit, delete)
#filter = ChannelAdminLogEventsFilter(False, False, False, True, False, False, False, False, False, False, False, False, False, False)
#param: (join, leave, invite, ban, unban, kick, unkick, promote, demote, info, 
#settings, pinned, edit, delete)
#filter = ChannelAdminLogEventActionParticipantJoin()
#user_list = client.channels.GetParticipantsRequest (entity=channel,filter=ChannelParticipantsRecent)
#participants = client(GetParticipantsRequest(channel,filter=filter, offset, limit, 0))
#participants = client(GetParticipantsRequest(channel, ChannelParticipantsSearch(''), offset, limit, 0))
#participants = client(GetAdminLogRequest(InputChannel(channel_use.chats[0].id,
#channel_use.chats[0].access_hash), '', 0, 0, 10, filter, admins))
#for _user in result.users:
#for _user in participants:
# with open(''.join(['users/', str(_user.id)]), 'w') as f:
# f.write(str(_user.id))
# #users.getUsers#0d91a548 id:Vector<InputUser> = Vector<User>#
#user_list = clients.get_participants(entity=channel,filter=ChannelParticipantsRecent)
#user_list= ChannelAdminLogEventActionParticipantJoin()
#user_list = client.get_Participants(entity=channel)
#for user in client.get_participants(channel, filter=ChannelParticipantsKicked):
#updater.dispatcher.add_handler(
# MessageHandler(Filters.status_update.new_chat_members, new_user)#)
    
    #all_participants.extend(participants.users)

    #for u in all_participants:
    #for u in client.iter_participants(channel):
       
      
        #all_participants[1] =  u.first_name
        
        #i += 1
       
#loop.run_until_complete(main())
#await main()



#      FIN      #



 #global channel
    #value = await client.get_admin_log(channel, limit=1, join= True)
    #a= await store()
    #a.almacenar(value[0].id)
    #p = client.get_participants(channel)
#account = await client.get_entity(target)
#if isinstance(account.status, UserStatusOffline):
#print( 'correctly Offline')
        
    #if (self.status, types.UserStatusOnline):
           #a= self.status
           
       # print(True)
#class UserUpdate(EventBuilder):
 
 #   if update.status(UpdateUserStatus='UserStatusOnline'):
  #      print(update.status)
   #     await Bienvenido()
   # The `datetime.datetime` until when the user should appear online.

#print(update)
  #user_list= event.user_id 
  #global i
  #i=i+1
   #global inf, cant
    #ncant = inf.full_chat.participants_count
    #if ncant> cant: 
    #await client.send_message(channel, 'Welcome !')

#   Todos los participantes
    #p = client.get_participants(channel)
    
########   Get all the users and print them
    #for u in client.iter_participants(channel, aggressive=True):
     
#Enviar mensaje al Canal
#client.send_message('@pruebastienda','Welcome')
#entity=client.get_entity(destination_user_username)
#client = TelegramClient('sessionname', api_id, api_hash) 

#await client.start()
#await client.run_until_disconnected()
#asyncio.get_event_loop().run_until_complete(main())
#client.run_until_disconnected()
 # client.add_event_handler(handler)

  
#return mievento
# await asyncio.sleep(5)

########       Show all user IDs in a chat
#for user in client.iter_participants('@pruebastienda'):
   

#########       Usuarios que han sido borrados
#channels.getParticipants#123e05e9 channel:InputChannel filter:ChannelParticipantsFilter offset:int limit:int hash:int = channels.ChannelParticipants
#for i in range(4):
  
#if  is not None:

 #info = client(GetFullChannelRequest(channel))
    #cant = info.full_chat.participants_count
