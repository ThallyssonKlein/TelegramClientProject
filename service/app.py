import data

params = data.find_all_params()

client = TelegramClient('default_session', params['API_ID'], params['API_HASH'])
client.start()

async def content_filter(event):
    if params.get('CONTENT_FILTER'):
        if event.message.message == params['CONTENT_FILTER']:
            return True
        else:
            return False
    else:
        return True

chats = data.find_all_chats()

# TODO - é chats ou from_users?
# TODO- Fluxo de puxar chats e parametros de novo do banco

@client.on(events.NewMessage(chats=chats, incoming=True, func=content_filter ))
async def event_handler(evento):   
    # data.save_one_message() # TODO - Ultima coisa
    f = open("tmplog.txt", "a")
    f.write(str(event))
    f.close()

client.loop.run_until_complete(main())