from data_access_layer.reimbursement_dal.reimbursement_dao import reimbursementDaoImp
from utilities.connedtion_module.postgres_connection import connection
from entities.reimbursement import Reimbursement
from entities.employee import Employee

RDI = reimbursementDaoImp()

test_reim = Reimbursement(1, 1, 100, 'pending', 'travel', 'text')
test_emp = Employee(-1, 'yeong', 'choi', -1)


def test_create_request():

    result = RDI.create_request(test_reim, test_emp)
    assert result.employee_id == -1
    # assert result.reimbursement_type == 'travel'


def test_get_reimbursement_by_request_id():
    result = RDI.get_reimbursement_by_request_id(test_reim)
    assert result.employee_id == -1


def test_get_all_requests_by_employee_id():
    result = RDI.get_all_requests_by_employee_id(test_emp)
    assert result[0].employee_id == -1


def test_update_reimbursement_request():
    result = RDI.update_reimbursement_request(test_reim)
    assert result.request_id == 1
