# conftest.py
import pytest
from appium import webdriver
from config.appium_config import APPIUM_SERVER_URL, desired_caps

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote(APPIUM_SERVER_URL, desired_caps)
    yield driver
    driver.quit()
