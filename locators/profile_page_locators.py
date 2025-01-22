from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    EXIT = (By.XPATH, "//button[text()='Выход']")