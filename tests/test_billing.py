import time
import pytest
from pages.Billing_page import BillingPage
@pytest.mark.order(5)
def test_billing_page(logged_in_driver):    
    billing_page = BillingPage(logged_in_driver)
    billing_page.view_billing()
    
    time.sleep(2)