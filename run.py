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
        rows = [("Bob", 30, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 13:12:45"),
                ("Fred", 100, "1920-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES(%s, %s, %s);", rows)
        connection.commit()

finally:
    # Close the connection
    connection.close()