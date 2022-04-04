from abc import ABC, abstractmethod


class reimbursementSerInt(ABC):

    @abstractmethod
    def service_create_request(self):
        pass

    @abstractmethod
    def service_get_reimbursement_by_request_id(self):
        pass

    @abstractmethod
    def service_get_all_requests_by_employee_id(self):
        pass

    @abstractmethod
    def service_update_reimbursement_request(self):
        pass

    @abstractmethod
    def service_delete_reimbursement_request(self):
        pass


