import time
from pages.authorization_and_recovery_pages import *
from locators.recovery_page_locators import *
from data import *


class TestRecoveryPassword:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.description("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_transition_to_page_recovery_using_the_recover_password_link(self, driver_start, create_and_delete_user):
        class_object = AuthorizationAndRecoveryPages()
        driver_start.get(LOGIN_PAGE_URL)
        time.sleep(3)
        class_object.find_element_with_wait(RecoveryPageLocators.recovery_password_link, driver_start).click()
        assert driver_start.current_url == FORGOT_PASSWORD_URL

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description("Ввод почты и клик по кнопке «Восстановить»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_transition_to_page_recovery_using_the_recover_password_button(self, driver_start):
        class_object = AuthorizationAndRecoveryPages()
        driver_start.get(FORGOT_PASSWORD_URL)
        time.sleep(3)
        class_object.recovery_password(driver_start)
        recovery_text = class_object.find_element_with_wait(RecoveryPageLocators.recovery_password_text, driver_start)
        assert recovery_text.is_displayed()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    @allure.description("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_show_click_on_eye_making_the_field_active(self, driver_start):
        class_object = AuthorizationAndRecoveryPages()
        driver_start.get(FORGOT_PASSWORD_URL)
        time.sleep(3)
        class_object.recovery_password(driver_start)
        time.sleep(3)
        recovery_password_field = class_object.find_element_with_wait(
            RecoveryPageLocators.recovery_input_field, driver_start)
        recovery_password_field.send_keys("123123123")
        class_object.find_element_with_wait(RecoveryPageLocators.eye_icon, driver_start).click()
        interact_input_field = class_object.find_element_with_wait(
            RecoveryPageLocators.recovery_password_password_field, driver_start)
        assert "input__placeholder-focused" in interact_input_field.get_attribute("class")