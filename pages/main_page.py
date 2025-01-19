import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import *
from locators.autorization_page_locators import *
from selenium.webdriver.common.action_chains import ActionChains
from data import *
from conftest import DRIVER_NAME


class MainPages:
    @allure.step('Находим элемент {locator}')
    def find_element_with_wait(self, locator, driver):
        element = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return element

    @allure.step('Находим несколько элементов {locator}')
    def find_few_elements_with_wait(self, locator, driver):
        elements = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_all_elements_located(locator))
        return elements

    @allure.step('Находим элемент после изменения предыдущего {locator}')
    def find_element_with_wait_for_chaching_text(self, locator, driver, text='9999'):
        WebDriverWait(driver, 15).until_not(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.find_element_with_wait(locator, driver)

    @allure.step('Кликаем по элементу {locator}')
    def click_to_element(self, locator, driver):
        self.find_element_with_wait(locator, driver).click()

    @allure.step('Авторизуемся')
    def authorization(self, driver_start):
        self.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()
        email_field = self.find_element_with_wait(AutorizationPageLocators.email_field, driver_start)
        email_field.send_keys(CREDS["email"])
        password_field = self.find_element_with_wait(AutorizationPageLocators.password_field, driver_start)
        password_field.send_keys(CREDS['password'])
        self.find_element_with_wait(AutorizationPageLocators.login_button, driver_start).click()
        time.sleep(1)
        self.find_element_with_wait(MainPageLocators.personal_account, driver_start).click()

    def create_order(self, driver_start):
        if DRIVER_NAME == "firefox":
            bun = self.find_element_with_wait(MainPageLocators.bun, driver_start)
            souse = self.find_element_with_wait(MainPageLocators.souse, driver_start)
            target_place = self.find_element_with_wait(MainPageLocators.target_place, driver_start)
            driver_start.execute_script("""
                var src = arguments[0];
                var target = arguments[1];
                var dataTransfer = { data: {} };
                var dragEvent = new MouseEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    view: window
                });
                var dropEvent = new MouseEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    view: window
                });
                src.dispatchEvent(dragEvent);
                target.dispatchEvent(dropEvent);
            """, bun, target_place)
            self.find_element_with_wait(MainPageLocators.create_order_button1, driver_start).click()
        else:
            bun = self.find_element_with_wait(MainPageLocators.bun, driver_start)
            souse = self.find_element_with_wait(MainPageLocators.souse, driver_start)
            target_place = self.find_element_with_wait(MainPageLocators.target_place, driver_start)
            actions = ActionChains(driver_start)
            actions.drag_and_drop(souse, target_place).perform()
            actions.drag_and_drop(bun, target_place).perform()
            self.find_element_with_wait(MainPageLocators.create_order_button1, driver_start).click()
