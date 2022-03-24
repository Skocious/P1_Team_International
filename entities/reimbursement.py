class Reimbursement:
    def __init__(self, reimbursement_id, reimbursement_type, balance, comment, employee_id, status):
        self.reimbursement_id = reimbursement_id
        self.reimbursement_type = reimbursement_type
        self.balance = balance
        self.comment = comment
        self.employee_id = employee_id
        self.status = status
