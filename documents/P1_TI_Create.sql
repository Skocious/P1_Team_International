

create table login(
	login_id SERIAL UNIQUE,
	login_name varchar(20) unique,
	pw varchar(20)
);

create table employee(
	employee_id SERIAL UNIQUE,
	employee_first_name varchar(20),  
	employee_last_name varchar(20),
	login_id int,
	constraint employee_foreign_key foreign key(login_id) references login(login_id) on delete cascade
);


create table reimbursements(
employee_id int, 
request_id serial primary key,
balance dec(15,2) not null check(balance<=1000.00),
status varchar(20),
category varchar(20),
"comment" varchar(100),
constraint reimbursements_foreign_key foreign key(employee_id) references employee(employee_id) on delete cascade  

);

insert into login values(-1), (1), (2), (3), (4);
insert into employee values(-1, 'Test', 'Delete', -1);
insert into employee values(1, 'Madeleine', 'Albright', 1);
insert into employee values(2, 'Margaret', 'Thatcher', 2);
insert into employee values(3, 'Martin', 'King', 3);
insert into employee values(4, 'Mahatma', 'Ghandi', 4);



