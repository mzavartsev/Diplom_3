from pages.main_page import *
from locators.main_page_locators import *
from selenium.webdriver.common.action_chains import ActionChains
from data import *
from time import sleep


class TestBasicFunctionality:
    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Переход по клику на «Конструктор»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_go_to_constructor(self, driver_start, create_and_delete_user):
        class_object = MainPages()
        driver_start.get(LOGIN_PAGE_URL)
        class_object.find_element_with_wait(MainPageLocators.constructor, driver_start).click()
        assemble_the_burger_text = class_object.find_element_with_wait(
            MainPageLocators.assemble_the_burger_text,driver_start)
        assert assemble_the_burger_text.is_displayed()

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Переход по клику на «Лента заказов»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_got_to_order_feed(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.find_element_with_wait(MainPageLocators.order_feed_button, driver_start).click()
        order_feed_text = class_object.find_element_with_wait(MainPageLocators.order_feed_text, driver_start)
        assert order_feed_text.is_displayed()

    @allure.title("Eсли кликнуть на ингредиент, появится всплывающее окно с деталями")
    @allure.description("Eсли кликнуть на ингредиент, появится всплывающее окно с деталями")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_show_modal_window_after_click_on_the_ingredient(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.find_element_with_wait(MainPageLocators.bun, driver_start).click()
        modal_window = class_object.find_element_with_wait(MainPageLocators.section_locator, driver_start)
        assert "opened" in modal_window.get_attribute("class")

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.description("Всплывающее окно закрывается кликом по крестику")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_close_modal_window_about_ingredient(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        class_object.find_element_with_wait(MainPageLocators.bun, driver_start).click()
        class_object.find_element_with_wait(MainPageLocators.cross_in_modal_window, driver_start).click()
        modal_window = class_object.find_element_with_wait(MainPageLocators.section_locator, driver_start)
        assert "opened" not in modal_window.get_attribute("class")

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    @allure.description("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_increase_counter_of_ingredient_after_drag_and_drop(self, driver_start):
        class_object = MainPages()
        driver_start.get(BASE_URL)
        souse = class_object.find_element_with_wait(MainPageLocators.souse, driver_start)
        target_place = class_object.find_element_with_wait(MainPageLocators.target_place, driver_start)
        actions = ActionChains(driver_start)
        for i in range(4):
            actions.drag_and_drop(souse, target_place).perform()
        counter = class_object.find_element_with_wait_for_chaching_text(MainPageLocators.counter_of_souse, driver_start)
        assert counter.text == "4"

    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.description("Залогиненный пользователь может оформить заказ")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_create_order_after_authorization(self, driver_start):
        class_object = MainPages()
        driver_start.get(LOGIN_PAGE_URL)
        class_object.authorization(driver_start)
        driver_start.get(BASE_URL)
        class_object.create_order(driver_start)
        order_number = (class_object.find_element_with_wait_for_chaching_text
                        (MainPageLocators.number_of_order_after_create_order, driver_start)).text
        assert len(order_number) == 6


