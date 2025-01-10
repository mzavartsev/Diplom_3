import time
from pages.main_page import *
from locators.main_page_locators import *
from locators.autorization_page_locators import *
from locators.profile_page_locators import *
from data import *
from time import sleep


class TestBasicFunctionality:
    def test_go_to_constructor(self, driver_start):
        class_object = MainPages()
        driver_start.get(LOGIN_PAGE_URL)
        class_object.find_element_with_wait(MainPageLocators.constructor, driver_start).click()
        assemble_the_burger_text = class_object.find_element_with_wait(MainPageLocators.assemble_the_burger_text,
                                                                      driver_start)
        assert assemble_the_burger_text.is_displayed()
