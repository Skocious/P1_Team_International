from data_access_layer.employee_dal.employee_dao import EmployeeDaoImp
from entities.employee import Employee

EDI = EmployeeDaoImp()

test_employee = Employee(-1, 'Test', 'Delete', -1)


def test_read_employee_info():
    result = EDI.read_employee_info(test_employee)
    assert result.employee_id == -1


def test_update_employee():
    result = EDI.read_employee_info(test_employee)
    assert result.employee_id == -1
