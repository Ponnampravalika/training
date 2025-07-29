use example;
create table employee(emp_id int primary key,name 
varchar(100),department varchar(20),salary int);
insert into employee values(1,'alice','hr',40000),(2,'bob','it',60000),
(3,'carol','finance',55000),(4,'david','it',72000);
with high_earners as(select name,salary from employee where salary>50000) 
select * from high_earners;
WITH it_employees AS (
  SELECT emp_id, name FROM employee WHERE department = 'it'
),
salaries AS (
  SELECT emp_id, salary FROM employee
)
SELECT it.name, s.salary
FROM it_employees it
JOIN salaries s ON it.emp_id = s.emp_id;
-- without using cte
SELECT e1.name, e2.salary
FROM employee e1
JOIN employee e2 ON e1.emp_id = e2.emp_id
WHERE e1.department = 'it';

