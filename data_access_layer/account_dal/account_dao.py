from abc import ABC
from data_access_layer.account_dal.account_dao_interface import AccountDaoInterface
from exception.custom_exception import *
from utilities.connedtion_module.postgres_connection import connection
from entities.employee import Employee
from entities.account import Account


# CRUD
class AccountDao(AccountDaoInterface, ABC):

    def employee_login(self, account: Account) -> Employee:
        sql = "select * from employee where login_id = (select login_id from login where " \
              "login_name = %s and pw = %s);"
        cursor = connection.cursor()
        cursor.execute(sql, (account.id_name, account.password))
        connection.commit()
        employee_info = cursor.fetchone()
        if cursor.rowcount != 0:
            return Employee(*employee_info)
        else:
            raise BadAccountInfo("No account with that Id found")

    def create_account(self, employee: Employee, account: Account) -> True:
        sql_one = "insert into test_login values(default, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql_one, (account.id_name, account.password))
        if cursor.rowcount != 1:
            connection.rollback()
            raise BadAccountInfo("Sender account Id not found")

        sql_two = "insert into test_employee values(default, %s, %s)"
        cursor.execute(sql_two, (employee.first_name, employee.last_name))
        if cursor.rowcount != 1:
            connection.rollback()
            raise BadAccountInfo("Receiver account Id not found")
        connection.commit()
        return True

    def delete_account(self, employee: Employee) -> True:
        sql = "delete from test_login where login_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee.employee_id])
        connection.commit()
        if cursor.rowcount != 1:
            connection.rollback()
            raise BadAccountInfo("Receiver account Id not found")

        sql2 = "delete from test_employee where login_id = %s"
        cursor.execute(sql2, [employee.employee_id])
        if cursor.rowcount != 1:
            connection.rollback()
            raise BadAccountInfo("Sender account Id not found")
        connection.commit()
        return True
