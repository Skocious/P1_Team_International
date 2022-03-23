

class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, password: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def employee_dictionary(self):
        return {
            "EmployeeID": self.employee_id,
            "Password": self.password
        }
