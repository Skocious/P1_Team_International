from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class NovoHomPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_box(self):
        return self.driver.find_element(By.ID, 'username-field')

    def select_password_box(self):
        return self.driver.find_element(By.ID, 'password-field')

    def select_login_button(self):
        return self.driver.find_element(By.ID, 'loginButton')
