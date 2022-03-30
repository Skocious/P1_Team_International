from abc import ABC, abstractmethod
from entities.employee import Employee
from entities.account import Account


class AccountDaoInterface(ABC):

    @abstractmethod
    def employee_login(self, account: Account) -> Employee:
        pass

    # @abstractmethod
    # def create_account(self, account: Account) -> True:
    #     pass
    #
    # @abstractmethod
    # def update_account(self, employee: Employee) -> True:
    #     pass
    #
    # @abstractmethod
    # def delete_account(self, employee: Employee) -> True:
    #     pass
