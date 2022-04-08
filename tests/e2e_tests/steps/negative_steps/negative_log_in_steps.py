from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then


@given(u'I am on the company main page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Yeonghwan%20Choi/Desktop/novo_home.html")


@when(u'I enter an incorrect {username} in the username box')
def step_impl(context, username: str):
    context.novo_home.select_username_box().send_keys(username)
#
#
# @when(u'I enter an incorrect {password} in the password box')
# def step_impl(context, password: str):
#     context.novo_home.select_password_box().send_keys(password)
#
#
# @when(u'I click the log-in button')
# def step_impl(context):
#     context.novo_home.select_login_button().click()
#
#
# @then(u'I receive an alert that I have entered wrong info')
# def step_impl(context):
#     WebDriverWait(context.driver, 4).until(alert_is_present())
#     assert context.driver.switch_to.alert.text == "Wrong Login Info Please, Try Again"
#     context.driver.switch_to.alert.accept()
