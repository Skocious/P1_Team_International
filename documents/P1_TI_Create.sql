

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


