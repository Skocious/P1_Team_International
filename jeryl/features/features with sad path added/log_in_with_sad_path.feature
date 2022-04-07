Feature: Employees should be able to log in.
    Scenario Outline: I need to log-in to my employee account to file for reimbursement for my company expenses
        Given   I am on the company's main page
        When    I enter my <username> in the username box
        When    I enter my <password> in the password box
        When    I click the log-in button
        Then    I am re-directed to the employee homepage with <title>

        Examples:
            | username |  | password | title                  |
            | test2    |  | test22   | Novo Employee Homepage |


### SAD PATH ###

Feature: Employees should be able to log in.
    Scenario Outline: I need to log-in to my employee account to file for reimbursement for my company expenses
        Given   I am on the company's main page
        When    I enter an incorrect <username> in the username box
        When    I enter my <password> in the password box
        When    I click the log-in button
        Then    I receive an alert that i have entered an incorrect username

        Examples:
            | username |  | password | title                  |
            | testxxx  |  | test22   | Novo Employee Homepage |

Feature: Employees should be able to log in.
    Scenario Outline: I need to log-in to my employee account to file for reimbursement for my company expenses
        Given   I am on the company's main page
        When    I enter my <username> in the username box
        When    I enter an incorrect <password> in the password box
        When    I click the log-in button
        Then    I receive an alert that i have entered an incorrect password

        Examples:
            | username |  | password | title                  |
            | test2    |  | testxxx  | Novo Employee Homepage |

