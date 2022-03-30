from abc import ABC, abstractmethod

from data_access_layer.employee_dal.employee_dao import EmployeeDaoImp
from entities.employee import Employee


class EmployeeServiceInt(ABC):

    def __init__(self, employee_dao: EmployeeDaoImp):
        self.employee_dao: EmployeeDaoImp = employee_dao

    @abstractmethod
    def read_employee_info(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> Employee:
        pass
