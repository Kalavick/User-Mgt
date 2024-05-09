import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '0435'

)

#prepare cursor object
cursorObject = dataBase.cursor()

#crete a database
cursorObject.execute("CREATE DATABASE userDB")

#Testing to see if database was created
print("All Done!!")