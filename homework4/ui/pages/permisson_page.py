from ui.locators.locators_android import PermissionPageANDROIDLocators
from ui.locators.locators_web import PermissionPageLocators
from ui.pages.base_page import BasePage


class PermissionPage(BasePage):
    locators = PermissionPageLocators()

    def all_permission(self):
        pass


class PermissionPageANDROID(PermissionPage):
    locators = PermissionPageANDROIDLocators()

    def all_permission(self):
        self.click_for_android(self.locators.ADD_PERMISSION)
        self.click_for_android(self.locators.ADD_PERMISSION)
