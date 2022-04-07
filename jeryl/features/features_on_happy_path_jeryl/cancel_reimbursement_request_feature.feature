Feature: Employees should be able to cancel their Reimbursement Request

    Scenario: I would like to cancel my Reimbursement Request
        Given   I am on the employee homepage
        When    I enter the Reimbursement Request ID to be cancelled
        When    I click on Confirm to cancel my request
        When    I receive a notification that the Reimbursement Request has been cancelled
        Then    I click the Okay button to confirm the cancellation is complete





