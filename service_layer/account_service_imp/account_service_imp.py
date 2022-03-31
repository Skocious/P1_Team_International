from entities.account import Account
from entities.employee import Employee
from service_layer.account_service_imp.account_service_interface import AccountServiceInterface
from data_access_layer.account_dal.account_dao import AccountDao
ADI = AccountDao()

# api_layer -> login info  -> Account(login info) ** here we are
# -> AccountServiceImp.log_in(Account(login info)) <- mocking and stubbing test
# -> AccountDao.employee_login(Account(login info))
# ->sql query -> DB -> employee_info -> api_layer -> employee(front_user)
class AccountServiceImp(AccountServiceInterface):
    def log_in(self, account: Account) -> Employee:
        if
         return ADI.employee_login(account)

# ADI.employee_login(account) = Employee(1, Madeleine, Albright, 1)
    def log_out(self, employee: Employee) -> True:
        pass
#
# def num():
#     a = 10
#     return a
#
# num_func = num()
# num_func1 = num()
# num_func2 = num()
#
# num_sum = num_func + num_func1
# print(num_sum)
#
# result = num() + num()
# print(result)
#
# num1 = 20
#
# num1