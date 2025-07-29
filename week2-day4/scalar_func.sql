-- scalar functions
select ucase("hello world") as upper_case_string;
select lcase("Hello World") as lower_case_string;
select mid("hello world",4,8) as sub_string;
select length("hello world") as length_of_string;
select round(1769.854,2) as round_value;
select now() as curretdatetime;
select format(1769.854,2) as format_number;
SELECT student_name, UPPER(student_name) AS name_uppercase FROM student;
select * from student;
select length(student_name) as length_name from student;


