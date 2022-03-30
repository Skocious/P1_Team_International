def create_request(self, reimbursement: Reimbursement, employee: Employee) -> Reimbursement:
    info = reimbursement
    sql = 'insert into test_reimbursement values(default, %s, %s, %s, %s, %s) returning *'
    cursor = connection.cursor()
    cursor.execute(sql, (info.reimbursement_type, info.balance, info.comment, 'pending', employee.employee_id))
    connection.commit()
    reimbursement_info = cursor.fetchone()
    return Reimbursement(*reimbursement_info)
