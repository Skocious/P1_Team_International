Feature: As am Employee I want to log into my employee homepage.
  Scenario: I want to log-in to my employee homepage with my userID and password.

    Given  I am on the Novo Edge Homepage
    When   I input my username and password, i am able to successfully log in to my account
    Then   I am redirected to the employee homepage.

Feature: On my employee homepage and want to file request for reimbursement
    Given  I am on the Novo Edge Employee homepage
    When   I enter the request information
    When   I click the request button
    Then   I am given an alert telling me "You have successfully submitted a reimbursement request