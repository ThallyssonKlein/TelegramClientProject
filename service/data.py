import mysql.connector
from env import env

cnx = mysql.connector.connect(user=env['DATABASE_USERNAME'], password=env['DATABASE_PASSWORD'],
                              host=env['DATABASE_HOST'],
                              database=env['DATABASE_NAME'])

def find_all_params():
    cursor = cnx.cursor()

    query = ("SELECT * FROM tc_params")

    cursor.execute(query)

    params = {}

    records = cursor.fetchall()

    for row in records:
        params[row[1]] = row[2]

    cursor.close()

    return params

def find_all_chats():
    cursor = cnx.cursor()

    query = ("SELECT * FROM tc_groups_channels")

    cursor.execute(query)

    records = cursor.fetchall()

    chats = []
    chat_ids = []

    for row in records:
        chats.append(row[2])
        chat_ids.append(row[0])

    cursor.close()

    return chats, chat_ids

def remove_emoji(string):
    return string.replace('🟢', '').replace('🟠', '')

def save_one_message(chat_id, message_id, message_text, datetime, isMedia):
    cursor = cnx.cursor()

    if isMedia:
        query = ("INSERT INTO tc_messages (chat_id, message_id, message_text, datetime, is_media) VALUES (%s, %s, %s, %s, 1)")
        cursor.execute(query, (chat_id, message_id, message_text, datetime))
    else:
        print(remove_emoji(message_text))
        query = ("INSERT INTO tc_messages (chat_id, message_id, message_text, datetime, is_media) VALUES (%s, %s, %s, %s, 2)")
        cursor.execute(query, (chat_id, message_id, remove_emoji(message_text), datetime))

    cnx.commit()

    cursor.close()