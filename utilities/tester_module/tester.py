from entities.reimbursement import Reimbursement
from exception.custom_exception import *
import re


def login_id_tester(txt):
    result = re.search(r'^[a-zA-Z0-9]', txt)
    if result is not None and len(txt) <= 20:
        return True
    else:
        raise BadAccountInfo("Type again ID name less than 20 and no special characters")


def login_pw_tester(txt):
    if len(txt) <= 20:
        return True
    else:
        raise BadPasswordInfo("Type again password less than 20")


def reimbursement_tester(obj: Reimbursement):
    try:
        obj.balance = float(obj.balance)
    except:
        raise TypeError('Balance must be numeric')
    if 1 > obj.balance:
        raise BalanceUnder("Must be more than $1 per request")
    elif obj.balance > 1000:
        raise BalanceOver("Balance must be 1000 or less.")
    elif len(obj.comment) > 100:
        raise TooLongComment('Comment should be no longer than 100 characters')
    else:
        return True


def id_tester(obj: int):
    try:
        obj = int(obj)
        return obj
    except:
        raise TypeError("Id number should be numeric")
