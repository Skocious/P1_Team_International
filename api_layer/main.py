from data_access_layer.employee_dal.employee_dao import EmployeeDaoImp
from entities.employee import Employee

login_employee = None       # Employee class object

EDI = EmployeeDaoImp()
EDI.read_employee_info(login_employee)