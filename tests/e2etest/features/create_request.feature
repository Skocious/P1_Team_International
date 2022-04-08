Feature: From the employee homepage, employees have the ability to file for reimbursement for company expenses
  Scenario Outline: I need to fill out a reimbursement request()

    Given   I am on the employee homepage
    When    I fill in the dollar <amount>
    When    I fill in the <comments> section
    When    I select the <category> from the drop down box
    When    I click on the Submit button
    Then    I will receive a Successfully Submitted notification for my request

    Examples:
      | amount | comments                          | category      |
      | 500    | "very strong wooden walking cane" | travel        |
      | 1      | "very old spinning wheel"         | supplies      |
      | 999    | "Samosa empty __init__ "          | meals         |
      | 500    | "Horse parking ticket"            | parking       |
      | 500    | "Payphone bill from year 2100"    | communication |

#    travel, supplies, meals, parking, communication