from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    url = 'https://target-sandbox.my.com/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        if self.driver.current_url == self.url:
            return
        self.driver.get(self.url)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 25
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout=None):
        return self.wait(timeout).until(method=EC.presence_of_all_elements_located(locator))

    def get_text(self, locator):
        return self.find(locator).text

    def input_text(self, locator, query):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(query)

    def upload_file(self, locator, file_path):
        element = self.find(locator)
        element.send_keys(file_path)

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_not_element_present(self, locator, timeout=None):
        if timeout is None:
            timeout = 10
        try:
            WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False
