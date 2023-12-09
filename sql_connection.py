import pymysql  
import creds

def sql_connector():
    connection = pymysql.connect(host=creds.sql_host,
                                user='root',
                                password=creds.sql_password,
                                database='data1',)
    mycursor = connection.cursor()
    return connection,mycursor







