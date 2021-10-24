import mysql.connector
from env import env

cnx = mysql.connector.connect(user=env['DATABASE_USERNAME'], password=env['DATABASE_PASSWORD'],
                              host=env['DATABASE_HOST'],
                              database=env['DATABASE_NAME'])

def init_db():
    cursor = cnx.cursor()

    query1 = ("CREATE TABLE IF NOT EXISTS tc_groups_channels (id INT AUTO_INCREMENT PRIMARY KEY, chat_name VARCHAR(20), chat_id INT)")

    cursor.execute(query1)

    query2 = ("CREATE TABLE IF NOT EXISTS tc_params (id INT AUTO_INCREMENT PRIMARY KEY, param_name VARCHAR(100), param_data VARCHAR(100))")

    cursor.execute(query2)

    query3 = ("CREATE TABLE IF NOT EXISTS tc_messages (id INT AUTO_INCREMENT PRIMARY KEY, chat_id INT, message_id INT, message_text VARCHAR(1000), datetime DATETIME)")

    cursor.execute(query3)

    cnx.commit()
    cnx.close()

if __name__ == "__main__":
    init_db()