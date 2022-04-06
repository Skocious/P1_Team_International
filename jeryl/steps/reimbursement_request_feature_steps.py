from behave import given, when, then

@given(u'I need to enter multiple fields of information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I need to enter multiple fields of information')


@when(u'I fill in the dollar amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill in the dollar amount')


@when(u'I fill in the comments section')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill in the comments section')


@when(u'I select the Travel expense category from the drop down box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select the Travel expense category from the drop down box')


@when(u'I click on the Submit button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the Submit button')


@then(u'I will receive a Successfully Submitted notification for my request')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will receive a Successfully Submitted notification for my request')


