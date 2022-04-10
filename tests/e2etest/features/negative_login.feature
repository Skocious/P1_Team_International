Feature: I need to log-in to my employee account to file for reimbursement for my company expenses negative
    Scenario Outline: Employees should be able to log in negative.
        Given   I am on the company main page
        When    I enter my negative <wrong_username> in the username box
        When    I enter my negative <wrong_password> in the password box
        When    I click the log-in button
        Then    I receive an alert that i have entered an incorrect username
        Examples:
            | wrong_username | wrong_password |
            | dasfdasf       | dasfdasfdas    |
#