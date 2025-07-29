delimiter //
create procedure GetSalary(IN emp_name VARCHAR(50))
begin
    select name, salary from employes where name = emp_name;
end;
//
delimiter ;
call GetSalary('alice');
DELIMITER //

create procedure IncreaseSalary(in dept_id int, in pct decimal(5,2))
begin
    update employes
    set salary = salary + (salary * pct / 100)
    where d_id = dept_id;
end;
//
delimiter ;
call IncreaseSalary(2, 10);  -- increases salary by 10% for employees in department 2
delimiter //
create procedure GetTotalEmployees(out total int)
begin
    select count(*) into total from employes;
end //

delimiter ;
CALL GetTotalEmployees(@count);
SELECT @count;





