from selenium.webdriver.common.by import By


class MainPageLocators:
    personal_account = (By.XPATH, "//*[text()='Личный Кабинет']")
    constructor = (By.XPATH, "//p[text()='Конструктор']")
    assemble_the_burger_text = (By.XPATH, "//h1[text()='Соберите бургер']")