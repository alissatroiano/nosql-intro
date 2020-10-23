import os
import datetime
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
        row = ("Bob", 30, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
        connection.commit()

finally:
    # Close the connection
    connection.close()