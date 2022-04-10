Feature: Employees should be able to log out.

    Scenario Outline: I need to log out of my employee account.
        Given  I am in the employee homepage
        When   I click the log-out button
        Then   I should be redirected to a webpage with the title <title>

    Examples:
        |title              |
        |Novo Employee Login|



