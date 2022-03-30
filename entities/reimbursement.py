class Reimbursement:
    def __init__(self, request_id, reimbursement_type, balance, comment, status, employee_id):
        self.request_id = request_id
        self.reimbursement_type = reimbursement_type
        self.balance = balance
        self.comment = comment
        self.status = status
        self.employee_id = employee_id

# - 1. travel - 2. office supplies -  3. meals - 4. parking - communications -

# reimbursement_type varchar(20) not null,
# 	balance dec(15,2) check(balance >= 1),
# 	comment varchar(20) not null,
# 	status varchar(20) not null,
# 	employee_id int,
# 	constraint test_reimbursement_foreign_key foreign key(employee_id) references test_employee(employee_id) on delete cascade
