CREATE TABLE student(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(40),
    email VARCHAR(20) UNIQUE
);
CREATE TABLE courses(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(20),
    course_length_weeks INT,
    credits INT
);
CREATE TABLE enrollments (
    course_id INT,
    student_id INT,
    grade INT,
    completion_status BOOLEAN,
    PRIMARY KEY(course_id, student_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY(student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);
-- Students
INSERT INTO student VALUES 
(101, 'Aravind','ab@gmail.com'),
(102, 'Sneha','xy@gmail.com'),
(103, 'Ravi','mn@gmail.com');

-- Courses
INSERT INTO courses VALUES 
(1, 'Data Structures',2,50),
(2, 'DBMS',4,70);

-- Enrollments
INSERT INTO enrollments VALUES 
(1, 101, 85, TRUE),
(1, 102, 75, TRUE),
(2, 103, 92, TRUE),
(2, 101, NULL, FALSE);
delete from student where student_id=103;
update student set course_id=3 where course_id=2;
select * from enrollments;
update enrollments set grade=95 where course_id=1;
select * from enrollments;
