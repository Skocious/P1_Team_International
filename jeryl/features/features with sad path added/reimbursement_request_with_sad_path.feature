Feature: From the employee homepage, employees have the ability to file for reimbursement for company expenses
  Scenario: I need to fill out a reimbursement request
    Given   I am on the employee homepage
     When    I fill in the dollar amount
     When    I fill in the comments section
     When    I select the Travel expense category from the drop down box
     When    I click on the Submit button
     Then    I will receive a Successfully Submitted notification for my request

  ### SAD PATH ###

Feature: From the employee homepage, employees have the ability to file for reimbursement for company expenses
  Scenario: I am on the employee homepage where i can fill out a reimbursement request
    Given   I am on the employee homepage
     When    I fill in a dollar amount over the $1,000
     Then    I will receive an alert that an amount over $1,000 is not allowed

Feature: From the employee homepage, employees have the ability to file for reimbursement for company expenses
  Scenario: I am on the employee homepage where i can fill out a reimbursement request
    Given   I am on the employee homepage
     When    I go over the 100 character limit in the Comments section
     Then    I receive an alert that i have gone over the 100 character limit

Feature: From the employee homepage, employees have the ability to file for reimbursement for company expenses
  Scenario: I am on the employee homepage where i can fill out a reimbursement request
    Given   I am on the employee homepage
     When    I mistakenly select the Supplies expense category from the drop down box
     Then    I can re-select the Travel expense category

