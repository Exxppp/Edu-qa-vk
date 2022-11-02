from ui.locators.basic_locators import SegmentsPageLocators
from ui.pages.base_page import BasePage
from random_content.methods import generate_random_text
import allure


class SegmentsPage(BasePage):

    locators = SegmentsPageLocators
    url = 'https://target-sandbox.my.com/segments'

    @allure.step('create segment')
    def create_classroom_segment_app_and_games_in_social_networks(self):
        self.driver.get(self.url + '/segments_list/new/')
        self.click(self.locators.APPS_AND_GAMES)
        self.click(self.locators.PLAYED_AND_PAID_IN_PLATFORM)
        self.click(self.locators.PLAYED_IN_PLATFORM)
        self.click(self.locators.BUTTON_ADD_SEGMENT)
        self.input_text(self.locators.NAME_SEGMENT, generate_random_text())
        self.click(self.locators.BUTTON_CREATE_SEGMENT)
        return self.get_text(self.locators.NAME_SEGMENT_IN_LIST)

    @allure.step('delete segment')
    def delete_segment(self):
        self.click(self.locators.SELECT_SEGMENT)
        self.click(self.locators.ACTIONS)
        self.click(self.locators.REMOVE_SEGMENTS)
        return self.is_not_element_present(self.locators.NAME_SEGMENT_IN_LIST, 2)

    @allure.step('adding vk edu to the data source')
    def add_data_source_vk_edu(self):
        self.click(self.locators.GROUPS_VK_AND_OK)
        self.input_text(self.locators.INPUT_LINK_GROUPS_VK_AND_OK, 'https://vk.com/vkedu')
        self.click(self.locators.SELECT_ALL)
        self.click(self.locators.ADD_SELECTED)
        return self.find(self.locators.DATA_SOURCE_VK)

    @allure.step('deleting vk edu in the data source')
    def delete_data_source_vk_edu(self):
        self.click(self.locators.GROUPS_VK_AND_OK)
        self.click(self.locators.REMOVE_DATA_SOURCE_VK)
        self.click(self.locators.CONFIRM_REMOVE)
        self.driver.refresh()
        return self.is_not_element_present(self.locators.DATA_SOURCE_VK, 5)

    @allure.step('creating segment vk edu')
    def create_segment_vk_edu(self):
        self.click(self.locators.SEGMENT_LIST)
        self.click(self.locators.CREATE_NEW_SEGMENT)
        self.click(self.locators.SEGMENT_VK_AND_OK)
        self.click(self.locators.SELECT_GROUP_VK)
        self.click(self.locators.BUTTON_ADD_SEGMENT)
        self.input_text(self.locators.NAME_SEGMENT, generate_random_text())
        self.click(self.locators.BUTTON_CREATE_SEGMENT)
        return self.get_text(self.locators.NAME_SEGMENT_IN_LIST)

    @allure.step('count segments')
    def count_segments(self):
        self.open()
        count = self.driver.find_elements(*self.locators.COUNT_SEGMENTS)

        return len(count)

