use example;
create table sales(emp_id int primary key,department char,amount int,sale_date date);
insert into sales values(1,'a',100,'2024-01-01'),(2,'a',200,'2024-01-02'),
(3,'b',300,'2024-01-01'),(4,'a',150,'2024-01-03');
select * from sales;
select emp_id,department,amount, row_number() over(partition by department order by amount desc)
as row_num from sales;
select emp_id,department,amount, row_number() over() as row_num from sales;
select emp_id,department,amount, rank() over(partition by department order by amount desc)
as ranks from sales;
select emp_id,department,amount, dense_rank() over(partition by department order by amount desc)
as dense_ranks from sales;
select emp_id,department,amount, rank() over()
as ranks from sales;
select emp_id,department,amount, dense_rank() over()
as dense_ranks from sales;
select emp_id,department,amount,RANK() OVER (ORDER BY amount DESC)as ranks from sales;
select emp_id,department,amount,dense_rank() OVER (ORDER BY amount DESC)as dense_ranks from sales;
insert into sales values(5,'b',300,'2024-01-02');
SELECT emp_id, department, amount,SUM(amount) OVER (PARTITION BY department) AS dept_total
FROM sales;
SELECT emp_id, amount,
     LAG(amount) OVER (ORDER BY sale_date) AS prev_amount,
     LEAD(amount) OVER (ORDER BY sale_date) AS next_amount
FROM sales;
 SELECT emp_id, amount,
     LAG(amount) OVER (ORDER BY sale_date) AS prev_amount,
     LEAD(amount) OVER (ORDER BY sale_date) AS next_amount
FROM sales;
 
SELECT emp_id, department, amount,
     FIRST_VALUE(amount) OVER (PARTITION BY department ORDER BY sale_date) AS first_sale,
     LAST_VALUE(amount) OVER (PARTITION BY department ORDER BY sale_date 
     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_sale
FROM sales;
SELECT emp_id, amount,
     LAG(amount) OVER (ORDER BY sale_date) AS prev_amount,
     LEAD(amount) OVER (ORDER BY sale_date) AS next_amount
FROM sales;
 
SELECT emp_id, department, amount,
     FIRST_VALUE(amount) OVER () AS first_sale,
     LAST_VALUE(amount) OVER () AS last_sale
FROM sales;
select emp_id,amount,ntile(2) over(order by amount) as bucket from sales;
select emp_id,amount,ntile(3) over(order by amount) as bucket from sales;
select emp_id,amount,ntile(4) over(order by amount) as bucket from sales;
select * from sales;
alter table sales add column name varchar(50); 
UPDATE sales SET name = 'Alice' WHERE emp_id = 1;
UPDATE sales SET name = 'bob' WHERE emp_id = 2;
UPDATE sales SET name = 'carol' WHERE emp_id = 3;
UPDATE sales SET name = 'david' WHERE emp_id = 4;
UPDATE sales SET name = 'dhoni' WHERE emp_id = 5;
delete from sales where emp_id=null;

 
 


