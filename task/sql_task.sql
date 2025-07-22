create database task;
use task;
CREATE TABLE students (
 id INT PRIMARY KEY,
 name VARCHAR(50),
 age INT,
 gender VARCHAR(10),
 marks INT,
 city VARCHAR(50)
);
 
INSERT INTO students (id, name, age, gender, marks, city) VALUES
(1, 'Alice', 20, 'Female', 85, 'Delhi'),
(2, 'Bob', 22, 'Male', 67, 'Mumbai'),
(3, 'Charlie', 23, 'Male', 92, 'Delhi'),
(4, 'Daisy', 21, 'Female', 74, 'Kolkata'),
(5, 'Evan', 20, 'Male', 89, 'Chennai'),
(6, 'Fiona', 22, 'Female', 95, 'Mumbai');
 
 
-- Only shows name and age
select name,age from students;
-- Unique city names
select distinct(city) from students;
-- Filters only male students
select * from students where gender='male';
-- Students scoring above 80
select * from students where marks>80;
-- Ages 20 to 22 inclusive
select * from students where age>20 and age<=22;
-- Students from Delhi
select * from students where city='delhi';
-- Names starting with A
select * from students where name like 'a%';
-- Sorted by marks descending
select * from students order by marks desc;
-- First 3 rows only
select * from students limit 3;
-- Total rows
select * from students;
-- Average marks
select avg(marks) from students;
-- Total marks
select sum(marks) from students;
-- Highest marks
select max(marks) from students;
-- Youngest student
select * from students where age<=20;
-- No. of unique cities
select count(distinct city) from students;
-- Male vs Female count
select count(*) from students where gender='male';
select count(*) from students where gender='female';
-- Avg marks per city
select avg(marks) from students group by city;
-- Top marks by gender
select max(marks) from students group by 'male';
select max(marks) from students group by 'female';
-- Cities with more than 1 student
select city, COUNT(*) AS student_count
FROM students
GROUP BY city
HAVING COUNT(*) > 1;

 
 