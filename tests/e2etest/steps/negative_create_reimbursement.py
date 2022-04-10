from behave import then
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
import time


@then(u'I receive an alert that i have wrong values')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    balance_error = "Balance must be 1000 or less."
    negative_balance = "Must be more than $1 per request"
    comment_error = "Comment should be no longer than 100 characters"

    message = context.driver.switch_to.alert.text
    assert message in [balance_error, comment_error, negative_balance]
    context.driver.switch_to.alert.accept()
    time.sleep(1)
