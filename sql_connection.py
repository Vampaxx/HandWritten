import pymysql  
import creds

def sql_connector():
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password=creds.sql_password,
                                database='data1',)
    mycursor = connection.cursor()
    return connection,mycursor







