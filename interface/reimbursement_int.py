from abc import ABC, abstractmethod


class ReimbursementInt(ABC):

    @abstractmethod
    def create_request(self):
        pass

    @abstractmethod
    def get_request_by_request_id(self):
        pass

    @abstractmethod
    def get_request_by_employee_id(self):
        pass

    @abstractmethod
    def get_all_requests_by_employee_id(self):
        pass

    @abstractmethod
    def update_request_request(self):
        pass

    @abstractmethod
    def delete_request_request(self):
        pass
