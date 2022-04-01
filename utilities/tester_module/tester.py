from entities.reimbursement import Reimbursement
from exception.custom_exception import *
import re


def login_id_tester(txt):
    result = re.search(r'^[a-zA-Z0-9]', txt)
    if result is not None and len(txt) <= 20:
        return True
    else:
        raise BadAccountInfo("Type again ID name less than 20 and no special characters ")


def login_pw_tester(txt):
    if len(txt) <= 20:
        return True
    else:
        raise BadAccountInfo("Type again password less than 20")


def reimbursement_tester(obj: Reimbursement):
    try:
        obj.balance = float(obj.balance)
    except:
        raise TypeError('Balance must be numeric')
    if 1 > obj.balance > 1000:
        raise WrongBalance("Must be between $1 and $1000 per request")
    elif len(obj.comment) > 100:
        raise TooLongComment('Comment shoul be no longer than 100 characters ')
    else:
        return True
