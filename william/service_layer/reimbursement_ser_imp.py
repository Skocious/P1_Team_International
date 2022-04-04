from data_access_layer.reimbursement_dal.reimbursement_dao import reimbursementDaoImp
from william.service_layer.reimbursement_ser_int import reimbursementSerInt

reimb_dao = reimbursementDaoImp()


class reimbursementServiceImp(reimbursementSerInt):

    def service_create_request(self):
        pass

    def service_get_reimbursement_by_request_id(self):
        pass

    def service_get_all_requests_by_employee_id(self):
        pass

    def service_update_reimbursement_request(self):
        pass

    def service_delete_reimbursement_request(self):
        pass
