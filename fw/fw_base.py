from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class FWBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def click_element(self, locator):
        web_element = self.find_element(locator)
        web_element.click()


    def find_element(self, locator):
        web_element = WebDriverWait(self.GetDriver(), 30).until(EC.presence_of_element_located(locator))
        return web_element

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver