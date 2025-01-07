import pytest
from selenium import webdriver
from data import *


@pytest.fixture(scope="module")
def driver_start():
    driver = webdriver.Firefox()
    driver.set_window_size(1024, 768)
    driver.get(BASE_URL)
    yield driver
    driver.quit()
