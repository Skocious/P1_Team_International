from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait

@given(u'I am on the employee homepage')
def step_impl(context):
    context.driver.get("file:///C:/Users/Yeonghwan%20Choi/Desktop/employee_homepage.html")


@when(u'I fill in the dollar {amount}')
def step_impl(context, amount):
    context.novo_employee.select_amount_input_box().send_keys(amount)


@when(u'I fill in the {comments} section')
def step_impl(context, comments):
    context.novo_employee.select_comment_input_box().send_keys(comments)


@when(u'I select the {category} from the drop down box')
def step_impl(context, category):
    context.novo_employee.select_type_selector(category)
    context.driver.implicitly_wait(1)

@when(u'I click on the submit button')
def step_impl(context):
    context.novo_employee.select_submit_button().click()
    context.driver.implicitly_wait(1)

@then(u'I will receive a Successfully Submitted notification for my request')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.driver.switch_to.alert.text == "You have successfully created a reimbursement request!"
    context.driver.switch_to.alert.accept()