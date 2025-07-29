use example;
select * from employee;
-- case in 
select name,salary, case
when salary>=70000 then 'high'
when salary between 50000 and 69999 then 'mediun'
else 'low'
end as salary_level
from employee;
-- case in order by
select * from employee order by case department 
when 'it' then 1
when 'hr' then 2
else 3
end;
-- case in update
update employee set salary = case 
when department='it' then salary+5000
when department='hr' then salary+2000
else salary
end;


