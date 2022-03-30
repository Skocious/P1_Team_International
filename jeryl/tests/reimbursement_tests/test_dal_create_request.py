
from implementation.reimbursement_imp import ReimbursementImp
from entities.reimbursement import Reimbursement

reimbursement_imp = ReimbursementImp()

def test_create_request_success():
    reimbursement = Reimbursement(request_type="travel", balance=10.00, comment= "Trial Exercise")
    result = reimbursement_imp.create_request(reimbursement)
    assert result.request_id == 1

def test_create_request_failure():
    reimbursement = Reimbursement(request_type="travel", balance=10.00, comment="Trial Exercise")
    result = reimbursement_imp.create_request(reimbursement)
    if result is None:
        # assert custom_exception: "Reimbursement system not available at this time"
        assert False
    else:
        return result.request_id










