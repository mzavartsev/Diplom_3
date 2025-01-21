import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import *
from selenium.webdriver.common.action_chains import ActionChains


class BasePages:
    @allure.step('Находим элемент {locator}')
    def find_element_with_wait(self, locator, driver):
        element = WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        return element

    def find_test(self, locator, driver):
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
        WebDriverWait(driver, 15).until(expected_conditions.invisibility_of_element((By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V5')]/div")))
        self.find_element_with_wait(locator, driver).click()

    def create_order(self, driver_start):
        bun = self.find_element_with_wait(MainPageLocators.bun, driver_start)
        souse = self.find_element_with_wait(MainPageLocators.souse, driver_start)
        target_place = self.find_element_with_wait(MainPageLocators.target_place, driver_start)
        self.drag_and_drop(driver_start, bun, target_place)
        self.drag_and_drop(driver_start, souse, target_place)
        self.find_element_with_wait(MainPageLocators.create_order_button1, driver_start).click()

    def drag_and_drop(self, driver_start, source, target_place):
        if driver_start.capabilities["browserName"] == "firefox":
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
            """, source, target_place)
        else:
            actions = ActionChains(driver_start)
            actions.drag_and_drop(source, target_place).perform()

    def get_page(self, driver_start, page):
        driver_start.get(page)
        WebDriverWait(driver_start, 15).until(expected_conditions.invisibility_of_element((By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V5')]/div")))
