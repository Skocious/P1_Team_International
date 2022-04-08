import time
from behave import then


@then(u'I receive an alert that i have entered an incorrect username')
def step_impl(context):
    time.sleep(2)
    assert context.driver.switch_to.alert.text == "Wrong Login Info Please, Try Again"

