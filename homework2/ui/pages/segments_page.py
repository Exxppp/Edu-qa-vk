import time

from ..locators.locators import SegmentsPageLocators
from .base_page import BasePage


class SegmentsPage(BasePage):

    locators = SegmentsPageLocators
    url = 'https://target-sandbox.my.com/segments'

    def create_classroom_segment(self, name_segment='my_new_segment'):
        self.click(self.locators.CREATE_NEW_SEGMENT)
        self.click(self.locators.APPS_AND_GAMES)
        self.click(self.locators.PLAYED_AND_PAID_IN_PLATFORM)
        self.click(self.locators.PLAYED_IN_PLATFORM)
        self.click(self.locators.BUTTON_ADD_SEGMENT)
        self.input_text(self.locators.NAME_SEGMENT, name_segment)
        self.click(self.locators.BUTTON_ADD_SEGMENTS)
        elem = self.get_text(self.locators.NAME_SEGMENT_IN_LIST)
        self.click(self.locators.SELECT_SEGMENT)
        self.click(self.locators.ACTIONS)
        self.click(self.locators.REMOVE_SEGMENTS)
        return elem

    def add_data_source_groups_list(self):
        self.click(self.locators.GROUPS_VK_AND_OK)
        self.input_text(self.locators.INPUT_LINK_GROUPS_VK_AND_OK, 'https://vk.com/vkedu')
        self.click(self.locators.SELECT_ALL)
        self.click(self.locators.ADD_SELECTED)
        elem = self.find(self.locators.DATA_SOURCE_VK)
        self.click(self.locators.REMOVE_DATA_SOURCE_VK)
        self.click(self.locators.CONFIRM_REMOVE)
        return elem
