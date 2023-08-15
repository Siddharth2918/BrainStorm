create database brainstorm;
use brainstorm;
create table users(user_id int primary key auto_increment, username varchar(50), user_password varchar(20), email_id varchar(50), first_name varchar(50), last_name varchar(50));
insert into users values
    (1, "soumil123", "soumil123", "soumilpuri23@gmail.com", "Soumil", "Puri");
create table soumil123(date varchar(10), gender varchar(10), age int, hypertension varchar(10), heartdisease varchar(10), evermarried varchar(10), 
	worktype varchar(10), recidencetype varchar(10), glucoselevel float, bmi float, smokingstatus varchar(20), prediction int);
