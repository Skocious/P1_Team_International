from behave import given, when, then

@given(u'I am on the employee homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the employee homepage')


@when(u'I click the "Submit" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Submit" button')


@then(u'I will be able to see the "Total Amount" of my Reimbursement Requests')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will be able to see the "Total Amount" of my Reimbursement Requests')


