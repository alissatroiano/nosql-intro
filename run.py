import os
import pymysql

# Get username from Gitpod workspace

username = os.getenv('alissatroiano')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
try:
    # Run a query here
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection
    connection.close()    