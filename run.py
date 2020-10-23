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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        for row in cursor:
            print(row)

finally:
    # Close the connection
    connection.close()