# conftest.py
import pytest
from selenium import webdriver
import yaml
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def logged_in_driver(driver):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    driver.get(config["base_url"])
    login = LoginPage(driver)
    login.login(config["username"], config["password"])
    return driver
