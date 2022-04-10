from exception.custom_exception import IdNotFound
from service_layer.employee_service.employee_service_int import EmployeeServiceInt
from data_access_layer.employee_dal.employee_dao import EmployeeDaoImp
# from exception.custom_exception import *
from entities.employee import Employee


class EmployeeServiceImp(EmployeeServiceInt):
    def __init__(self):
        self.EDI = EmployeeDaoImp()

    def read_employee_info(self, employee: Employee) -> Employee:
        if type(employee.employee_id) == int:
            return self.EDI.read_employee_info(employee)
        else:
            raise IdNotFound("Id not found, please try again!")
