from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    RECOVERY_PASSWORD_LINK = (By.XPATH, ".//*[text()='Восстановить пароль']")
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    RECOVERY_INPUT_FIELD = (By.XPATH, "//*[contains(@class, 'input__textfield')]")
    RECOVERY_PASSWORD_PASSWORD_FIELD = (By. XPATH, "//label[text()='Пароль']")
    EYE_ICON = (By. XPATH, "//div[contains(@class, 'icon input')]")
    RECOVERY_PASSWORD_TEXT = (By.XPATH, "//h2[text()='Восстановление пароля']")