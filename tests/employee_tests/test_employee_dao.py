from entities.employee import Employee
from william.implementation.employee_imp import EmployeeImp

employee_dao = EmployeeImp()


def test_get_employee_by_employee_id():
    test_employee = Employee(1, "Madeleine", "Albright")
    returned_employee = employee_dao.get_employee_by_id(test_employee)
    print(returned_employee.employee_id)
    assert returned_employee.employee_id == 1


def test_get_employee_by_non_existent_employee_id():
    test_employee = Employee(100, "Test", "None")
    returned_employee = employee_dao.get_employee_by_id(test_employee)
    assert returned_employee.employee_id != 100
