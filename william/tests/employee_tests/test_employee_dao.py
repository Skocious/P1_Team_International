from entities.employee import Employee
from william.implementation.employee_imp import EmployeeImp

employee_dao = EmployeeImp()


def test_get_employee_by_employee_id():
    test_employee = Employee(10, "Barry", "White")
    returned_employee = employee_dao.get_employee_by_id(test_employee)
    assert returned_employee.employee_id == 10
    print(returned_employee)


def test_get_employee_by_non_existent_employee_id():
    test_employee = Employee(100, "Test", "None")
    returned_employee = employee_dao.get_employee_by_id(test_employee)
    assert returned_employee.employee_id == 100
    print(returned_employee)

    