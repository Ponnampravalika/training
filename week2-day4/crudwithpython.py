import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="@@Aravind1$$",
    database="task"
)

cursor = con.cursor()
cursor.execute("create table if not exists employee (e_id int primary key,e_name varchar(100))")
cursor.execute("insert into employee (e_id, e_name) values (101, 'pravalika'), (102, 'krishna'), (105,'prasanna')")
cursor.execute("update employee set e_id=103 where e_id=105")
con.commit()
cursor.execute("select * from employee")
for row in cursor.fetchall():
    print(row)
cursor.execute("delete from employee where e_id=101")
con.close()

