-- Table: employes
create database example;
use example;
create table  employes (name varchar(50) primary key,salary decimal(10,2),d_id INT);
-- Table: log_employes (for logging insert actions)
create table log_employes (name varchar(50),action varchar(20),
logged_at timestamp default current_timestamp);
-- after insert trigger
delimiter //
create trigger after_insert_employe
after insert on employes
for each row
begin
    insert into log_employes(name, action)
    values (new.name, 'insert');
end;
//
delimiter ;
insert employes values ('james', 55000.00, 2);
select * from log_employes;
select * from employes;
select * from log_employes;
-- before update trigger
delimiter //
create trigger before_salary_update
before update on employes
for each row
begin
    if new.salary < old.salary then
        signal sqlstate '45000'
        set message_text = 'Salary decrease is not allowed';
    end if;
end;
//
delimiter ;
-- Should fail
update employes set salary = 40000 where name = 'james';
-- Should pass
update employes set salary = 60000 where name = 'james';
select * from employes;
select * from log_employes;
-- after delete trigger
-- Table to log deletions
CREATE TABLE deleted_employees (
    name VARCHAR(50),
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
delimiter //
create trigger after_delete_employe
after delete on employes
for each row
begin
    insert into deleted_employees(name)values(old.name);
end
//
delimiter ;
delete from  employes where name = 'james';
select * from deleted_employees;
create table deleted_employees (name varchar(50),deleted_at timestamp default current_timestamp);








