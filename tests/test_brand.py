import time
import pytest
from pages.Brand_page import BrandPage

@pytest.mark.order(2)
def test_brand_page(logged_in_driver):
    brand_page = BrandPage(logged_in_driver)
    brand_page.create_brand()

    brand_page.filter_by_status("Active")
    time.sleep(1)
    brand_page.filter_by_status("Inactive")  
    time.sleep(1)
    brand_page.click_brand_detail()

