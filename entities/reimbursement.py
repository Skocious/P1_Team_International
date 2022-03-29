class Reimbursement:
    def __init__(self, request_type, balance, comment):
        self.request_id = None
        self.request_type = request_type
        self.balance = balance
        self.comment = comment
        self.employee_id = None
        self.status = None
