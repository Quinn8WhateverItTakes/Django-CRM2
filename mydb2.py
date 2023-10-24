import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2@Madison',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE quinco")
print("all done")
