from env import env

import mysql.connector

cnx = mysql.connector.connect(user=env['DATABASE_USERNAME'], password=env['DATABASE_PASSWORD'],
                              host=env['DATABASE_HOST'],
                              database=env['DATABASE_NAME'])
if __name__ == "__main__":
    cursor = cnx.cursor()
    
    query1 = ("INSERT INTO tc_groups_channels(chat_name, chat_id) VALUES ('Criptomaníacos', %s)")

    cursor.execute(query1, (env['SAMPLE_CHAT_ID'],))

    cnx.commit()
    cnx.close()