



reimbursement_imp = ReimbursementImp()

def test_incorrect_request_type():
    request = (1,request_type = "miscellaneous", balance=10.00, comment= "Trial Exercise")
    result = reimbursement_imp.create_request(reimbursement)