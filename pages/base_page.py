from selenium.webdriver.common.keys import Keys
import time
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def type(self, by, locator, value):
        self.find(by, locator).send_keys(value)

    def click(self, by, locator):
        self.find(by, locator).click()
    
    def clear(self, by, locator):
        self.find(by, locator).clear()
    
    def clear_and_reset(self, by, locator):
        element = self.find(by, locator)
        element.clear()
        time.sleep(0.5)
        element.send_keys(" ")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.TAB)
