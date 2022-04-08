from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then
from selenium import webdriver

@given(u'I am on the employee homepage')
def step_impl(context):
    webdriver.Chrome("chromedriver.exe").get("file:///C:/Users/Yeonghwan%20Choi/Desktop/employee_homepage.html")


@when(u'I enter the Reimbursement {request_id} to be cancelled')
def step_impl(context, request_id: int):
    context.novo_employee.select_cancel_input_box().send_keys(request_id)


@when(u'I click on Confirm to cancel my request')
def step_impl(context):
    context.novo_employee.select_cancel_submit_button_box.click()


@then(u'I receive a notification that the Reimbursement Request has been cancelled')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.novo_employee.get_alert().text == "You have successfully canceled a reimbursement request!"