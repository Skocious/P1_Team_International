Feature: From the employee homepage, employees have the ability to file for reimbursement for company expenses
  Scenario Outline: I need to fill out a reimbursement request()
    Given   I am on the employee homepage
    When    I fill in the dollar <amount>
    When    I fill in the <comments> section
    When    I select the <category> expense category from the drop down box
    When    I click on the Submit button
    Then    I will receive a Successfully Submitted notification for my request

    Examples:
      |amount|comments     |category      |
      |500   |"helloworld" |travel        |
      |500   |"helloworld2"|supplies      |
      |500   |"helloworld3"|meals         |
      |500   |"helloworld4"|parking       |
      |500   |"helloworld5"|communication |