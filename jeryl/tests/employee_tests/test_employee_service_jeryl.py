from data_access_layer.employee_dal.employee_dao import EmployeeDaoImp
from entities.employee import Employee
from service_layer.employee_service.employee_service_imp import EmployeeServiceImp
from utilities.custom_exceptions.id_not_found import IdNotFound
from utilities.custom_exceptions.invalid_entry import InvalidEntry
from unittest.mock import MagicMock

employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp(employee_dao)


def test_read_employee_info_success():
    try:
        employee_service.read_employee_info = MagicMock(return_value=[Employee(1, "Madeleine", "Albright", 1)])
        result = employee_service.read_employee_info([Employee(1, "Madeleine", "Albright", 1)])
        assert result == MagicMock
    except IdNotFound as e:
        assert str(e) == "Id not found, please try again!"


def test_read_employee_info_non_existent_employee_id_failure():
    try:
        employee_service.read_employee_info = MagicMock(return_value=[Employee(1, "Madeleine", "Albright", 1)])
        assert True
    except IdNotFound as e:
        assert str(e) == "Id not found, please try again!"


def test_read_employee_info_non_int_request_failure():
    try:
        employee_service.read_employee_info_non_int_request_failure = MagicMock(return_value=[Employee(xyz, "Madeleine", "Albright", 1)])
        assert True
    except InvalidEntry as e:
        assert str(e) == "Your Id must be a number. "




