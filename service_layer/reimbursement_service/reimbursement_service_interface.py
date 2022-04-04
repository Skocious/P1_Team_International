from abc import ABC, abstractmethod
from entities.employee import Employee
from entities.reimbursement import Reimbursement


# 3. As an employee I want to file for reimbursements as needed.
# 4. As an employee I want to choose a reason for my reimbursement.
# 5. As an employee I want to add a comment about my reimbursement request.
# 6. As an employee I want to see the total amount of my reimbursement requests.
# 6. As an employee I can cancel a request.

class ReimbursementServiceInterface(ABC):

    @abstractmethod
    def create_reimbursement_request(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def get_all_reimbursement_by_employee_id(self, employee_id: int) -> list:
        pass

    @abstractmethod
    def cancel_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass
