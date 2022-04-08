from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class NovoEmployeePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_cancel_input_box(self):
        return self.driver.find_element(By.ID, 'cancelReq')

    def select_cancel_submit_button_box(self):
        return self.driver.find_element(By.ID, 'cancelButton')

    def select_log_out_button_box(self):
        return self.driver.find_element(By.ID, 'logOut')

    def select_amount_input_box(self):
        return self.driver.find_element(By.ID, 'amount')

    def select_comment_input_box(self):
        return self.driver.find_element(By.ID, 'comment')

    def select_type_selector(self): #travel
        return self.driver.find_element(By.ID, 'category')

    def select_submit_button(self):
        return self.driver.find_element(By.ID, 'submitButton')
