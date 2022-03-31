from exception.custom_exception import *
import re


class Tester:

    def login_id_tester(self, txt):
        result = re.search(r'^[a-zA-Z0-9]', txt)
        if result is not None and len(txt) <= 20:
            return True
        else:
            raise BadAccountInfo("Type again ID name less then 20 and no special characters ")

    def login_pw_tester(self, txt):
        if len(txt) <= 20:
            return True
        else:
            raise BadAccountInfo("Type again password less then 20")
