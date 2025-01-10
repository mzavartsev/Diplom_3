from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    recovery_password_link = (By.XPATH, ".//*[text()='Восстановить пароль']")
    recovery_button = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    recovery_input_field = (By.XPATH, "//*[contains(@class, 'input__textfield')]")
    recovery_password_password_field = (By. XPATH, "//label[text()='Пароль']")
    eye_icon = (By. XPATH, "//div[contains(@class, 'icon input')]")

    # phone_field = (By.CSS_SELECTOR, "[placeholder = '* Телефон: на него позвонит курьер']")
    # next_button = (By.XPATH, ".//button[text()='Далее']")