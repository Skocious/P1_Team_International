from service_layer.reimbursement_service.reimbursement_service_interface import reimbursementServiceInterface
from data_access_layer.reimbursement_dal.reimbursement_dao import reimbursementDaoImp
from entities.reimbursement import Reimbursement
from utilities.tester_module import tester


class reimbursementServiceImp(reimbursementServiceInterface):

    def __init__(self):
        self.RDI = reimbursementDaoImp()

    def create_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        if tester.reimbursement_tester(reimbursement):
            return self.RDI.create_request(reimbursement)

    def get_all_reimbursement_by_employee_id(self, employee_id: int) -> list:
        return self.RDI.get_all_requests_by_employee_id(employee_id)

    def cancel_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursement.status = 'Cancel'
        return self.RDI.get_all_requests_by_employee_id(reimbursement)
