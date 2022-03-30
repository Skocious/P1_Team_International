from service_layer.account_service_imp.account_service_interface import AccountServiceInterface
from data_access_layer.account_dal.account_dao import AccountDao
from entities.account import Account
from entities.employee import Employee


class AccountServiceImp(AccountServiceInterface):
    def __init__(self):
        self.account = None

    def log_in(self, account: Account) -> Employee:
        #if id_tester and pw_tester:
        return AccountDao.employee_login(self.account)
        
    def log_out(self, employee: Employee) -> True:

        pass
