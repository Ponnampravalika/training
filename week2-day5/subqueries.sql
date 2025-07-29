use task;
create table employes (
    name varchar(50) primary key,
    salary decimal(10,2)
);
insert into employes values('alice',50000.00),('bob',70000.00),('charlie',70000.00),('diana',60000.00);
select name,salary from employes where salary=(select max(salary) from employes);
create table departments(d_id int primary key,d_name varchar(100),location varchar(100));
insert into departments values(1,'hr','bangolore'),(2,'it','chennai'),(3,'finance','bamngalore');
select name from employes where d_id in(select d_id from departments where location='bangolore');
drop table employes;
select * from employes;
drop table departments;
use task;
-- Create the departments table
create table departments (d_id int primary key,d_name varchar(100),location varchar(100));
-- Insert data into departments
insert into departments values(1, 'hr', 'bangalore'),(2, 'it', 'chennai'),(3, 'finance', 'bangalore');
-- Create the employes table with a foreign key to departments
create table employes (name varchar(50) primary key,salary decimal(10,2),d_id int,
foreign key (d_id) references departments(d_id));
-- Insert data into employes
insert into employes values('alice', 50000.00, 1),('bob', 70000.00, 2),('charlie', 70000.00, 2),
('diana', 60000.00, 3);
-- Query: Get employees with the maximum salary
select name, salary from employes where salary = (select max(salary) from employes);
-- Query: Get employees who work in departments located in 'bangalore'
select name from employes where d_id in (select d_id from departments where location = 'bangalore');
-- subquery in from clause
select d_id,avg(salary) as avg_salary from 
(select d_id,salary from employes)as emp_sub group by d_id;
-- subquery in select clause
select name,(select d_name from departments where departments.d_id=employes.d_id)as 
dept_name from employes;
-- correlated subquery
select name,salary from employes e1 where salary>
(select avg(salary) from employes e2 where e1.d_id=e2.d_id);
-- using exists 
select exists (select 1 from employes e join departments d on e.d_id = d.d_id
    where d.location = 'chennai')as first_id;


