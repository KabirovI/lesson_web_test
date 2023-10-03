from selenium.webdriver.common.by import By

from fw.fw_base import FWBase


class Locator:
    xpath_tab_search = (By.XPATH, '//iframe[@class="yandex-frame"]')
    xpath_tab_search_text = (By.XPATH, '//a[contains(@class, "Tab_selected")]')


class ActionsInPageSearch(FWBase):

    def get_text_tab_search(self):
        self.switch_to_i_frame(Locator.xpath_tab_search)
        return self.find_element(Locator.xpath_tab_search_text).text