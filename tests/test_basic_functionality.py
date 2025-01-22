from pages.authorization_and_recovery_pages import *
from data import *


class TestBasicFunctionality:
    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Переход по клику на «Конструктор»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_go_to_constructor(self, driver_start, create_and_delete_user):
        class_object = BasePages()
        class_object.get_page(driver_start, LOGIN_PAGE_URL)
        class_object.find_element_with_wait(MainPageLocators.CONSTRUCTOR, driver_start).click()
        assemble_the_burger_text = class_object.find_element_with_wait(
            MainPageLocators.ASSEMBLE_THE_BURGER_TEXT, driver_start)
        assert assemble_the_burger_text.is_displayed()

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Переход по клику на «Лента заказов»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_got_to_order_feed(self, driver_start):
        class_object = BasePages()
        class_object.find_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON, driver_start).click()
        order_feed_text = class_object.find_element_with_wait(MainPageLocators.ORDER_FEED_TEXT, driver_start)
        assert order_feed_text.is_displayed()

    @allure.title("Eсли кликнуть на ингредиент, появится всплывающее окно с деталями")
    @allure.description("Eсли кликнуть на ингредиент, появится всплывающее окно с деталями")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_show_modal_window_after_click_on_the_ingredient(self, driver_start):
        class_object = BasePages()
        class_object.find_element_with_wait(MainPageLocators.BUN, driver_start).click()
        modal_window = class_object.find_element_with_wait(MainPageLocators.SECTION_LOCATOR, driver_start)
        assert "opened" in modal_window.get_attribute("class")

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.description("Всплывающее окно закрывается кликом по крестику")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_close_modal_window_about_ingredient(self, driver_start):
        class_object = BasePages()
        class_object.find_element_with_wait(MainPageLocators.BUN, driver_start).click()
        modal_window = class_object.find_element_with_wait(MainPageLocators.SECTION_LOCATOR, driver_start)
        class_object.find_element_with_wait(MainPageLocators.CROSS_IN_MODAL_WINDOW, driver_start).click()
        WebDriverWait(driver_start, 10).until(expected_conditions.invisibility_of_element
                                              (MainPageLocators.SECTION_LOCATOR))
        assert not modal_window.is_displayed()

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    @allure.description("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_increase_counter_of_ingredient_after_drag_and_drop(self, driver_start):
        class_object = BasePages()
        souse = class_object.find_element_with_wait(MainPageLocators.SOUSE, driver_start)
        target_place = class_object.find_element_with_wait(MainPageLocators.TARGET_PLACE, driver_start)
        for i in range(4):
            class_object.drag_and_drop(driver_start, souse, target_place)
        counter = class_object.find_element_with_wait_for_chaching_text(MainPageLocators.COUNTER_OF_SOUSE, driver_start)
        assert counter.text == "4"

    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.description("Залогиненный пользователь может оформить заказ")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_create_order_after_authorization(self, driver_start, create_and_delete_user):
        class_object = AuthorizationAndRecoveryPages()
        class_object.get_page(driver_start, LOGIN_PAGE_URL)
        class_object.authorization(driver_start)
        class_object.get_page(driver_start, BASE_URL)
        class_object.create_order(driver_start)
        order_number = (class_object.find_element_with_wait_for_chaching_text
                        (MainPageLocators.NUMBER_OF_ORDER_AFTER_CREATE_ORDER, driver_start)).text
        assert len(order_number) == 6
