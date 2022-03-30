class Reimbursement:
    def __init__(self, request_id, reimbursement_type, balance, comment, status, employee_id):
        self.request_id = request_id
        self.reimbursement_type = reimbursement_type
        self.balance = balance
        self.comment = comment
        self.status = status
        self.employee_id = employee_id
