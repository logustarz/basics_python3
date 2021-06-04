import mysql.connector
  
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "loguRIO123"
  database = "stu"
)
  
mycursor = mydb.cursor()
sql = "INSERT INTO student (mark, name) VALUES (%s, %s)"
val = ("100","logu")
see = "SELECT * FROM student"
mycursor.execute(sql, val, see)
  
mydb.commit()
