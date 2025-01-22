from locators.profile_page_locators import *
from pages.authorization_and_recovery_pages import *
from data import *


class TestPersonalAccount:
    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Переход по клику на «Личный кабинет»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_go_to_personal_account_by_clicking_on_personal_account(self, driver_start, create_and_delete_user):
        class_object = AuthorizationAndRecoveryPages()
        class_object.authorization(driver_start)
        driver_start.get(PROFILE_PAGE_URL)
        assert driver_start.current_url == PROFILE_PAGE_URL

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Переход в раздел «История заказов»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_go_to_order_history(self, driver_start, create_and_delete_user):
        class_object = AuthorizationAndRecoveryPages()
        class_object.authorization(driver_start)
        class_object.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY, driver_start).click()
        assert driver_start.current_url == ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта.")
    @allure.description("Выход из аккаунта.")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_logout(self, driver_start, create_and_delete_user):
        class_object = AuthorizationAndRecoveryPages()
        class_object.authorization(driver_start)
        class_object.find_element_with_wait(ProfilePageLocators.EXIT, driver_start).click()
        class_object.click_to_element(MainPageLocators.PERSONAL_ACCOUNT, driver_start)
        assert driver_start.current_url == LOGIN_PAGE_URL
