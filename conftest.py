import pytest
from selenium import webdriver
import requests
from data import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["chrome"])
def driver_start(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(BASE_URL)
    else:
        driver = webdriver.Firefox
        driver.set_window_size(1920, 1080)
        driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def create_and_delete_user():
    user = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=CREDS)
    return user.status_code, user.json(), user.text

