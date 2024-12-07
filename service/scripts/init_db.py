import mysql.connector
from env import env

print(env['DATABASE_USERNAME'])
print(env['DATABASE_PASSWORD'])
print(env['DATABASE_HOST'])
print(env['DATABASE_NAME'])
cnx = mysql.connector.connect(user=env['DATABASE_USERNAME'], password=env['DATABASE_PASSWORD'],
                              host=env['DATABASE_HOST'],
                              database=env['DATABASE_NAME'])

def init_db():
    cursor = cnx.cursor()

    query1 = ("CREATE TABLE IF NOT EXISTS tc_groups_channels (id INT AUTO_INCREMENT PRIMARY KEY, chat_name VARCHAR(20), chat_id BIGINT) ENGINE=InnoDB CHARSET=utf8")

    cursor.execute(query1)

    query2 = ("CREATE TABLE IF NOT EXISTS tc_params (id INT AUTO_INCREMENT PRIMARY KEY, param_name VARCHAR(100), param_data VARCHAR(100)) ENGINE=InnoDB CHARSET=utf8")

    cursor.execute(query2)

    query3 = ("CREATE TABLE IF NOT EXISTS tc_messages (id INT AUTO_INCREMENT PRIMARY KEY, chat_id INT, message_id INT, message_text VARCHAR(1000), datetime DATETIME, is_media BOOLEAN,FOREIGN KEY (chat_id) REFERENCES tc_groups_channels(id)) ENGINE=InnoDB CHARSET=utf8")

    cursor.execute(query3)

    cnx.commit()
    cnx.close()

if __name__ == "__main__":
    init_db()