from abc import ABC, abstractmethod


class reimbursement_int(ABC):

    @abstractmethod
    def create_reimbursement(self):
        pass

    @abstractmethod
    def get_reimbursement_by_request_id(self):
        pass

    @abstractmethod
    def get_reimbursement_by_employee_id(self):
        pass

    @abstractmethod
    def get_all_reimbursements_by_employee_id(self):
        pass

    @abstractmethod
    def update_reimbursement_request(self):
        pass

    @abstractmethod
    def delete_reimbursement_request(self):
        pass
