from behave.runner import Context
from selenium import webdriver
from tests.e2e_tests.page_object_models.novo_homepage import NovoHompage
from tests.e2e_tests.page_object_models.novo_employee_page import NovoEmployeePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("tests/e2e_tests/chromedriver.exe")
    context.novo_home = NovoHompage(context.driver)
    context.novo_employee = NovoEmployeePage(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context):
    context.driver.quit()

