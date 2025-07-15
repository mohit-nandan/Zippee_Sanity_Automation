import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class BillingPage(BasePage):
     SIDEBAR_MENU = (By.CSS_SELECTOR, ".px-2")
     BILLING_NAME = (By.XPATH, "//span[normalize-space()='Billing']")
     GENERATE_INVOICE = (By.XPATH, "//button[normalize-space()='Generate Invoice']")
     GENERATE_INVOICE_CLOSE = (By.XPATH, "//button[normalize-space()='Cancel']")
     SEND_INVOICE = (By.XPATH, "//button[normalize-space()='Send Invoices']")
     SEND_INVOICE_CLOSE = (By.XPATH, "//button[normalize-space()='Cancel']")
     MG_ADJUSTMENT = (By.XPATH, "//button[normalize-space()='MG Adjustment']")
     MG_ADJUSTMENT_CLOSE = (By.XPATH, "//button[normalize-space()='Cancel']")
     DEDUCTION_VIEW = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[2]")
     INVOICE_VIEW = (By.XPATH, "//button[normalize-space()='Invoices']")
     PAGE_CHANGE_2 = (By.XPATH, "//button[normalize-space()='2']")
     PAGE_CHANGE_1 = (By.XPATH, "//button[normalize-space()='1']")


     def view_billing(self):
        wait = WebDriverWait(self.driver, 5)
        actions = ActionChains(self.driver)


        sidebar = wait.until(EC.presence_of_element_located(self.SIDEBAR_MENU))
        actions.move_to_element(sidebar).perform()

 
        billing = wait.until(EC.element_to_be_clickable(self.BILLING_NAME))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", billing)
        billing.click()

        wait.until(EC.url_contains("/billing"))
        time.sleep(1)

 
        self.click(*self.GENERATE_INVOICE)
        time.sleep(1)
        self.click(*self.GENERATE_INVOICE_CLOSE)
        time.sleep(1)

       
        self.click(*self.SEND_INVOICE)
        time.sleep(1)
        self.click(*self.SEND_INVOICE_CLOSE)   
        time.sleep(1)

        self.click(*self.MG_ADJUSTMENT)
        time.sleep(1)
        self.click(*self.MG_ADJUSTMENT_CLOSE)
        time.sleep(1)

        self.click(*self.DEDUCTION_VIEW)
        time.sleep(1)
       
        try:
            page_2_button = wait.until(EC.element_to_be_clickable(self.PAGE_CHANGE_2))
            page_2_button.click()
            time.sleep(1)


            page_1_button = wait.until(EC.element_to_be_clickable(self.PAGE_CHANGE_1))
            page_1_button.click()
            time.sleep(1)
        except Exception as e:
            print("Page 2 is not available, skipping pagination")
        
        self.click(*self.INVOICE_VIEW)
        time.sleep(1)
        
