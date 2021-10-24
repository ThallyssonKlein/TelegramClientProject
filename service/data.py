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

    for row in records:
        chats.append(row[2])

    cursor.close()

    return chats

def save_one_message(chat_id, message_id, message_text, datetime):
    cursor = cnx.cursor()

    query = ("INSERT INTO tc_messages (chat_id, message_id, message_text, datetime) VALUES (%s, %s, %s, %s)")

    cursor.execute(query, (chat_id, message_id, message_text, datetime))

    cnx.commit()

    cursor.close()