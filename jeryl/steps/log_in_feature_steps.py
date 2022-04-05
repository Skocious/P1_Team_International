from behave import given, when, then

@given(u'I am in the company\'s main page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am in the company\'s main page')

@when(u'I enter my username in the username box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter my username in the username box')


@when(u'I enter my password in the password box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter my password in the password box')


@when(u'I click the log-in button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the log-in button')


@then(u'I am re-directed to the employee homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am re-directed to the employee homepage')
