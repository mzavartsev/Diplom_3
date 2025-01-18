from pages.main_page import *
from locators.main_page_locators import *
from locators.profile_page_locators import *
from data import *
from time import sleep


class TestPersonalAccount:
    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Переход по клику на «Личный кабинет»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_go_to_personal_account_by_clicking_on_personal_account(self, driver_start, create_and_delete_user):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.authorization(driver_start)
        driver_start.get(PROFILE_PAGE_URL)
        assert driver_start.current_url == PROFILE_PAGE_URL

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Переход в раздел «История заказов»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_go_to_order_history(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.authorization(driver_start)
        class_object.find_element_with_wait(ProfilePageLocators.order_history, driver_start).click()
        assert  driver_start.current_url == ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта.")
    @allure.description("Выход из аккаунта.")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_logout(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.authorization(driver_start)
        class_object.find_element_with_wait(ProfilePageLocators.exit, driver_start).click()
        class_object.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        assert driver_start.current_url == LOGIN_PAGE_URL

