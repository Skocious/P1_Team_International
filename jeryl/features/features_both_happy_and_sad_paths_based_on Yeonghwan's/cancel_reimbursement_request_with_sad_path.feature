Feature: Employees can cancel their Reimbursement Request
    Scenario Outline: I would like to cancel my Reimbursement Request
        Given   I am on the employee homepage
        When    I enter the Reimbursement <request_id> to be cancelled
        When    I click on Confirm to cancel my request
        When    I receive a notification that the Reimbursement Request has been cancelled
        Then    I click the Okay button to confirm the cancellation is complete

      Examples:
        | request_id |
        | 20         |


      ### SAD PATH ###

Feature: Employees can cancel their Reimbursement Request
    Scenario Outline: I would like to cancel my Reimbursement Request
        Given   I am on the employee homepage
        When    I enter an incorrect Reimbursement <request_id> to be cancelled
        When    I click on Confirm to cancel my request
        Then    Then I receive an alert that the Reimburesement Request ID is incorrect

      Examples:
        | request_id |
        | 20xxx      |