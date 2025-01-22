from locators.recovery_page_locators import *
from pages.base_page import *
import time
from data import *
from locators.autorization_page_locators import *


class AuthorizationAndRecoveryPages(BasePages):
    @allure.step('Авторизуемся')
    def authorization(self, driver_start):
        self.find_element_with_wait(MainPageLocators.PERSONAL_ACCOUNT, driver_start).click()
        email_field = self.find_element_with_wait(AutorizationPageLocators.EMAIL_FIELD, driver_start)
        email_field.send_keys(CREDS["email"])
        password_field = self.find_element_with_wait(AutorizationPageLocators.PASSWORD_FIELD, driver_start)
        password_field.send_keys(CREDS['password'])
        self.find_element_with_wait(AutorizationPageLocators.LOGIN_BUTTON, driver_start).click()
        time.sleep(1)
        self.find_element_with_wait(MainPageLocators.PERSONAL_ACCOUNT, driver_start).click()

    def recovery_password(self, driver_start):
        input_field = self.find_element_with_wait(RecoveryPageLocators.RECOVERY_INPUT_FIELD, driver_start)
        input_field.send_keys(CREDS["email"])
        self.click_to_element(RecoveryPageLocators.RECOVERY_BUTTON, driver_start)
