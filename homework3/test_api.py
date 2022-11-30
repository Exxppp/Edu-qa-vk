import pytest

from base import BaseCaseApi


@pytest.mark.API
class TestApi(BaseCaseApi):

    def test_create_company(self):
        name = self.builder.company().name
        self.api_client.create_company(name)

        assert self.api_client.id_last_company
        assert self.api_client.get_name_company() == name

        self.api_client.get_name_company()
        self.api_client.delete_company(self.api_client.id_last_company)

    def test_create_segment(self):
        name = self.builder.segments().name
        self.api_client.create_segment(name)

        assert self.api_client.id_last_segment_in_audience
        assert self.api_client.get_name_segment() == name

        self.api_client.delete_segment_in_audience(self.api_client.id_last_segment_in_audience)

    def test_create_data_source_vk_edu(self):
        name = self.builder.segments().name
        self.api_client.create_data_source_vk_edu()
        self.api_client.create_segment_vk_group(name)

        assert self.api_client.id_last_groups
        assert self.api_client.id_last_segment_in_audience
        assert self.api_client.get_name_segment() == name

        self.api_client.delete_segment_in_audience(self.api_client.id_last_segment_in_audience)
        self.api_client.delete_data_source_vk_group(self.api_client.id_last_groups)
