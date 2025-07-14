import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class BrandPage(BasePage):
    SIDEBAR_MENU = (By.CSS_SELECTOR, ".px-2")
    BRAND_NAME = (By.XPATH, "//span[normalize-space()='Brands']")
    ADD_BRAND_BUTTON = (By.XPATH, "//button[normalize-space()='Add Brand']")
    CANCEL_BUTTON = (By.XPATH, "//button[@class='text-xl text-black']//*[name()='svg']")
    VIEW_CONFIG_BUTTON = (By.XPATH, "//tbody/tr[1]/td[6]/button[1]")
    CANCEL_CONFIG_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    BRAND_NAME_TEXT = (By.XPATH, "//tbody/tr[1]/td[1]/a[1]")
    BRAND_NAME_INPUT = (By.XPATH, "//th[1]//div[1]//div[1]//input[1]")
    DROPDOWN = (By.CSS_SELECTOR, ".css-zmivz5-container")  # Dropdown container
    DROPDOWN_OPTION_ACTIVE = (By.XPATH, "//div[contains(text(), 'Active')]")
    DROPDOWN_OPTION_INACTIVE = (By.XPATH, "//div[contains(text(), 'Inactive')]")
    STATUS_COLUMN_CELL = (By.XPATH, "//tbody/tr[1]/td[5]")  # Assuming 5th column shows status
    BRAND_DETAIL_LINK = (By.XPATH, "//tbody/tr[1]/td[1]/a")
    BRAND_DETAIL_COMMERICALS_TAB = (By.XPATH, "//button[normalize-space()='Commercials']")
    BRAND_DETAIL_GST_TAB = (By.XPATH, "//button[normalize-space()='GST Details']")
    BRAND_DETAIL_WAREHOUSE_TAB = (By.XPATH, "//button[normalize-space()='Warehouses']")
    BRAND_DETAIL_WEBHOOK_TAB = (By.XPATH, "//button[normalize-space()='Webhooks']")
    BRAND_DETAIL_RULES_TAB = (By.XPATH, "//button[normalize-space()='Rules']")


    def create_brand(self):
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)


        sidebar_element = wait.until(EC.presence_of_element_located(self.SIDEBAR_MENU))
        actions.move_to_element(sidebar_element).perform()
        time.sleep(1)

        brand_element = wait.until(EC.element_to_be_clickable(self.BRAND_NAME))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", brand_element)
        brand_element.click()
        time.sleep(1)


        self.click(*self.ADD_BRAND_BUTTON)
        time.sleep(1)
        self.click(*self.CANCEL_BUTTON)
        time.sleep(1)


        self.click(*self.VIEW_CONFIG_BUTTON)
        time.sleep(1)
        self.click(*self.CANCEL_CONFIG_BUTTON)
        time.sleep(1)


        brand_name_element = wait.until(EC.visibility_of_element_located(self.BRAND_NAME_TEXT))
        brand_name = brand_name_element.text

        self.type(*self.BRAND_NAME_INPUT, brand_name)
        time.sleep(1)


        search_result = wait.until(EC.visibility_of_element_located(self.BRAND_NAME_TEXT))
        assert brand_name in search_result.text, "Search result doesn't match brand name"
        time.sleep(1)
        # Clear the search box
        self.clear_and_reset(*self.BRAND_NAME_INPUT)
        time.sleep(3)
    
    def filter_by_status(self, status="Active"):
        wait = WebDriverWait(self.driver, 10)

        # Click the dropdown
        dropdown = wait.until(EC.element_to_be_clickable(self.DROPDOWN))
        dropdown.click()
        time.sleep(1)

        # Select the desired option
        if status.lower() == "active":
            option = wait.until(EC.element_to_be_clickable(self.DROPDOWN_OPTION_ACTIVE))
        elif status.lower() == "inactive":
            option = wait.until(EC.element_to_be_clickable(self.DROPDOWN_OPTION_INACTIVE))
        else:
            raise ValueError("Status must be 'Active' or 'Inactive'")

        option.click()
        time.sleep(1)

        cell = wait.until(EC.visibility_of_element_located(self.STATUS_COLUMN_CELL))
        assert status.lower() in cell.text.lower(), f"Expected status '{status}', but got '{cell.text}'"
    
    def click_brand_detail(self):
        wait = WebDriverWait(self.driver, 10)


        brand_detail_link = wait.until(EC.element_to_be_clickable(self.BRAND_DETAIL_LINK))
        brand_detail_link.click()
        time.sleep(2)


        assert "/brand-details/" in self.driver.current_url, f"Brand detail page did not load correctly. Current URL: {self.driver.current_url}"


        self.click(*self.BRAND_DETAIL_COMMERICALS_TAB)
        time.sleep(2)
        self.click(*self.BRAND_DETAIL_GST_TAB)
        time.sleep(2)
        self.click(*self.BRAND_DETAIL_WAREHOUSE_TAB)
        time.sleep(2)
        self.click(*self.BRAND_DETAIL_WEBHOOK_TAB)
        time.sleep(2)
        self.click(*self.BRAND_DETAIL_RULES_TAB)
        time.sleep(2)



