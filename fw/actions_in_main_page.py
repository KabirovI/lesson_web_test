from fw.fw_base import FWBase
from selenium.webdriver.common.by import By

class Locator:
    id_tab_city = (By.XPATH, '//a[@data-testid="news-tabs-tab-item-regional"]')

class ActionsInMainPage(FWBase):

    def click_tab_city(self):
        self.click_element(Locator.id_tab_city)
        return self