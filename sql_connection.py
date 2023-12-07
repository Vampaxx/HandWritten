import pymysql  

def sql_connector():
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='arjun9400508669',
                                database='data1',)
    mycursor = connection.cursor()
    return connection,mycursor







