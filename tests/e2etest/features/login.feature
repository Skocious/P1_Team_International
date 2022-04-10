Feature: I need to log-in to my employee account to file for reimbursement for my company expenses

    Scenario Outline: Employees should be able to log in.
        Given   I am on the company main page
        When    I enter my <username> in the username box
        When    I enter my <password> in the password box
        When    I click the log-in button
        Then     I am re-directed to the employee homepage with <title>




    Examples:
        | username | password | title                  |
        | test4    | test44   | Novo Employee Homepage |
