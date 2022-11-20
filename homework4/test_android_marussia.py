import pytest

from base import BaseCase


@pytest.mark.AndroidUI
class TestAndroid(BaseCase):

    def test_command_window_with_input_russia(self):
        self.main_page.open_keyboard()
        self.main_page.send_text_russia()
        name = self.main_page.get_name_country()
        description = self.main_page.get_description_country()

        assert name == 'Россия'
        assert description == 'Росси́я, или Росси́йская'

        # НАСЕЛЕНИЯ ЗЕМЛИ ТЕПЕРЬ НЕТУ В ВЫБОРЕ
        self.main_page.population_of_russia()
        population_russia = self.main_page.get_population_of_russia()

        assert population_russia == '146 млн.'

    def test_command_window_calculator(self):
        expression = '10 * 8 + 11'
        self.main_page.open_keyboard()
        self.main_page.send_expression(expression)
        answer = self.main_page.get_answer()

        assert str(eval(expression)) == answer

    def test_news_mail_ru(self):
        self.main_page.go_to_settings()
        self.settings_page.go_to_news_source_page()
        self.news_source_page.add_mail_ru_to_news_source()
        self.news_source_page.go_to_settings_page()
        self.settings_page.go_to_main_page()
        self.main_page.open_keyboard()
        self.main_page.send_keys_news()

        assert self.main_page.get_name_news_source()

    def test_about_app(self, get_version_apk):
        self.main_page.go_to_settings()
        self.settings_page.go_to_info_page()

        assert self.info_page.get_about_version() == get_version_apk
        assert self.info_page.get_about_copyright() == 'Все права защищены.'
