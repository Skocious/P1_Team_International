from entities.employee import Employee
from interface.employee_int import EmployeeInt
from utilities.create_connection import connection


class EmployeeImp(EmployeeInt):

    def get_employee_by_id(self):
        sql = "select employee "
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        result = cursor.rowcount
        assert result
        print(result)





