from entities.employee_id import Employee_id
import utilities.custom_exceptions.invalid_entry
from entities.reimbursement import Reimbursement
from interface.reimbursement_int import ReimbursementInt
from utilities.create_connection import connection
from utilities.custom_exceptions.invalid_entry import InvalidEntry
from unittest.mock import MagicMock, patch

class ReimbursementDAOImp(ReimbursementDAOInterface)

#def __init__(self, request_id, reimbursement_type, balance, comment, status, employee_id):

fake_txt = 'a' * 101

@patch("utilities.custom_exceptions.invalid_entry.InvalidEntry")
def test_comments_too_long()
    try:
        mock.side.effect = CommentsTooLong("Comments must be 100 characters or less.")
        reimbursement_dao.create_entry(Reimbursement(1, travel, 100, 'a'*101, %s, 1))
        assert False
    except InvalidEntry as e:
        assert str(e) == "Comments must be 100 characters or less."


#employee_dao.read_employee_info = MagicMock(return_valmployee(1, "Madeleine", "Albright", 1))
#result = employee_service.read_employee_info(Employee(1, "Madeleine", "Albright", 1))
#assert result.employee_id