from behave import given, when, then


@given(u'I am in the employee homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am in the employee homepage')


@when(u'I click the log-out button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the log-out button')

@then(u'I am re-directed back to the landing homepage, clearing everything on the employee homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am re-directed back to the landing homepage, clearing everything on the employee homepage')

