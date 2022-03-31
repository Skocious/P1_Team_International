from data_access_layer.employee_dal.employee_dao_interface import EmployeeDaoInterface
from utilities.connedtion_module.postgres_connection import connection
from entities.employee import Employee


class EmployeeDaoImp(EmployeeDaoInterface):

    def read_employee_info(self, employee: Employee) -> Employee:
        sql = "select * from employee where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee.employee_id])
        connection.commit()
        employee_info = cursor.fetchone()
        return Employee(*employee_info)

    # def update_employee(self, employee: Employee) -> Employee:
    #     sql = "update employee set first_name = %s last_name = %s where employee_id = %s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, (employee.first_name, employee.last_name, employee.employee_id))
    #     connection.commit()
    #     employee_info = cursor.fetchone()
    #     return Employee(*employee_info)




# test_employee = Employee(-1, 'Test', 'Delete', -1)

# EDI = EmployeeDaoImp()
#result = EDI.read_employee_info(test_employee)
# print(result.employee_id)

# result = EDI.read_employee_info(test_employee)
# print(result.employee_id)