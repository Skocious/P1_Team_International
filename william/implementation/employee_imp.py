from entities.employee import Employee
from interface.employee_int import EmployeeInt
from utilities.create_connection import connection


class EmployeeImp(EmployeeInt):

    def get_employee_by_id(self, employee: Employee):
        sql = "select * from employee where employee_id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, [employee.employee_id])
        result = cursor.fetchone()
        if result is not None:
            return Employee(result[0], result[1], result[2])
#       else:
            assert True
#
# test = EmployeeImp()
# result = test.get_employee_by_id(Employee(1, "Madeleine", "Albright"))
