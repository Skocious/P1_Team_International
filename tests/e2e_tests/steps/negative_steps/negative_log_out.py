from behave import given, when, then
from selenium.webdriver.support.expected_conditions import title_contains, alert_is_present
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am in the employee homepage')
def step_impl(context):
    context.driver.get("file:///C:/Users/Yeonghwan%20Choi/Desktop/employee_homepage.html")


@when(u'I click the log-out button')
def step_impl(context):
    context.novo_employee.select_log_out_button_box().click()
#
#
# @when(u'I accept alert')
# def step_impl(context):
#     WebDriverWait(context.driver, 4).until(alert_is_present())
#
#

@then(u'I should be redirected to a webpage with the title {title}')
def step_impl(context, title):
    WebDriverWait(context.driver, 4).until(title_contains(title))
    assert context.driver.title == title