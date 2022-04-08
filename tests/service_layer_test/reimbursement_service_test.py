from data_access_layer.reimbursement_dal.reimbursement_dao import ReimbursementDaoImp
from service_layer.reimbursement_service.reimbursement_service_imp import ReimbursementServiceImp
from entities.employee import Employee
from entities.reimbursement import Reimbursement
from exception.custom_exception import *
from unittest.mock import MagicMock, patch

RSI = ReimbursementServiceImp()
RDI = ReimbursementDaoImp()

test_reim = Reimbursement(1, 'travel', 100, 'text', 'Cancel', -1)
test_emp = Employee(-1, 'yeong', 'choi', -1)


def test_create_reimbursement_request():
    RDI.create_request = MagicMock(return_value=test_reim)
    result = RSI.create_reimbursement_request(test_reim)
    assert result.employee_id == -1


def test_create_reimbursement_request_negative_comment_length():
    test_wrong_comment = Reimbursement(-1, 'travel', 100, 'wrong' * 100, 'Cancel', -1)
    try:
        RSI.create_reimbursement_request(test_wrong_comment)
        assert False
    except TooLongComment as e:
        assert str(e) == 'Comment should be no longer than 100 characters'


def test_balance_over_reimbursement_request():
    test_reim_balance_over = Reimbursement(-1, 'travel', 1001, 'text', 'pending', -1)
    try:
        RSI.create_reimbursement_request(test_reim_balance_over)
        assert False
    except BalanceOver as e:
        assert str(e) == "Balance must be 1000 or less."


def test_create_reimbursement_request_negative_balance():
    test_wrong_balance = Reimbursement(-1, 'travel', -100, 'text', 'Cancel', -1)
    try:
        RSI.create_reimbursement_request(test_wrong_balance)
        assert False
    except BalanceUnder as e:
        assert str(e) == "Must be more than $1 per request"


def test_create_reimbursement_request_negative_str_balance():
    test_wrong_str_balance = Reimbursement(-1, 'travel', 'Not a number', 'text', 'Cancel', -1)
    try:
        RSI.create_reimbursement_request(test_wrong_str_balance)
        assert False
    except TypeError as e:
        assert str(e) == 'Balance must be numeric'


def test_get_all_reimbursement_by_employee_id():
    RDI.get_all_requests_by_employee_id = MagicMock(return_value=[test_reim])
    result = RSI.get_all_reimbursement_by_employee_id(test_emp.employee_id)
    assert result[0]['employee_id'] == -1


def test_cancel_reimbursement_request():
    RDI.update_reimbursement_request = MagicMock(return_value=test_reim)
    result = RSI.cancel_reimbursement_request(test_reim)
    assert result.status == "Cancel"

