import pytest
from base import BaseCase


@pytest.mark.UI
class TestAbc(BaseCase):

    def test_create_company(self, file_path):
        name_company = 'test company'
        assert self.dashboard_page.creating_advertising_campaign_vk_products(file_path,
                                                                             name_company=name_company) == name_company

    def test_create_segment(self):
        name_segment = 'test segment'
        page = self.segments_page
        page.open()
        assert page.create_classroom_segment(name_segment) == name_segment

    def test_add_groups_list(self):
        page = self.segments_page
        page.open()
        assert page.add_data_source_groups_list()
