import data
from telethon import TelegramClient, events
import asyncio

params = data.find_all_params()
print(params)

client = TelegramClient('default_session', params['API_ID'], params['API_HASH'])
client.start()

@client.on(events.NewMessage())
async def event_handler(evento):   
    # data.save_one_message()
    print(evento)
    f = open("tmplog.txt", "a")
    f.write(str(evento))
    f.close()

async def infinity_loop():
    while True:
        pass
        await asyncio.sleep(1)

client.loop.run_until_complete(infinity_loop())