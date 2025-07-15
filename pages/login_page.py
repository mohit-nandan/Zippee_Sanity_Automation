import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    USERNAME = (By.XPATH, '//input[@id="email"]') 
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    Continue_with_email_btn = (By.XPATH, "//button[normalize-space()='Continue with Email']") 
    LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")
    WRONG_USERNAME = "abcd"
    WRONG_PASSWORD = "test1234"

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        self.type(*self.USERNAME, self.WRONG_USERNAME)
        time.sleep(1)
        self.click(*self.Continue_with_email_btn)
        time.sleep(1)


        self.driver.refresh()


        self.type(*self.USERNAME, username)
        self.click(*self.Continue_with_email_btn)
        wait.until(EC.presence_of_element_located(self.PASSWORD)) 
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
        time.sleep(1)

