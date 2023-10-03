from data.settings import Settings
from fw.application_manager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_class(self):
        pass

    def setup_method(self):
        self.APP.driver_instance.get_driver().get(Settings.main_page)

    def teardown_class(self):
        pass

    def teardown_method(self):
        self.APP.driver_instance.stop_driver()