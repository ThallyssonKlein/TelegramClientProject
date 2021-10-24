import data

params = data.find_all_params()

from telethon import TelegramClient, events

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
print(chats)

@client.on(events.NewMessage(chats=chats, incoming=True, func=content_filter))
async def event_handler(event):   
    # data.save_one_message() # TODO - Ultima coisa
    print(str(event.message.message))
    print(str(event.message.peer_id.channel_id))
    f = open("tmplog.txt", "a")
    f.write(str(event))
    f.close()

import asyncio

counter = 0
async def infinity_loop():
    while True:
        print("Running")
        await asyncio.sleep(1)
        counter += 1
        if counter == 60:
            chats = data.find_all_chats()
            params = data.find_all_params()
            counter = 0

client.loop.run_until_complete(infinity_loop())