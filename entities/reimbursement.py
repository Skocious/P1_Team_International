class Reimbursement:
    def __init__(self, request_id, request_type, balance, comment, employee_id, status):
        self.request_id = request_id
        self.request_type = request_type
        self.balance = balance
        self.comment = comment
        self.employee_id = employee_id
        self.status = status
