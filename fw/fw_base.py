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

    def switch_to_i_frame(self, locator):
        frame = self.find_element(locator)
        self.GetDriver().switch_to.frame(frame)

    def switch_to_default(self):
        self.GetDriver().switch_to.default_content()

    def send_keys_to_i_frame(self, locator_frame, locator_element, text):
        self.switch_to_i_frame(locator_frame)
        self.send_keys(locator_element, text)
        self.switch_to_default()

    def send_keys(self, locator, text):
        web_element = self.find_element(locator)
        web_element.send_keys(text)

    def get_current_url(self):
        return self.GetDriver().current_url

