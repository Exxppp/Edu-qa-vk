from base import BaseCase


class TestReg(BaseCase):

    def test_reg_correct_user(self):
        self.register_page.register()

        assert self.driver.current_url == self.main_page.url
