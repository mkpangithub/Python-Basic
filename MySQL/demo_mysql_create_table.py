import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users(name VARCHAR(255), address VARCHAR(255))")