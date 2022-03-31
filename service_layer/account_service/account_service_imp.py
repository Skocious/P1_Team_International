from service_layer.account_service.account_service_interface import AccountServiceInterface
from data_access_layer.account_dal.account_dao import AccountDao
from exception.custom_exception import *
from utilities.tester_module.tester import Tester
from entities.account import Account
from entities.employee import Employee
import re

class AccountServiceImp(AccountServiceInterface):

    def __init__(self):
        self.ADI = AccountDao()
        self.tester = Tester()

    def log_in(self, account: Account) -> Employee:
        if self.tester.login_id_tester(account.id_name) and self.tester.login_pw_tester(account.password):
            result = self.ADI.employee_login(account)
            if result is not None:
                return result
            else:
                raise UserNotFound("User not found type again")

    def log_out(self, employee: Employee) -> True:
        # logined employee Class = None
        pass


