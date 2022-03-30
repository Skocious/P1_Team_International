import re

class Tester:

    def id_tester(self, txt):
        result = re.search(r'^[a-zA-Z]+\d+[a-zA-Z\d]+$', txt)
        if result is not None and len(txt) <= 20:
            return True

    def pw_tester(self):
        result = re.search(r'^[a-zA-Z]+\d+[a-zA-Z\d]+$', txt)
        if result is not None and len(txt) <= 20:
            return True
