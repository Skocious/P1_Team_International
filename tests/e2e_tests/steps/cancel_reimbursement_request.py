from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then


@given(u'I am in the employee page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Will/Desktop/P1_Team_International/html_js/novo_edge_home.html")


@when(u'I enter {request_id} into the cancel input box')
def step_impl(context, request_id: int):
    context.novo_employee.select_cancel_input_box().send_keys(request_id)


@when(u'I click cancel submit button')
def step_impl(context):
    context.novo_employee.select_cancel_submit_button_box.click()


@then(u'I should be able to read an alert with some text in it')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.novo_employee.get_alert().text == "You have successfully canceled a reimbursement request!"