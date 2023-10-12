import time

from tests.test_base import TestBase


class TestMainPage(TestBase):

    def test_go_to_tab_city(self):
        self.APP.actions_in_main_page.click_tab_city()
        assert self.APP.actions_in_main_page.get_text_on_tab_city() == "Нижний Новгород"


    def test_check_search(self):
        self.APP.actions_in_main_page.send_keys_in_search("Гвозди")
        self.APP.actions_in_main_page.click_button_search()
        time.sleep(1)
        assert 'https://mail.ru/search' in self.APP.actions_in_main_page.get_current_url()
        assert self.APP.actions_in_page_search.get_text_tab_search() == "поиск"

    def test_go_to_tab_games(self):
        self.APP.actions_in_main_page.click_tab_games()
        assert self.APP.actions_in_main_page.get_text_on_tab_games() == "Игры"