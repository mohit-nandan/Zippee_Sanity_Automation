import pytest
from pages.Analtyics_page import AnalyticsPage

@pytest.mark.order(3)
def test_analytics_page(logged_in_driver):
    analytics = AnalyticsPage(logged_in_driver)
    analytics.view_analytics()

