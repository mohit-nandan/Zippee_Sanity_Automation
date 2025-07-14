import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.XPATH, '//input[@id="email"]')  # adjust as needed
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    Continue_with_email_btn = (By.XPATH, "//button[normalize-space()='Continue with Email']") 
    LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")  # adjust as needed

    def login(self, username, password):
        self.type(*self.USERNAME, username)
        time.sleep(3) 
        self.click(*self.Continue_with_email_btn)
        time.sleep(3) 
        self.type(*self.PASSWORD, password)
        time.sleep(3) 
        self.click(*self.LOGIN_BTN)
        time.sleep(3)  # wait for login to process, adjust as needed
