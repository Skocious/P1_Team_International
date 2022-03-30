from entities.employee import Employee
from entities.reimbursement import Reimbursement
from interface.reimbursement_int import ReimbursementInt
from utilities.create_connection import connection


#
# class Reimbursement:
#     def __init__(self, request_type, balance, comment, employee_id):
#         self.request_id = request_id
#         self.request_type = request_type
#         self.balance = balance
#         self.comment = comment
#         self.employee_id = employee_id
#         self.status = status

# Reimbursement(request_type, balance, comment)
# Reimbursement(1, 100, 'comment')
# ReimbursementInt
class ReimbursementImp:
    def __init__(self):
        self.employee = Employee(1, 'Madeleine', 'Albright')
        self.type = {'1': 'travel', '2': 'office supplies', '3': 'meals', '4': 'parking', '5': 'communication'}

    def create_request(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "insert into reimbursements values(default, %s, %s, %s, %s, %s) returning request_id"
        cursor = connection.cursor()
        cursor.execute(sql, (self.type[reimbursement.request_type], reimbursement.balance, reimbursement.comment,
                             self.employee.employee_id, 'pending'))
        connection.commit()
        result = cursor.fetchone()
        return result


test = ReimbursementImp()
test_emp = Reimbursement(1, 100, 'comment')
result = test.create_request(test_emp)



# print(test.type['1'])


# ctrl + /
#
# def get_request_by_request_id(self):
#     pass
# def get_all_request_by_request_id(self):
#     pass
#
# def get_request_by_employee_id(self):
#     pass
#
# def get_all_requests_by_employee_id(self):
#     pass
#
# def update_request_request(self):
#     pass
#
# def delete_request_request(self):
#     pass
