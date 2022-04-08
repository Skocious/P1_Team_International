from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait
from behave import given, when, then


@given(u'I am on the company main page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Yeonghwan%20Choi/Desktop/novo_home.html")


@when(u'I enter my {username} in the username box')
def step_impl(context, username: str):
    context.novo_home.select_username_box().send_keys(username)


@when(u'I enter my {password} in the password box')
def step_impl(context, password: str):
    context.novo_home.select_password_box().send_keys(password)


@when(u'I click the log-in button')
def step_impl(context):
    context.novo_home.select_login_button().click()


@then(u'I am re-directed to the employee homepage with {title}')
def step_impl(context, title: str):
    WebDriverWait(context.driver, 4).until(title_contains(title))
    assert context.driver.title == title