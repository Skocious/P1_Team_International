from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDaoInterface(ABC):
    @abstractmethod
    def read_employee_info(self, employee: Employee) -> Employee:
        pass
