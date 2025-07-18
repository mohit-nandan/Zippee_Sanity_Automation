# import time
# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage

# class LoginPage(BasePage):
#     USERNAME = (By.XPATH, '//input[@id="email"]')  # adjust as needed
#     PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
#     Continue_with_email_btn = (By.XPATH, "//button[normalize-space()='Continue with Email']") 
#     LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")  # adjust as needed

#     def login(self, username, password):
#         self.type(*self.USERNAME, username)
#         time.sleep(1) 
#         self.click(*self.Continue_with_email_btn)
#         time.sleep(1) 
#         self.type(*self.PASSWORD, password)
#         time.sleep(1) 
#         self.click(*self.LOGIN_BTN)
#         time.sleep(1) 

import time
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    USERNAME = (By.XPATH, '//input[@id="email"]')
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    Continue_with_email_btn = (By.XPATH, "//button[normalize-space()='Continue with Email']") 
    LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")

    @allure.step("Login with username: {1} and password: [HIDDEN]")
    def login(self, username, password):
        with allure.step("Enter username"):
            self.type(*self.USERNAME, username)
            time.sleep(1)

        with allure.step("Click 'Continue with Email' button"):
            self.click(*self.Continue_with_email_btn)
            time.sleep(1)

        with allure.step("Enter password"):
            self.type(*self.PASSWORD, password)
            time.sleep(1)

        with allure.step("Click 'Login' button"):
            self.click(*self.LOGIN_BTN)
            time.sleep(1)
