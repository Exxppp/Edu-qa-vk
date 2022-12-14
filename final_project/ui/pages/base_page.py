import time
from contextlib import contextmanager

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

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

    def get_text(self, locator, time_wait=10):
        text = ''
        for i in range(time_wait):
            el = self.find(locator)
            text = el.text
            if text:
                return text
            else:
                time.sleep(0.5)
        return text

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

    def move_and_click_to_next_element(self, locator_for_find, locator_for_click):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find(locator_for_find))
        actions.click(self.find(locator_for_click))
        actions.perform()

    def is_not_element_present(self, locator, timeout=None):
        if timeout is None:
            timeout = 10
        try:
            WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False
