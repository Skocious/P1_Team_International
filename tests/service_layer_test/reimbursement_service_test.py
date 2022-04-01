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


test_reim = Reimbursement(-1, 'travel', 100, 'text', 'pending', -1)
test_emp = Employee(-1, 'yeong', 'choi', -1)



def test_create_reimbursement_request():
    RDI.create_request = MagicMock(return_value=test_reim)
    result = RSI.create_reimbursement_request(test_reim)
    assert result.employee_id == -1


def test_get_all_reimbursement_by_employee_id():
    RDI.get_all_requests_by_employee_id = MagicMock(return_value=[test_reim])
    result = RSI.get_all_reimbursement_by_employee_id(test_emp.employee_id)
    assert result[0].employee_id == -1

def cancel_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
    reimbursement.status = 'Cancel'
    return self.RDI.get_all_requests_by_employee_id(reimbursement)
