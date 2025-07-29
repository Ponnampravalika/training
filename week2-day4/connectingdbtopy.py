import mysql.connector
con=mysql.connector.connect(host="localhost",port=3306,user="root",password="@@Aravind1$$",database="task")
cursor=con.cursor()
cursor.execute("select * from task.student")

for row in cursor:
    print(row)
con.close()
