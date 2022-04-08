from selenium.webdriver.support.expected_conditions import alert_is_present, invisibility_of_element
from selenium.webdriver.support.wait import WebDriverWait
from behave import then


@then(u'Then I receive an alert that the Reimburesement Request ID is incorrect')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.driver.switch_to.alert.text == "No account with that Id found"
