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

