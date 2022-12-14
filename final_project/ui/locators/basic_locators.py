from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.CSS_SELECTOR, '#username')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#password')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '#submit')
    BUTTON_GO_TO_REG = (By.XPATH, '//a[@href="/reg"]')
    ALERT = (By.CSS_SELECTOR, '#flash')


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
    ALERT = (By.CSS_SELECTOR, '#flash')


class MainPageLocators:
    LOGOUT = (By.XPATH, '//a[@href="/logout"]')
    HOME = (By.XPATH, '//a[text()="HOME"]')
    PYTHON = (By.XPATH, '//li[@class="uk-parent"][1]')
    PYTHON_HISTORY = (By.XPATH, '((//ul[@class="uk-nav uk-nav-navbar"])[1]//a)[1]')
    ABOUT_FLASK = (By.XPATH, '((//ul[@class="uk-nav uk-nav-navbar"])[1]//a)[2]')
    LINUX = (By.XPATH, '//li[@class="uk-parent"][2]')
    CENTOS_DOWNLOAD = (By.XPATH, '((//ul[@class="uk-nav uk-nav-navbar"])[2]//a)[1]')
    NETWORK = (By.XPATH, '//li[@class="uk-parent"][3]')
    WIRESHARK_NEWS = (By.XPATH, '(//ul[@class="uk-nav-sub"]//a)[1]')
    WIRESHARK_DOWNLOAD = (By.XPATH, '(//ul[@class="uk-nav-sub"]//a)[2]')
    TCPDUMP_EXAMPLES = (By.XPATH, '//a[text()="Examples "]')
    WHAT_IS_AN_API = (By.XPATH, '(//figure[@class="uk-overlay uk-overlay-hover"])[1]/a')
    FUTURE_OF_INTERNET = (By.XPATH, '(//figure[@class="uk-overlay uk-overlay-hover"])[2]/a')
    SMTP = (By.XPATH, '(//figure[@class="uk-overlay uk-overlay-hover"])[3]/a')
    USERNAME_INFO = (By.XPATH, '//div[@id="login-name"]//li[1]')
    NAMES_INFO = (By.XPATH, '//div[@id="login-name"]//li[2]')
    VK_ID_INFO = (By.XPATH, '//div[@id="login-name"]//li[3]')
