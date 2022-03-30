from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDaoInterface(ABC):

    @abstractmethod
    def read_employee_info(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> Employee:
        pass

#
# Y_E1. As an employee I want to be able to log in through a webpage. (employee_login)
# Y_E2. As an employee I want to be able to log out through a webpage. (employee_logout)

# J_R3. As an employee I want to file for reimbursements as needed. (create_request)
# W_R4. As an employee I can choose an associated category my reimbursement will fall under.
# [Travel, Supplies, Meals, Parking, Communications] (create_request)
# W_R5. As  an employee I can cancel a reimbursement request. (delete_request)
# Z_R6. As an employee I can see the total amount of money I requested (get_request_by_employee_id)
# J_R7. Employees must be given a visual notice upon a successful or failed reimbursement request (create_request) (notification of successful submission)
# Z_R8. As an employee I want to be able to see all of my reimbursement request (get_all_requests_by_employee_id)


# crud
