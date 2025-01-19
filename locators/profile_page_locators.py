from selenium.webdriver.common.by import By


class ProfilePageLocators:
    order_history = (By.XPATH, "//a[text()='История заказов']")
    exit = (By.XPATH, "//button[text()='Выход']")