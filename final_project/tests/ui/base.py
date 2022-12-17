import os
from contextlib import contextmanager

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from builder import Builder
from mysql.client import MysqlClient
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.register_page import RegisterPage


class BaseCase:

    driver = None
    authorize = False

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        browser_logs = os.path.join(temp_dir, 'browser.log')
        with open(browser_logs, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
        with open(browser_logs, 'r') as f:
            allure.attach(f.read(), 'browser.log', allure.attachment_type.TEXT)
        if failed_test_count < request.session.testsfailed:
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            self.driver.save_screenshot(filename=screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, mysql_client, request):
        self.driver: WebDriver = driver
        self.builder = Builder()
        self.mysql: MysqlClient = mysql_client

        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        self.register_page: RegisterPage = (request.getfixturevalue('register_page'))
        self.main_page: MainPage = (request.getfixturevalue('main_page'))

        if self.authorize:
            name, value = request.getfixturevalue('cookies_ui')
            self.base_page.open()
            driver.add_cookie({'name': name, 'value': value})
            self.driver.refresh()
            self.auth_user_data = request.config.user_data
