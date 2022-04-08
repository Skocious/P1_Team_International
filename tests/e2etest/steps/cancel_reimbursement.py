import time
from selenium.webdriver.support.expected_conditions import alert_is_present, invisibility_of_element
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then


@given(u'I am in the employee page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Yeonghwan%20Choi/Desktop/employee_homepage.html")
    time.sleep(1)


@when(u'I enter the Reimbursement {request_id} to be cancelled')
def step_impl(context, request_id: int):
    context.novo_employee.select_cancel_input_box().send_keys(int(request_id))
    time.sleep(1)


@when(u'I click on Confirm to cancel my request')
def step_impl(context):
    context.novo_employee.select_cancel_submit_button_box().click()
    time.sleep(1)


@then(u'I receive a notification that the Reimbursement Request has been cancelled')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.driver.switch_to.alert.text == "You have successfully canceled a reimbursement request!"
    time.sleep(1)
