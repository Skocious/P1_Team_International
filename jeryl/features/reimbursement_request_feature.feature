Feature:    From the employee homepage, employees have the ability to file for reimbursement for company expenses

Scenario:   I am on the employee homepage where i can fill out a reimbursement request
      Given   I need to enter multiple fields of information
      When    I fill in the dollar amount
      When    I fill in the comments section
      When    I select the "Travel" expense category from the drop down box
      When    I click on the "Submit" button
      Then    I will receive a "Successfully Submitted" notification for my request

Feature:    From the employee homepage, employees have the ability to file for reimbursement for company expenses

  Scenario:   I am on the employee homepage where i can fill out a reimbursement request
      Given   I need to enter multiple fields of information
      When    I fill in the dollar amount
      When    I fill in the comments section
      When    I select the "Travel" expense category from the drop down box
      When    I click on the "Submit" button
      Then    I will receive a "Successfully Submitted" notification for my request

Feature: Employees can cancel their Reimbursement Request

    Scenario: I would like to cancel my Reimbursement Request
        Given   I am on the employee homepage
        When    I enter the Reimbursement Request ID to be cancelled
        When    I click on "Confirm" to cancel my request
        When    I receive a notification that the Reimbursement Request has been cancelled
        Then    I click the "Okay" button to confirm the cancellation is complete

Feature: Employees can review the total amount of all their Reimbursement Requests

    Scenario: I would like to know the total dollar amount of my Reimbursement Requests
        Given   I am on the employee homepage
        When    I click the "Submit" button
        Then    I will be able to see the "Total Amount" of my Reimbursement Requests

Feature: Employees should be able to log out.

    Scenario: I need to log out of my employee account.
        Given  I am in the employee homepage
        When   I click the log-out button
        Then   I am re-directed back to the landing homepage, clearing everything on the employee homepage





