import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="python3.8"
)


mycursor = mydb.cursor()

sql = "CREATE DATABASE pythontest"

mycursor.execute(sql)