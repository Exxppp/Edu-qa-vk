import pytest
from base import BaseCase


@pytest.mark.UI
class TestUi(BaseCase):

    def test_create_company(self, file_path):
        count_start = self.dashboard_page.count_companies()
        self.logger.info('Ready to start')
        self.logger.info('Creating advertising campaign vk products ')
        self.dashboard_page.creating_advertising_campaign_vk_products(file_path)
        count_end = self.dashboard_page.count_companies()

        assert self.dashboard_page.get_name_company()
        assert count_end - count_start == 1
        self.logger.info('Delete company')
        self.dashboard_page.delete_company()
        self.logger.info('End test')

    def test_create_segment_app_and_games_in_social_networks(self):
        self.logger.info('Ready to start')
        self.segments_page.open()
        count_start = self.segments_page.count_segments()
        self.logger.info('Creating segment app and games in social networks')

        assert self.segments_page.create_classroom_segment_app_and_games_in_social_networks()
        self.logger.info('Add 2 segment')
        self.segments_page.create_classroom_segment_app_and_games_in_social_networks()
        count_end = self.segments_page.count_segments()

        assert count_end - count_start == 2
        self.logger.info('Delete segment')
        self.segments_page.delete_segment()
        self.segments_page.delete_segment()
        self.logger.info('End test')

    def test_data_source_vk_edu(self):
        self.logger.info('Ready to start')
        self.segments_page.open()
        count_start = self.segments_page.count_segments()
        self.logger.info('Adding VK education group to data sources')
        self.segments_page.add_data_source_vk_edu()
        self.logger.info('Creating a segment with a data source VK edu')
        name_segment = self.segments_page.create_segment_vk_edu()
        count_end = self.segments_page.count_segments()

        assert name_segment
        assert count_end - count_start == 1
        self.logger.info('Deleted segment vk edu')
        self.segments_page.delete_segment()
        self.logger.info('Deleted data sources vk edu')
        self.segments_page.delete_data_source_vk_edu()
        self.logger.info('End test')
