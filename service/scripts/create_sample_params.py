from env import env

import mysql.connector

cnx = mysql.connector.connect(user=env['DATABASE_USERNAME'], password=env['DATABASE_PASSWORD'],
                              host=env['DATABASE_HOST'],
                              database=env['DATABASE_NAME'])
if __name__ == "__main__":
    cursor = cnx.cursor()
    
    query1 = ("INSERT INTO tc_params(param_name, param_data) VALUES ('API_ID', %s)")
    query2 = ("INSERT INTO tc_params(param_name, param_data) VALUES ('API_HASH', %s)")
    query3 = ("INSERT INTO tc_params(param_name, param_data) VALUES ('MEDIA_DIR', %s)")
    query4 = ("INSERT INTO tc_params(param_name, param_data) VALUES ('APP_LOG', %s)")

    cursor.execute(query1, (env['API_ID'],))
    cursor.execute(query2, (env['API_HASH'],))
    cursor.execute(query3, (env['MEDIA_DIR'],))
    cursor.execute(query4, (env['APP_LOG'],))

    cnx.commit()
    cnx.close()