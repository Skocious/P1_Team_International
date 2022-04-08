from data_access_layer.employee_dal.employee_dao import EmployeeDaoImp
from entities.employee import Employee
from service_layer.employee_service.employee_service_imp import EmployeeServiceImp
from unittest.mock import MagicMock, patch

employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp()

#
# def test_read_employee_info_success():
#     employee_dao.read_employee_info = MagicMock(return_value=Employee(1, "Madeleine", "Albright", 1))
#     result = employee_service.read_employee_info(Employee(1, "Madeleine", "Albright", 1))
#     assert result.employee_id == 1










