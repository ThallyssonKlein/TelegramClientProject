import data

params = data.find_all_params()
content_filter_v = params.get('CONTENT_FILTER')

from telethon import TelegramClient, events

client = TelegramClient('default_session', params['API_ID'], params['API_HASH'])
client.start()

async def content_filter(event):
    global content_filter_v
    if content_filter_v:
        separated_content_filter = content_filter_v.split(',')
        for term in separated_content_filter:
            if term in event.message.message:
                return True
        
        return False
    else:
        return True

chats, chat_ids = data.find_all_chats()

from os.path import basename

@client.on(events.NewMessage(chats=chats, incoming=True, func=content_filter))
async def event_handler(event):
    global params
    global chats
    global chat_ids

    channel_id = event.message.peer_id.channel_id
    channel_id_on_database = chat_ids[chats.index(channel_id)]
    if event.message.photo:
        path = await client.download_media(event.message.media, params['MEDIA_DIR'])
        filename = basename(path)
        print('File name: {}'.format(filename))
        data.save_one_message(channel_id_on_database, event.message.id, filename, event.message.date, True)
    else:  
        data.save_one_message(channel_id_on_database, event.message.id, event.message.message, event.message.date, False)
    print(str(event.message.date))
    
    params = data.find_all_params()
    chats, chat_ids = data.find_all_chats()

import asyncio

async def infinity_loop():
    while True:
        print("Running")
        await asyncio.sleep(1)

client.loop.run_until_complete(infinity_loop())