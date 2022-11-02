import os
import allure
import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.segments_page import SegmentsPage
import allure


class BaseCase:
    driver = None
    authorize = True

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
        test_log = os.path.join(temp_dir, 'test.log')
        with open(test_log, 'r') as f:
            allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)
        if failed_test_count < request.session.testsfailed:
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            self.driver.save_screenshot(filename=screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)

    @allure.step('setup')
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.dashboard_page: DashboardPage = (request.getfixturevalue('dashboard_page'))
        self.segments_page: SegmentsPage = (request.getfixturevalue('segments_page'))
        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        if self.authorize:
            login_page = LoginPage(self.driver)
            login_page.login()
