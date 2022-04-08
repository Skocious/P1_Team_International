Feature: Employees can cancel their Reimbursement Request

    Scenario Outline: I would like to cancel my Reimbursement Request
        Given   I am in the employee page
        When    I enter the Reimbursement <request_id> to be cancelled
        When    I click on Confirm to cancel my request
        Then    I receive a notification that the Reimbursement Request has been cancelled


      Examples:
        | request_id |
        | 20         |