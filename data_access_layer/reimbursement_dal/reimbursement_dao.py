from data_access_layer.reimbursement_dal.reimbursment_dao_interface import ReimbursementDaoInterface
from utilities.connedtion_module.postgres_connection import connection
from entities.reimbursement import Reimbursement
from entities.employee import Employee
from exception.custom_exception import *


class ReimbursementDaoImp(ReimbursementDaoInterface):
    def __init__(self):
        # self.reimbursement = {'1' : "travel", '2': 'office supplies', '3': 'meals', '4': 'parking', '5': 'communication'}
        pass

    def create_request(self, reimbursement: Reimbursement) -> Reimbursement:
        info = reimbursement
        sql = 'insert into reimbursements values(default, %s, %s, %s, %s, %s) returning *'
        cursor = connection.cursor()
        cursor.execute(sql, (info.reimbursement_type, info.balance, info.comment, 'pending', reimbursement.employee_id))
        connection.commit()
        reimbursement_info = cursor.fetchone()
        return Reimbursement(*reimbursement_info)

    def get_reimbursement_by_request_id(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'select * from reimbursements where request_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.request_id])
        connection.commit()
        reimbursement_info = cursor.fetchone()
        if cursor.rowcount != 0:
            return Reimbursement(*reimbursement_info)
        else:
            raise BadAccountInfo("No account with that Id found")

    def get_all_requests_by_employee_id(self, employee: Employee) -> list:
        sql = 'select * from reimbursements where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [employee.employee_id])
        connection.commit()
        reimbursement_objs = cursor.fetchall()
        if reimbursement_objs == []:
            raise InfoNotFound('No Reimbursement record found')
        else:
            return [vars(Reimbursement(*info)) for info in reimbursement_objs]

    def update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        info = reimbursement
        sql = 'update reimbursements set reimbursement_type = %s, balance = %s, comment = %s, status = %s where request_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (info.reimbursement_type, info.balance, info.comment, info.status, info.request_id))
        connection.commit()
        return info

    def delete_reimbursement_request(self, reimbursement: Reimbursement) -> True:
        pass
