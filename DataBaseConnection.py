pip install mysql-connector-python
import mysql.connector
con = mysql.connector.connect(user='root',password='Tannu',host='127.0.0.1',database='student_database')
print(con)

sqlQuery = "SELECT * FROM student_details"
ourCursor = con.cursor()
ourCursor.execute(sqlQuery)
allRows = ourCursor.fetchall()
for i in allRows:
    print(i)

sqlQuery = "INSERT INTO student_details(stud_id, name) VALUES(106,'anjal')"
ourCursor.execute(sqlQuery)
con.commit()
print(ourCursor.rowcount)    
