from entities.employee import Employee
from utilities.custom_exceptions.id_not_found import IdNotFound
from william.implementation.employee_imp import EmployeeImp

employee_dao = EmployeeImp()


def test_get_employee_by_employee_id():
    test_employee = Employee(1, "Madeleine", "Albright")
    returned_employee = employee_dao.get_employee_by_id(test_employee)
    assert returned_employee.employee_id == 1
    print(returned_employee)


def test_get_employee_by_non_existent_employee_id():
    try:
        test_employee = Employee(100, "Test", "None")
        employee_dao.get_employee_by_id(test_employee)
        assert True
    except IdNotFound as e:
        assert str(e) == "Id not found"
    