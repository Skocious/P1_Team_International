from abc import ABC, abstractmethod
from entities.employee import Employee
from entities.reimbursement import Reimbursement


class reimbursementDaoInterface(ABC):

    @abstractmethod
    def create_request(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def get_reimbursement_by_request_id(self, request_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all_requests_by_employee_id(self, employee_id: int) -> list:
        pass

    @abstractmethod
    def update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def delete_reimbursement_request(self, reimbursement: Reimbursement) -> True:
        pass


