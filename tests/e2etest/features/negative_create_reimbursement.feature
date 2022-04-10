Feature: From the employee homepage, employees have the ability to file for reimbursement for company expenses negative
  Scenario Outline: I need to fill out a reimbursement request() negative

    Given   I am on the employee homepage
    When    I fill in the dollar <amount>
    When    I fill in the <comments> section
    When    I select the <category> from the drop down box
    When    I click on the Submit button
    Then    I receive an alert that i have wrong values

    Examples:
      | amount  | category | comments                                                                                                |
      | 5000000 | travel   | "I wish i had this much"                                                                                |
      | 500     | supplies | 'toooooloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong' |
      | -500    | meals    | "reimbursement to company"                                                                              |

#    travel, supplies, meals, parking, communication