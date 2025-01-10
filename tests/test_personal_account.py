import time
from pages.main_page import *
from locators.main_page_locators import *
from locators.autorization_page_locators import *
from locators.profile_page_locators import *
from data import *
from time import sleep


class TestPersonalAccount:
    def test_go_to_personal_account_by_clicking_on_personal_account(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        email_field = class_object.find_element_with_wait(AutorizationPageLocators.email_field, driver_start)
        email_field.send_keys(CREDS["email"])
        password_field = class_object.find_element_with_wait(AutorizationPageLocators.password_field, driver_start)
        password_field.send_keys(CREDS['password'])
        class_object.find_element_with_wait(AutorizationPageLocators.login_button, driver_start).click()
        class_object.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        sleep(3)
        assert driver_start.current_url == PROFILE_PAGE_URL

    def test_go_to_order_history(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        email_field = class_object.find_element_with_wait(AutorizationPageLocators.email_field, driver_start)
        email_field.send_keys(CREDS["email"])
        password_field = class_object.find_element_with_wait(AutorizationPageLocators.password_field, driver_start)
        password_field.send_keys(CREDS['password'])
        class_object.find_element_with_wait(AutorizationPageLocators.login_button, driver_start).click()
        class_object.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        class_object.find_element_with_wait(ProfilePageLocators.order_history, driver_start).click()
        assert  driver_start.current_url == ORDER_HISTORY_URL

    def test_logout(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        email_field = class_object.find_element_with_wait(AutorizationPageLocators.email_field, driver_start)
        email_field.send_keys(CREDS["email"])
        password_field = class_object.find_element_with_wait(AutorizationPageLocators.password_field, driver_start)
        password_field.send_keys(CREDS['password'])
        class_object.find_element_with_wait(AutorizationPageLocators.login_button, driver_start).click()
        class_object.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        class_object.find_element_with_wait(ProfilePageLocators.exit, driver_start).click()
        class_object.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        assert driver_start.current_url == LOGIN_PAGE_URL
