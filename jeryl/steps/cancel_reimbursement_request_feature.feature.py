from behave import given, when, then

@when(u'I enter the Reimbursement Request ID to be cancelled')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter the Reimbursement Request ID to be cancelled')


@when(u'I click on "Confirm" to cancel my request')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "Confirm" to cancel my request')


@when(u'I receive a notification that the Reimbursement Request has been cancelled')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I receive a notification that the Reimbursement Request has been cancelled')


@then(u'I click the "Okay" button to confirm the cancellation is complete')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click the "Okay" button to confirm the cancellation is complete')

###

Feature: Employees can cancel their Reimbursement Request # cancel_reimbursement_request_feature.feature:1

  Scenario: I would like to cancel my Reimbursement Request                         # cancel_reimbursement_request_feature.feature:3
    Given I am on the employee homepage                                             # ../steps/total_reimbursements_feature_steps.py:3
      Traceback (most recent call last):
        File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\model.py", line 1329, in run
          match.run(runner.context)
        File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\matchers.py", line 98, in run
          self.func(context, *args, **kwargs)
        File "..\steps\total_reimbursements_feature_steps.py", line 5, in step_impl
          raise NotImplementedError(u'STEP: Given I am on the employee homepage')
      NotImplementedError: STEP: Given I am on the employee homepage

    When I enter the Reimbursement Request ID to be cancelled                       # None
    When I click on "Confirm" to cancel my request                                  # None
    When I receive a notification that the Reimbursement Request has been cancelled # None
    Then I click the "Okay" button to confirm the cancellation is complete          # None


Failing scenarios:
  cancel_reimbursement_request_feature.feature:3  I would like to cancel my Reimbursement Request

0 features passed, 1 failed, 0 skipped
0 scenarios passed, 1 failed, 0 skipped
0 steps passed, 1 failed, 4 skipped, 0 undefined

