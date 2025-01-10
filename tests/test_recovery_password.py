import time
from pages.authorization_and_recovery_pages import *
from locators.recovery_page_locators import *
from data import *


class TestRecoveryPassword:
    def test_transition_to_page_recovery_using_the_recover_password_link(self, driver_start):
        class_object = AuthorizationAndRecoveryPages()
        driver_start.get(LOGIN_PAGE_URL)
        class_object.find_element_with_wait(RecoveryPageLocators.recovery_password_link, driver_start).click()
        assert driver_start.current_url == FORGOT_PASSWORD_URL

    def test_transition_to_page_recovery_using_the_recover_password_button(self, driver_start):
        class_object = AuthorizationAndRecoveryPages()
        driver_start.get(FORGOT_PASSWORD_URL)
        input_field = class_object.find_element_with_wait(RecoveryPageLocators.recovery_input_field, driver_start)
        input_field.send_keys(CREDS["email"])
        class_object.find_element_with_wait(RecoveryPageLocators.recovery_button, driver_start).click()
        time.sleep(5)
        assert driver_start.current_url == RESET_PASSWORD_PAGE_URL

    def test_show_click_on_eye_making_the_field_active(self, driver_start):
        class_object = AuthorizationAndRecoveryPages()
        driver_start.get(FORGOT_PASSWORD_URL)
        input_field = class_object.find_element_with_wait(RecoveryPageLocators.recovery_input_field, driver_start)
        input_field.send_keys(CREDS["email"])
        class_object.find_element_with_wait(RecoveryPageLocators.recovery_button, driver_start).click()
        time.sleep(3)
        recovery_password_field = class_object.find_element_with_wait(RecoveryPageLocators.recovery_input_field,
                                                                      driver_start)
        recovery_password_field.send_keys("123123123")
        time.sleep(3)
        class_object.find_element_with_wait(RecoveryPageLocators.eye_icon, driver_start).click()
        time.sleep(3)
        interact_input_field = class_object.find_element_with_wait(RecoveryPageLocators.recovery_password_password_field, driver_start)
        assert "input__placeholder-focused" in interact_input_field.get_attribute("class")