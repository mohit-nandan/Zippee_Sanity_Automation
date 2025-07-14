import pytest
import yaml
from utils.driver_factory import create_driver

@pytest.fixture(scope="function")
def driver():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    driver = create_driver(config["browser"])
    yield driver
    driver.quit()
