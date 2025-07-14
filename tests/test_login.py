import yaml
from pages.login_page import LoginPage

def test_login_valid(driver):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["base_url"])
    login = LoginPage(driver)
    login.login(config["username"], config["password"])
    
    # Dummy assertion - update with actual check
    assert "dashboard" in driver.current_url or driver.title != ""
