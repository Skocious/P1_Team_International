from behave import given, when, then


@given(u'I am in the companys main page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Will/Desktop/P1_Team_International/html_js/novo_edge_home.html")


@when(u'I enter my us {username} in the username box')
def step_impl(context, username: str):
    context.novo_home.select_username_box.select_username_box().send_keys(username)


@when(u'I enter my {password} in the password box')
def step_impl(context, password: str):
    context.novo_home.select_username_box.select_password_box().send_keys(password)


@when(u'I click the log-in button')
def step_impl(context):
    context.novo_home.select_login_button.select_login_button.click()


@then(u'I am re-directed to the employee homepage with {title}')
def step_impl(context, title: str):
    assert context.novo_home.driver.title == title
