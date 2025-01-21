from locators.recovery_page_locators import *
from pages.base_page import *
import time
from data import *
from locators.autorization_page_locators import *

class AuthorizationAndRecoveryPages(BasePages):
    @allure.step('Авторизуемся')
    def authorization(self, driver_start):
        self.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        email_field = self.find_element_with_wait(AutorizationPageLocators.email_field, driver_start)
        email_field.send_keys(CREDS["email"])
        password_field = self.find_element_with_wait(AutorizationPageLocators.password_field, driver_start)
        password_field.send_keys(CREDS['password'])
        self.find_element_with_wait(AutorizationPageLocators.login_button, driver_start).click()
        time.sleep(1)
        self.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()

    def recovery_password(self, driver_start):
        input_field = self.find_element_with_wait(RecoveryPageLocators.recovery_input_field, driver_start)
        input_field.send_keys(CREDS["email"])
        self.click_to_element(RecoveryPageLocators.recovery_button, driver_start)



