from data_access_layer.reimbursement_dal.reimbursement_dao import reimbursementDaoImp
from service_layer.reimbursement_service.reimbursement_service_imp import reimbursementServiceImp
from entities.employee import Employee
from entities.reimbursement import Reimbursement
from utilities.tester_module import tester
from unittest.mock import MagicMock, patch

RSI = reimbursementServiceImp()
RDI = reimbursementDaoImp()
# def test_log_in():
#     ASI.ADI.employee_login = MagicMock(return_value=test_employee)
#     result = ASI.log_in(test_account)
#     assert result.login_id == 1

fake_txt = 'a' * 101
test_reim = Reimbursement(-1, 'travel', 100, 'text', 'pending', -1)
test_reim_comments_too_long = Reimbursement(-1, 'travel', 100, 'a'*101, 'pending', -1)
test_reim_balance_over_int= Reimbursement(-1, 'travel', 1001, 'text', 'pending', -1)
test_reim_non_numeric_request = Reimbursement(-1, 'travel', 'abcde', text', 'pending', -1)
test_reim_status_not_provided = Reimbursement(-1, 'travel', 100, 'text', 'status_not_provided', -1)
test_emp = Employee(-1_, 'yeong', 'choi', -1)

#def __init__(self, request_id, reimbursement_type, balance, comment, status, employee_id):

# Yeonghwan's POSITIVE TEST FIRST, THEN NEGATIVE TEST coding as example (updated 4/1)

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
        assert str(e) == 'Comment shoul be no longer than 100 characters'

####--------
#Jeryl's trial coding, patterned after Yeonghwan's NEGATIVE TEST coding from 4/ above:

def test_balance_over_int_reimbursement_request():
        try:
            RSI.create_reimbursement_request(test_reim_balance_over_int)
            assert False
        except BalanceOverInt as e:
            assert str(e) == "Balance must be 1000 or less."

def test_non_numeric_request_reimbursement_request():
    try:
        RSI.create_reimbursement_request(-1, 'travel', 'abcde', text', 'pending', -1)
        assert False
    except NonNumericRequest as e:
        assert str(e) == "Request amount must be numeric. Please enter dollar amount."

def test_status_not_provided_reimbursement_request():
    try:
        RSI.create_reimbursement_request(-1, 'travel', 100, 'text', 'status_not_provided', -1)
        assert False
    except StatusNotProvided as e:
        assert str(e) == "Please review your request and submit to obtain status."


###-------
#Jeryl's trial coding, based on Eric's NEGATIVE TEST coding from Project 0, and from Yeonghwan's POSITIVE Magic Mock 3/31:

@patch("utilities.custom_exceptions.invalid_entry.InvalidEntry")
def test_comments_too_long()
    try:
        mock.side.effect = CommentsTooLong("Comments must be 100 characters or less.")
        reimbursement_dao.create_entry(Reimbursement(1, travel, 100, 'a'*101, %s, 1))
        assert False
    except InvalidEntry as e:
        assert str(e) == "Comments must be 100 characters or less."


def test_comments_too_long_reimbursement_request():
    RDI.create_request = MagicMock(return_value(return_value=test_reim_comments_too_long))
    try:
        RSI.create_reimbursement_request(test_reim_comments_too_long)
        assert False
    except:
        assert str(e) == "Comments must be 100 characters or less."