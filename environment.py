from tests.e2etest.poms.novo_employee_page import NovoEmployeePage
from tests.e2etest.poms.novo_homepage import NovoHomPage
from behave.runner import Context
from selenium import webdriver


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.novo_home = NovoHomPage(context.driver)
    context.novo_employee = NovoEmployeePage(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context):
    context.driver.quit()

