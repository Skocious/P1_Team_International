Feature:    From the employee homepage, employees have the ability to file for reimbursement for company expenses

  Scenario: I need to fill out a reimbursement request on the employee homepage
    Given  I am on the employee homepage
     When   I fill in the dollar amount
     When   I fill in the comments section
     When   I select the Travel expense category from the drop down box
     When   I click on the Submit button
     Then   I will receive a Successfully Submitted notification for my request














