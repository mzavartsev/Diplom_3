import time

from pages.main_page import *
from locators.main_page_locators import *
from data import *


class TestSectionOrderFeed:
    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    @allure.description("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_show_details_of_order(self, driver_start, create_and_delete_user):
        class_object = MainPages()
        driver_start.get(ORDER_FEED_URL)
        class_object.find_element_with_wait(MainPageLocators.order_in_order_feed, driver_start).click()
        modal_window = class_object.find_element_with_wait(MainPageLocators.section_open_locator, driver_start)
        assert "opened" in modal_window.get_attribute("class")

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    @allure.description("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_user_orders_displayed_on_the_order_feed(self, driver_start):
        class_object = MainPages()
        driver_start.get(LOGIN_PAGE_URL)
        class_object.authorization(driver_start)
        driver_start.get(BASE_URL)
        class_object.create_order(driver_start)
        order_number_element = (class_object.find_element_with_wait_for_chaching_text
                                (MainPageLocators.number_of_order_after_create_order, driver_start))
        order_number = order_number_element.text
        driver_start.get(ORDER_FEED_URL)
        order_status_box = class_object.find_element_with_wait(MainPageLocators.order_status_box, driver_start).text
        assert order_number in order_status_box

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    @allure.description("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_counter_of_completed_order_for_all_time_increases(self, driver_start):
        class_object = MainPages()
        driver_start.get(ORDER_FEED_URL)
        counters = class_object.find_few_elements_with_wait(MainPageLocators.counters_of_created, driver_start)
        counter_one_before = counters[0].text
        driver_start.get(LOGIN_PAGE_URL)
        class_object.authorization(driver_start)
        driver_start.get(BASE_URL)
        class_object.create_order(driver_start)
        driver_start.get(ORDER_FEED_URL)
        counters = class_object.find_few_elements_with_wait(MainPageLocators.counters_of_created,
                                                                                  driver_start)
        counter_one_after = counters[0].text
        assert int(counter_one_before) <= int(counter_one_after)

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    @allure.description("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_counter_of_completed_order_for_today_increases(self, driver_start):
        class_object = MainPages()
        driver_start.get(ORDER_FEED_URL)
        counters = class_object.find_few_elements_with_wait(MainPageLocators.counters_of_created, driver_start)
        counter_two_before = counters[1].text
        driver_start.get(LOGIN_PAGE_URL)
        class_object.authorization(driver_start)
        driver_start.get(BASE_URL)
        class_object.create_order(driver_start)
        driver_start.get(ORDER_FEED_URL)
        counters = class_object.find_few_elements_with_wait(MainPageLocators.counters_of_created, driver_start)
        counter_two_after = counters[1].text
        assert int(counter_two_before) <= int(counter_two_after)

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    @allure.description("После оформления заказа его номер появляется в разделе В работе")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/")
    def test_show_number_of_order_after_create(self, driver_start, create_and_delete_user):
        class_object = MainPages()
        driver_start.get(LOGIN_PAGE_URL)
        class_object.authorization(driver_start)
        driver_start.get(BASE_URL)
        class_object.create_order(driver_start)
        order_number_element = class_object.find_element_with_wait_for_chaching_text(
            MainPageLocators.number_of_order_after_create_order, driver_start)
        order_number = order_number_element.text
        time.sleep(2)
        driver_start.get(ORDER_FEED_URL)
        numbers_at_work = class_object.find_element_with_wait_for_chaching_text(MainPageLocators.order_number_at_work, driver_start, text="Все текущие заказы готовы!")
        class_object.find_element_with_wait_for_chaching_text(MainPageLocators.order_number_at_work1, driver_start, text="Все текущие заказы готовы!")
        number_of_li = numbers_at_work.find_elements(By.TAG_NAME, "li")
        for i in range(len(number_of_li)):
            number_of_li[i] = int(number_of_li[i].text)
        # numbers_at_work = list(map(lambda x: int(x.text), numbers_at_work))
        assert int(order_number) in number_of_li
