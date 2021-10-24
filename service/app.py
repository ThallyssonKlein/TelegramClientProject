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

chats, chat_ids = data.find_all_chats()

@client.on(events.NewMessage(chats=chats, incoming=True, func=content_filter))
async def event_handler(event):
    channel_id = event.message.peer_id.channel_id
    channel_id_on_database = chat_ids[chats.index(channel_id)]   
    data.save_one_message(channel_id_on_database, event.message.id, event.message.message, event.message.date)
    print(str(event.message.date))
    f = open("tmplog.txt", "a")
    f.write(str(event))
    f.close()

import asyncio

async def infinity_loop():
    while True:
        print("Running")
        await asyncio.sleep(1)

client.loop.run_until_complete(infinity_loop())