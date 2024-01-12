import os
import creds
import pymysql  


def sql_connector():
    connection = pymysql.connect(host=creds.sql_host,
                                user='root',
                                password=creds.sql_password,
                                database='data1',)
    mycursor = connection.cursor()
    return connection,mycursor


'''def sql_connector():
    db_url = 'mysql+pymysql://root:{password}@flask_db:3306/data1'
    print(db_url)

    if db_url:
        connection = pymysql.connect(db_url)
    else:
        # If DB_URL is not set, use default values
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='data1',
        )

    mycursor = connection.cursor()
    return connection, mycursor
'''






