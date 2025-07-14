import pytest
from pages.Emergency_page import EmergencyPage

@pytest.mark.order(4)
def test_emergency_page(logged_in_driver):
    emergency_page = EmergencyPage(logged_in_driver)
    emergency_page.view_emergency()

