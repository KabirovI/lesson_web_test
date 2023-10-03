from tests.test_base import TestBase


class TestMainPage(TestBase):

    def test_go_to_tab_city(self):
        self.APP.actions_in_main_page.click_tab_city()
        print(123123123)