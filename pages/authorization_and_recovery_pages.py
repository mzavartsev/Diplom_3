import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class AuthorizationAndRecoveryPages:
    @allure.step('Находим элемент {locator}')
    def find_element_with_wait(self, locator, driver):
        element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return element

    @allure.step('Кликаем по элементу {locator}')
    def click_to_element(self, locator, driver):
        self.find_element_with_wait(locator, driver).click()

