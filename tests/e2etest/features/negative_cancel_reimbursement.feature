Feature: Employees can cancel their Reimbursement Request negative

    Scenario Outline: I would like to cancel my Reimbursement Request negative
        Given   I am in the employee page
        When    I enter the Reimbursement <wrong_request_id> to be cancelled
        When    I click on Confirm to cancel my request
        Then    Then I receive an alert that the Reimburesement Request ID is incorrect


      Examples:
        | wrong_request_id |
        | 20111111111      |