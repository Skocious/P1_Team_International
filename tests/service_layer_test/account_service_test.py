from data_access_layer.account_dal.account_dao import AccountDao
from entities.account import Account
from entities.employee import Employee
from service_layer.account_service.account_service_imp import AccountServiceImp
from unittest.mock import MagicMock, patch


ADI = AccountDao()
ASI = AccountServiceImp()
test_account = Account('test1', 'test11')
test_employee = Employee(1, 'Madeleine', 'Albright', 1)

def test_log_in():
    ASI.ADI.employee_login = MagicMock(return_value=test_employee)
    result = ASI.log_in(test_account)
    assert result.login_id == 1

