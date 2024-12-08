import data

params = data.find_all_params()
print(params)
content_filter_v = params.get('CONTENT_FILTER')

from telethon import TelegramClient, events

async def content_filter(event):
    print('content_filter')
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
print(chats)
client = TelegramClient('default_session', params['API_ID'], params['API_HASH'])

from os.path import basename

import pytz

def format_date(date):
	old_timezone = pytz.timezone()
	new_timezone = pytz.timezone("America/Araguaiana")
	
	localized_timestamp = old_timezone.localize(date)
	new_localized_timestamp = localized_timestamp.astimezone(new_timezone)
	
	return new_localized_timestamp

@client.on(events.NewMessage(chats=chats, incoming=True, func=content_filter))
async def event_handler(event):
    print('message received')
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
        data.save_one_message(channel_id_on_database, event.message.id, str(event.message.message), event.message.date, False)
    
    params = data.find_all_params()
    chats, chat_ids = data.find_all_chats()

import asyncio

async def main():
    await client.start()
    print("Client started")
    await client.run_until_disconnected()


asyncio.run(main())