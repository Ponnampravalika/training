use task;
delimiter //
create function caluculatearea(length float,width float)
returns float 
deterministic
begin
    return length*width;
end //
delimiter ;
select caluculatearea(3.5,2.3) as area;
delimiter //
create function add(a int,b int)
delimiter //
create function caluculatearea(length float,width float)
returns float 
deterministic
begin
    return length*width;
end //
delimiter ;
select caluculatearea(3.5,2.3) as area;
delimiter //
create function add(a int,b int)
delimiter //
create function caluculatearea(length float,width float)
returns float 
deterministic
begin
    return length*width;
end //
delimiter ;
select caluculatearea(3.5,2.3) as area;
use task;
delimiter //
create function adds(a int,b int)
returns int 
deterministic
begin
    return a+b;
end //
delimiter ;
select adds(3.5,2.3) as addition;




    


    


    