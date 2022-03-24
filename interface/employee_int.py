from abc import ABC, abstractmethod


class EmployeeInt(ABC):

    @abstractmethod
    def get_employee_by_id(self):
        pass
