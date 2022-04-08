from data_access_layer.account_dal.account_dao import AccountDao
from entities.account import Account

test_dao = AccountDao()


def test_employee_login():
    test_account = Account('test0', 'test00')
    result = test_dao.employee_login(test_account)
    assert result.employee_id == -1
