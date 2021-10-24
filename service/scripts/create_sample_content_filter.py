from env import env

import mysql.connector

cnx = mysql.connector.connect(user=env['DATABASE_USERNAME'], password=env['DATABASE_PASSWORD'],
                              host=env['DATABASE_HOST'],
                              database=env['DATABASE_NAME'])
if __name__ == "__main__":
    cursor = cnx.cursor()
    
    query1 = ("INSERT INTO tc_params(param_name, param_data) VALUES ('CONTENT_FILTER', %s)")

    cursor.execute(query1, ('haha,kkk',))

    cnx.commit()
    cnx.close()