import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class EmergencyPage(BasePage):
    SIDEBAR_MENU = (By.CSS_SELECTOR, ".px-2")
    EMERGENCY_NAME = (By.XPATH, "//span[normalize-space()='Emergency Comms']")
    EMERGENCY_LOGS = (By.XPATH, "//button[normalize-space()='View Logs']")
    EMERGENCY_CLOSE = (By.XPATH, "(//button[normalize-space()='×'])[1]")

    def view_emergency(self):
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)

        # Hover over sidebar
        sidebar = wait.until(EC.presence_of_element_located(self.SIDEBAR_MENU))
        actions.move_to_element(sidebar).perform()

        # Click Emergency menu
        emergency = wait.until(EC.element_to_be_clickable(self.EMERGENCY_NAME))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", emergency)
        emergency.click()

        # Confirm URL loaded
        wait.until(EC.url_contains("/emergency-comms"))

        self.click(*self.EMERGENCY_LOGS)
        print("Emergency logs opened successfully")

        close_button = wait.until(EC.element_to_be_clickable(self.EMERGENCY_CLOSE))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
        close_button.click()
        time.sleep(1)


