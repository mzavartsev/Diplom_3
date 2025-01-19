import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.recovery_page_locators import *
from locators.main_page_locators import *
from data import *
from conftest import DRIVER_NAME


class AuthorizationAndRecoveryPages:
    @allure.step('Находим элемент {locator}')
    def find_element_with_wait(self, locator, driver):
        if DRIVER_NAME == "firefox":
            WebDriverWait(driver, 15).until_not(expected_conditions.invisibility_of_element_located(MainPageLocators.modal_window))
            element = WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(locator))
            return element
        else:
            element = WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(locator))
            return element

    @allure.step('Кликаем по элементу {locator}')
    def click_to_element(self, locator, driver):
        self.find_element_with_wait(locator, driver).click()

    def recovery_password(self, driver_start):
        input_field = self.find_element_with_wait(RecoveryPageLocators.recovery_input_field, driver_start)
        input_field.send_keys(CREDS["email"])
        self.find_element_with_wait(RecoveryPageLocators.recovery_button, driver_start).click()



