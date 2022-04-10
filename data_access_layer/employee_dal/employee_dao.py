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
