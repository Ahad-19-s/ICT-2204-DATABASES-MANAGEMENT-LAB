create database university ;
use university ;



CREATE TABLE department (
    dept_name VARCHAR(20),
    building VARCHAR(15),
    budget NUMERIC(12 , 2 ) CHECK (budget > 0)
);

INSERT INTO department (dept_name, building, budget)  
VALUES  
    ('CSE', 'CSE and GEO', 500000.00),  
    ('IIT', 'IIT and Math', 400000.00),  
    ('Statistics', 'IIT and Math', 600000.00),  
    ('Physics', 'Physics', 300000.00);

SELECT* FROM department;





CREATE TABLE instructor (
    ID VARCHAR(20),
    name VARCHAR(20) NOT NULL,
    dept_name VARCHAR(20),
    salary NUMERIC(8 , 2 )
   
   
);

INSERT INTO instructor (ID, name, dept_name, salary)  
VALUES  
    ('CSE-1201', 'Rashidul Hasan', 'CSE', 92000),  
    ('IIT-1202', 'Omar Faruk', 'IIT', 60000),  
    ('Math-1203', 'Supto Kundu', 'Math', 110000),  
    ('Physics-1204', 'Humaon Kabir', 'Physics', 80000),  
    ('CSE-1205', 'Naim Hossain', 'CSE', 45000);
    









CREATE TABLE student (
    ID          VARCHAR(5), 
    name        VARCHAR(20) NOT NULL, 
    dept_name   VARCHAR(20), 
    tot_cred    NUMERIC(3,0) CHECK (tot_cred >= 0)
   
   
);

INSERT INTO student (ID, name, dept_name, tot_cred)  
VALUES  
    ('1099', 'Milon', 'CSE', 180),  
    ('1029', 'Omar', 'IIT', 170),  
    ('1030', 'Supto', 'Math', 180),  
    ('1033', 'Kabir', 'Physics', 180),  
    ('1043', 'Naim', 'CSE', 190);
    
select* from student;


set sql_safe_updates = 0;
update student
set dept_name='Statistics' where id= '1099';
select* from student;




alter table department
add column feculty_name varchar(20) after building;

select* from department;



delete  from department
where dept_name='Statistics';




select name from instructor
where salary > 90000 and salary <=100000 order by name desc;














