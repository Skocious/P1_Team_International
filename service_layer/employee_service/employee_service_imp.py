from service_layer.employee_service.employee_service_int import EmployeeServiceInt
from data_access_layer.employee_dal.employee_dao import EmployeeDaoImp
from exception.custom_exception import *
from entities.employee import Employee


class EmployeeServiceImp(EmployeeServiceInt):
    def __init__(self):
        self.EDI = EmployeeDaoImp()

    def read_employee_info(self, employee: Employee) -> Employee:
        if type(employee.employee_id) == int:
            return self.EDI.read_employee_info(employee)
        else:
            raise IdNotFound("Id not found, please try again!")






    # def update_employee(self, employee: Employee) -> Employee:
    #     if employee.employee_id != employee.employee_id:
    #         raise InvalidEntry("You can not change your ID number!")
    #     elif employee.login_id != employee.login_id:
    #         raise InvalidEntry("You can not change your ID number!")
    #     elif len(employee.first_name) >= 21:
    #         raise InvalidEntry("First name should be less than 20 char.")
    #     elif len(employee.last_name) >= 21:
    #         raise InvalidEntry("Last name should be less than 20 char.")
    #     elif type(employee.first_name) != str:
    #         raise InvalidEntry("Name must be letters!")
    #     elif type(employee.last_name) != str:
    #         raise InvalidEntry("Name must be letters!")
    #     return self.employee_dao.update_employee(employee)
