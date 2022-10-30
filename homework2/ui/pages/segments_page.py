from ui.locators.basic_locators import SegmentsPageLocators
from ui.pages.base_page import BasePage
from random_content.methods import random_text
import allure


class SegmentsPage(BasePage):

    locators = SegmentsPageLocators
    url = 'https://target-sandbox.my.com/segments'

    @allure.step
    def create_classroom_segment_app_and_games_in_social_networks(self):
        self.click(self.locators.CREATE_NEW_SEGMENT)
        self.click(self.locators.APPS_AND_GAMES)
        self.click(self.locators.PLAYED_AND_PAID_IN_PLATFORM)
        self.click(self.locators.PLAYED_IN_PLATFORM)
        self.click(self.locators.BUTTON_ADD_SEGMENT)
        self.input_text(self.locators.NAME_SEGMENT, random_text())
        self.click(self.locators.BUTTON_ADD_SEGMENTS)
        return self.get_text(self.locators.NAME_SEGMENT_IN_LIST)

    @allure.step
    def delete_classroom_segment_app_and_games_in_social_networks(self):
        self.click(self.locators.SELECT_SEGMENT)
        self.click(self.locators.ACTIONS)
        self.click(self.locators.REMOVE_SEGMENTS)
        return self.is_not_element_present(self.locators.NAME_SEGMENT_IN_LIST, 2)

    @allure.step
    def add_data_source_vk_edu(self):
        self.click(self.locators.GROUPS_VK_AND_OK)
        self.input_text(self.locators.INPUT_LINK_GROUPS_VK_AND_OK, 'https://vk.com/vkedu')
        self.click(self.locators.SELECT_ALL)
        self.click(self.locators.ADD_SELECTED)
        return self.find(self.locators.DATA_SOURCE_VK)

    @allure.step
    def delete_data_source_vk_edu(self):
        self.click(self.locators.REMOVE_DATA_SOURCE_VK)
        self.click(self.locators.CONFIRM_REMOVE)
        self.driver.refresh()
        return self.is_not_element_present(self.locators.DATA_SOURCE_VK, 5)
