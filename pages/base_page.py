import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import *


class BasePages:
    @allure.step('Находим элемент {locator}')
    def find_element_with_wait(self, locator, driver):
        element = WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        return element

    @allure.step('Находим несколько элементов {locator}')
    def find_few_elements_with_wait(self, locator, driver):
        elements = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_all_elements_located(locator))
        return elements

    @allure.step('Кликаем по элементу {locator}')
    def click_to_element(self, locator, driver):
        WebDriverWait(driver, 15).until(expected_conditions.invisibility_of_element(MainPageLocators.MODAL_WINDOW3))
        self.find_element_with_wait(locator, driver).click()

    @allure.step('Переходим на страницу')
    def get_page(self, driver_start, page):
        driver_start.get(page)
        WebDriverWait(driver_start, 15).until(expected_conditions.invisibility_of_element(MainPageLocators.MODAL_WINDOW3))
