from fw.fw_base import FWBase
from selenium.webdriver.common.by import By

class Locator:
    id_tab_city = (By.XPATH, '//a[@data-testid="news-tabs-tab-item-regional"]')
    xpath_frame_search = (By.XPATH, '//iframe[contains(@class, "search-arrow__frame")]')
    xpath_input_search = (By.XPATH, '//input[contains(@class, "arrow__input")]')
    id_button_search = (By.XPATH, '//button[@data-testid="search-button"]')


class ActionsInMainPage(FWBase):

    def click_tab_city(self):
        self.click_element(Locator.id_tab_city)
        return self

    def get_text_on_tab_city(self):
        return self.find_element(Locator.id_tab_city).text

    def send_keys_in_search(self, text):
        self.send_keys_to_i_frame(Locator.xpath_frame_search, Locator.xpath_input_search, text)

    def click_button_search(self):
        self.click_element(Locator.id_button_search)