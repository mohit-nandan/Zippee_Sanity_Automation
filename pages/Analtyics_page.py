import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AnalyticsPage(BasePage):
    SIDEBAR_MENU = (By.CSS_SELECTOR, ".px-2")
    ANALYTICS_NAME = (By.XPATH, "//span[normalize-space()='Analytics']")
    BUISNESS_TAB = (By.XPATH, "//button[normalize-space()='Business']")
    BRANDS_TAB = (By.XPATH, "//button[normalize-space()='Brands']")

    def view_analytics(self):
        wait = WebDriverWait(self.driver, 20)
        actions = ActionChains(self.driver)

        # Hover over sidebar
        sidebar_element = wait.until(EC.presence_of_element_located(self.SIDEBAR_MENU))
        actions.move_to_element(sidebar_element).perform()

        # Click the Analytics menu
        analytics_element = wait.until(EC.element_to_be_clickable(self.ANALYTICS_NAME))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", analytics_element)
        analytics_element.click()

        # Confirm URL loaded
        wait.until(EC.url_contains("/analytics"))

        self.click(*self.BUISNESS_TAB)
        time.sleep(3)

        self.click(*self.BRANDS_TAB)
        time.sleep(3)

        # Wait for the Business tab to be clickable, then click
        # wait.until(EC.element_to_be_clickable(self.BUISNESS_TAB)).click()

        # # ✅ Wait for content under the Business tab to be visible
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Business')]")))

        # # Click the Brands tab
        # wait.until(EC.element_to_be_clickable(self.BRANDS_TAB)).click()

        # # ✅ Wait for content under Brands tab to load
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Brand')]")))
