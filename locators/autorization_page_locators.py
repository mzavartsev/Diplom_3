from selenium.webdriver.common.by import By


class AutorizationPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text']")
    PASSWORD_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
