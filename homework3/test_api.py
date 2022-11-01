from base import ApiBase
import pytest


@pytest.mark.API
class TestApi(ApiBase):

    def test_create_company(self):
        self.api_client.create_company()

        assert self.api_client.id_last_company
        self.api_client.delete_company(self.api_client.id_last_company)

    def test_create_segment(self):
        self.api_client.create_segment()

        assert self.api_client.id_last_segment_in_audience
        self.api_client.delete_segment_in_audience(self.api_client.id_last_segment_in_audience)

    def test_create_data_source_vk_edu(self):
        self.api_client.create_data_source_vk_edu()
        self.api_client.create_segment_vk_group()

        assert self.api_client.id_last_groups
        assert self.api_client.id_last_segment_in_audience
        self.api_client.delete_segment_in_audience(self.api_client.id_last_segment_in_audience)
        self.api_client.delete_data_source_vk_group(self.api_client.id_last_groups)
