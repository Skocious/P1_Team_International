from service_layer.reimbursement_service.reimbursement_service_interface import ReimbursementServiceInterface
from data_access_layer.reimbursement_dal.reimbursement_dao import ReimbursementDaoImp
from entities.reimbursement import Reimbursement
from entities.employee import Employee
from exception.custom_exception import InfoNotFound
from utilities.tester_module import tester


class ReimbursementServiceImp(ReimbursementServiceInterface):

    def __init__(self):
        self.RDI = ReimbursementDaoImp()

    def create_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        if tester.reimbursement_tester(reimbursement):
            reimbursement.balance = float(reimbursement.balance)
            return self.RDI.create_request(reimbursement)

    def get_all_reimbursement_by_employee_id(self, employee_id: int) -> list:
        result = self.RDI.get_all_requests_by_employee_id(employee_id)
        return result

    def cancel_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursement.request_id = tester.id_tester(reimbursement.request_id)
        result: Reimbursement = self.RDI.get_reimbursement_by_request_id(reimbursement)
        result.status = 'Cancel'
        return self.RDI.update_reimbursement_request(result)


