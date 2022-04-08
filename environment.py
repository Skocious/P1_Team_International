<<<<<<< HEAD
from tests.e2e_tests.page_object_models.novo_homepage import NovoHomPage
from tests.e2e_tests.page_object_models.novo_employee_page import NovoEmployeePage
from behave.runner import Context
from selenium import webdriver

def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.novo_home = NovoHomPage(context.driver)
=======
from behave.runner import Context
from selenium import webdriver
from tests.e2e_tests.page_object_models.novo_homepage import NovoHompage
from tests.e2e_tests.page_object_models.novo_employee_page import NovoEmployeePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("tests/e2e_tests/chromedriver.exe")
    context.novo_home = NovoHompage(context.driver)
>>>>>>> origin/main
    context.novo_employee = NovoEmployeePage(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context):
    context.driver.quit()

<<<<<<< HEAD
# C:\Users\Yeonghwan Choi\Desktop\P1_Team_International\environment.py
=======
>>>>>>> origin/main
