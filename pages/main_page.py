from pages.base_page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import *
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePages):
    @allure.step('Находим элемент после изменения предыдущего {locator}')
    def find_element_with_wait_for_changing_text(self, locator, driver, text='9999'):
        WebDriverWait(driver, 15).until_not(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.find_element_with_wait(locator, driver)

    @allure.step('Создаем новый заказ')
    def create_order(self, driver_start):
        bun = self.find_element_with_wait(MainPageLocators.BUN, driver_start)
        souse = self.find_element_with_wait(MainPageLocators.SOUSE, driver_start)
        target_place = self.find_element_with_wait(MainPageLocators.TARGET_PLACE, driver_start)
        self.drag_and_drop(driver_start, bun, target_place)
        self.drag_and_drop(driver_start, souse, target_place)
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON1, driver_start).click()

    @allure.step('Перетаскиваем ингредиент в заказ')
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