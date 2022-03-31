from abc import ABC, abstractmethod
from entities.account import Account
from entities.employee import Employee


class AccountServiceInterface(ABC):

    @abstractmethod
    def log_in(self, account: Account) -> Employee:
        pass

    @abstractmethod
    def log_out(self, employee: Employee) -> True:
        pass