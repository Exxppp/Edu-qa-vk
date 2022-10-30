import pytest
import allure
from base import BaseCase


@pytest.mark.UI
class TestUi(BaseCase):

    def test_create_company(self, file_path):
        self.logger.info('Ready to start')
        self.logger.info('Creating advertising campaign vk products ')

        assert self.dashboard_page.creating_advertising_campaign_vk_products(file_path)
        self.logger.info('Delete company')

        assert self.dashboard_page.delete_company()
        self.logger.info('End test')

    def test_create_segment_app_and_games_in_social_networks(self):
        self.logger.info('Ready to start')
        self.segments_page.open()
        self.logger.info('Creating segment app and games in social networks')

        assert self.segments_page.create_classroom_segment_app_and_games_in_social_networks()
        self.logger.info('Delete segment')

        assert self.segments_page.delete_classroom_segment_app_and_games_in_social_networks()
        self.logger.info('End test')

    def test_data_source_vk_edu(self):
        self.logger.info('Ready to start')
        self.segments_page.open()
        self.logger.info('Adding VK education group to data sources')

        assert self.segments_page.add_data_source_vk_edu()
        self.logger.info('Deleted data sources vk edu')

        assert self.segments_page.delete_data_source_vk_edu()
        self.logger.info('End test')
