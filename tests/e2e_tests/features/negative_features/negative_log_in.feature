Feature: Employees should be able to log in (negative).

    Scenario Outline: I need to log-in to my employee account with wrong info to file for reimbursement for my company expenses
        Given   I am on the company main page
        When    I enter an incorrect <username> in the username box
#        When    I enter an incorrect <password> in the password box
#        When    I click the log-in button
#        Then    I receive an alert that I have entered wrong info

#
        Examples:
#            | username | password |
#            | test2123 | testxxx  |
#
#