import logging
from flask_cors import CORS
from entities.reimbursement import Reimbursement
from service_layer.account_service.account_service_imp import AccountServiceImp
from service_layer.employee_service.employee_service_imp import EmployeeServiceImp
from service_layer.reimbursement_service.reimbursement_service_imp import ReimbursementServiceImp
from entities.account import Account
from exception.custom_exception import *
from flask import Flask, jsonify, request

import config
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")
app: Flask = Flask(__name__)
CORS(app)

ASI = AccountServiceImp()
ESI = EmployeeServiceImp()
RSI = ReimbursementServiceImp()

config.login_employee = None  # Employee class object


@app.route("/login", methods=["POST"])
def login():
    try:
        data: dict = request.get_json()
        login_data = Account(data['id_name'], data['password'])
        config.login_employee = ASI.log_in(login_data)

        return vars(config.login_employee), 200
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


# 2. As an employee I want to be able to log out through a webpage.
@app.route("/logout", methods=["GET"])
def logout():
    try:
        if config.login_employee is None:
            return "Wrong try please sign in"
        else:
            config.login_employee = None
            return " Successfully Logout", 200
    except UserNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/create_reimbursement_request", methods=["POST"])
def create_reimbursement_request():
    try:
        if config.login_employee is None:
            return "Wrong try please sign in"
        else:
            data: dict = request.get_json()
            Reimbursement_data = Reimbursement(0, data['reimbursement_type'], data['balance'], data['comment'],
                                               0, config.login_employee.employee_id)
            result = RSI.create_reimbursement_request(Reimbursement_data)
            return vars(result), 200
    except BalanceUnder as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except BalanceOver as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except TooLongComment as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/cancel_reimbursement_request/<request_id>", methods=["GET"])
def cancel_reimbursement_request(request_id: int):
    try:
        if config.login_employee is None:
            return "Wrong try please sign in"
        else:
            result = RSI.cancel_reimbursement_request(Reimbursement(request_id, 0, 0, 0, 0, 0))
            return vars(result), 200
    except TypeError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/get_all_requests_by_employee_id/<id>", methods=["GET"])
def get_all_requests_by_employee_id(id):
    try:
        if config.login_employee is None:
            return "Wrong try please sign in"
        else:
            result = RSI.get_all_reimbursement_by_employee_id(config.login_employee.employee_id)

            return jsonify(result), 200
    except InfoNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/get_sum_requests_amount_by_employee_id/<id>", methods=["GET"])
def get_sum_requests_amount_by_employee_id(id):
    try:
        if config.login_employee is None:
            return "Wrong try please sign in"
        else:
            result = RSI.get_all_reimbursement_by_employee_id(config.login_employee.employee_id)
            return jsonify(sum([i['balance'] for i in result if i['status'] == 'pending'])), 200
    except InfoNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


app.run()
