import mysql.connector
from mysql.connector.cursor import MySQLCursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)