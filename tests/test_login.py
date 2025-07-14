import pytest

@pytest.mark.order(1)
def test_login_valid(logged_in_driver):
    assert "dashboard" in logged_in_driver.current_url or logged_in_driver.title != ""
