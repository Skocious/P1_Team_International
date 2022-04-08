from behave.runner import Context
from selenium import webdriver

from poms.reimbursement_request_home import Reimbursement


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.reimbursement_request_home = Reimbursement(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
