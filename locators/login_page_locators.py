from selenium.webdriver.common.by import By


class LoginPageLocatoirs:
    recovery_password_button = (By.XPATH, ".//*[text()='Восстановить пароль']")
    recovery_input_field = (By.XPATH, "//*[contains(@class, 'input__textfield')]")