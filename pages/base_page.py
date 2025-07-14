class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def type(self, by, locator, value):
        self.find(by, locator).send_keys(value)

    def click(self, by, locator):
        self.find(by, locator).click()
