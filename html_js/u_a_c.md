Acceptance Criteria for Project: Employee Reimbursement

Feature:Employees should be able to log in and log out of their employee accounts.

Scenario:   As an employee I want to login to my employee homepage using my employee id and password.

    Given:  I am on the employee homepage
    When:   I input my username
    Wehn:   I input my password
    When:   I click the "Login" button
    Then:   I am given an alert that I have sucessfully logged in and will be redirected to the employee homepage.

    Given:  I have received the alert of successful login
    When:   I click the "Ok" button
    Then:   I am re-directed to the employee homepage

Feature: Employees have the ability to file for reimbursement for expenses incurred on behalf of the company

Scenario:   I am on my employee homepage and wish to file a request for reimbursement

    Given:  I have successfully logged in to the employee homepage and have clicked on the "Reimbursement" button
    When:   A "Create Reimbursement Request" button appears on the Reimbursement webpage
    When:   I click on the "Create Reimbursement Request"
    Then:   I receive a Reimbursement Request form with the Request ID automatically inputted into the form.

    Given:  I need to fill in multiple fields in the Reimbursement Request form,
    When:   I fill out the first field,a drop down box allows me to choose one of five categories of expenses
    Then:   I will select the "Travel" category as the reason for my expense

    Given:  I must identify the details regarding this expense in the "Comments" section
    When:   I begin imputing my text into the "Comments" section
    Then:;  A statement appears that the comments must be no longer than 100 characters.

    Given:  I must identify the dollar amount for the Reimbursement Request
    When:   I imput the amount into the dollar amount field
    Then:   A statement appears identifying that the amount must be between $1.00 and $1,000.00

    Given:  I have filled in all the information requested on the Reimbursement Request form
    When:   I have clicked on "Complete"
    When:   I have clicked on the "Submit" button
    Then:   I will receive a "Successfully Submitted" notification or i will receive a "Submission Failed" notification

    Given:  I decide i no longer want to submit a Reimbursement Request
    When:   I am in the Reimbursement Request form or in the "Successfully Submitted" or in the "Submission Failed"
                notification
    Then:   A "Cancel Request" button is available for me to cancel my Reimbursement Request

    Given:  I would like to review the status of all my Reimbursement Requests
    When:   I receive the successful or failed notification
    When    A button appears to check the status of all Reimbursement Requests
    When:   i click on this option
    Then:   A summary page appears with all my Reimbursement Requests with a total amount outstanding

    Note: Log-out scenario is above