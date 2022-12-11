from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, '#username')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#password')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '#submit')
    BUTTON_GO_TO_REG = (By.XPATH, '//a[@href="/reg"]')


class RegisterPageLocators:
    INPUT_NAME = (By.CSS_SELECTOR, '#user_name')
    INPUT_SURNAME = (By.CSS_SELECTOR, '#user_surname')
    INPUT_MIDDLENAME = (By.CSS_SELECTOR, '#user_middle_name')
    INPUT_USERNAME = (By.CSS_SELECTOR, '#username')
    INPUT_EMAIL = (By.CSS_SELECTOR, '#email')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#password')
    INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, '#confirm')
    ACCEPT = (By.CSS_SELECTOR, '#term')
    BUTTON_REG = (By.CSS_SELECTOR, '#submit')
    BUTTON_GO_TO_LOGIN = (By.XPATH, '//a[@href="/login"]')


class MainPageLocators:
    LOGOUT = (By.XPATH, '//a[@href="/logout"]')

