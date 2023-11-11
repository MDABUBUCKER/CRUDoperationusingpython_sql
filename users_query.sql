create database python_with_sql;  -- creating database 

use python_with_sql; -- we using taht database

/* then create table name and 
enter column name datatype */

create table users(
ID integer auto_increment primary key,
NAME varchar(30),
AGE integer,
COURSE varchar(20));

desc users; -- showing structure

select * from users; #showing table values

alter table users rename column NAME to S_NAME; #query rename column name

alter table users modify COURSE varchar(20) after AGE; #using for change column orders

insert into users(S_NAME,AGE,COURSE)
value("ALEX",22,"MSC");
# then insert value of table

select age,course from users; #query used see particular column

select age,course from users where s_name = "kevin"; 

