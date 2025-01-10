import pytest
from selenium import webdriver
from data import *


@pytest.fixture(scope="session")
def driver_start():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)
    yield driver
    driver.quit()
