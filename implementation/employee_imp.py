from entities import employee
from entities.employee import Employee
from interface.employee_int import EmployeeInt
from utilities.create_connection import connection


class EmployeeImp(EmployeeInt):

    def get_employee_by_id(self, employee):
        sql = "select * from employee where employee_id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, [employee.employee_id])
        result = cursor.fetchone()
        print(result)
        return Employee(result[0], result[1], result[2])

   # def test123(self, login_id):
    #    sql = "select * from login where login_id = %s;"
     #   cursor = connection.cursor()
      #  cursor.execute(sql, [login_id])
       # result = cursor.fetchone()
       # return result

asd = EmployeeImp()

qwe = asd.get_employee_by_id(Employee(1, "Madeleine", "Albright"))

print(qwe)