from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDaoInterface(A
BC):
    @abstractmethod
    def read_employee_info(self, employee: Employee) -> Employee:
        pass

    #@abstractmethod
    #def update_employee(self, employee: Employee) -> Employee:
    #   pass



