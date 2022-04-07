from behave import given, when, then


@given(u'I am in the employee page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Will/Desktop/P1_Team_International/html_js/novo_edge_home.html")


@when(u'I click log out button')
def step_impl(context):
    context.novo_employee.select_cancel_log_out_button_box.click()


@then(u'I should be redirected to a webpage with the title {title}')
def step_impl(context, title):
    assert context.novo_employee.driver.title == title