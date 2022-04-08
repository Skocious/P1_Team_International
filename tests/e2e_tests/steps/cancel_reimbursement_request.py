from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then
<<<<<<< HEAD
from selenium import webdriver

@given(u'I am on the employee homepage')
def step_impl(context):
    webdriver.Chrome("chromedriver.exe").get("file:///C:/Users/Yeonghwan%20Choi/Desktop/employee_homepage.html")


@when(u'I enter the Reimbursement {request_id} to be cancelled')
=======


@given(u'I am in the employee page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Yeonghwan%20Choi/Desktop/employee_homepage.html")


@when(u'I enter {request_id} into the cancel input box')
>>>>>>> origin/main
def step_impl(context, request_id: int):
    context.novo_employee.select_cancel_input_box().send_keys(request_id)


<<<<<<< HEAD
@when(u'I click on Confirm to cancel my request')
=======
@when(u'I click cancel submit button')
>>>>>>> origin/main
def step_impl(context):
    context.novo_employee.select_cancel_submit_button_box.click()


<<<<<<< HEAD
@then(u'I receive a notification that the Reimbursement Request has been cancelled')
=======
@then(u'I should be able to read an alert with some text in it')
>>>>>>> origin/main
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.novo_employee.get_alert().text == "You have successfully canceled a reimbursement request!"