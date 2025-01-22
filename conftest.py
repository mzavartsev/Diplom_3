import pytest
from selenium import webdriver
import requests
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *
from selenium.webdriver.support import expected_conditions


DRIVER_NAME = None

@pytest.fixture(params=["chrome","firefox"])
def driver_start(request):
    global DRIVER_NAME
    if request.param == "chrome":
        DRIVER_NAME = "chrome"
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(BASE_URL)
    else:
        DRIVER_NAME = "firefox"
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(BASE_URL)
        WebDriverWait(driver, 15).until(expected_conditions.invisibility_of_element((MainPageLocators.MODAL_WINDOW3)))
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def create_and_delete_user():
    user = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register",
                         data=CREDS)
    token = user.json()["accessToken"]
    auth_token = {"authorization": token}
    yield user.status_code, user.json(), user.text
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user",
                                  headers=auth_token)
