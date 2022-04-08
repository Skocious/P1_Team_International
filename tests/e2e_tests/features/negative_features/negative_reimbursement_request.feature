Feature: From the employee homepage, employees have the ability to file for reimbursement for company expenses
  Scenario Outline: I need to fill out a reimbursement request()
    Given   I am on the employee homepage
    When    I fill in the dollar <amount>
    When    I fill in the <comments> section
    When    I select the <category> from the drop down box
    When    I click on the submit button
    Then    I will receive a Successfully Submitted notification for my request

    Examples:
      | amount | comments      | category |
      | 500    | "helloworld"  | 1        |
      | 500    | "helloworld2" | 2        |
      | 500    | "helloworld3" | 3        |
      | 500    | "helloworld4" | 4        |
      | 500    | "helloworld5" | 5        |