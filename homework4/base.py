import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.info_page import InfoPage
from ui.pages.main_page import MainPage
from ui.pages.permisson_page import PermissionPage
from ui.pages.settings_page import SettingsPage
from ui.pages.news_source_page import NewsSourcePage


class BaseCase:
    INSTALL_MARUSSIA = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger, ui_report):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.permission_page: PermissionPage = request.getfixturevalue('permission_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.settings_page: SettingsPage = request.getfixturevalue('settings_page')
        self.info_page: InfoPage = request.getfixturevalue('info_page')
        self.news_source_page: NewsSourcePage = request.getfixturevalue('news_source_page')

        self.logger.debug('Initial setup done!')
        if self.INSTALL_MARUSSIA:
            self.permission_page.all_permission()

